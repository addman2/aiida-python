# -*- coding: utf-8 -*-

from aiida.engine import ExitCode
from aiida.parsers.parser import Parser
from aiida.plugins import CalculationFactory
from aiida.common import exceptions
from aiida.orm import (Int, Float, Str, SinglefileData)
from aiida_python.data import IHideYouHolder
from aiida_python.calc import (INFILE, OUTFILE, ERRFILE)
import re


class ParserPython(Parser):
    def __init__(self, node):
        """
        Initialize Parser instance

        :param node: ProcessNode of calculation
        :param type node: :class:`aiida.orm.ProcessNode`
        """
        super().__init__(node)

    def parse(self, **kwargs):
        """
        Parse outputs, store results in database.

        :returns: an exit code
        """

        output_filename = self.node.get_option('output_filename')
        input_filename = self.node.get_option('input_filename')
        files_retrieved = self.retrieved.list_object_names()
        serializers = self.node.get_option('serializers')
        docs = CalculationFactory(
            self.node.process_type.split(':')[1]).run_python.__doc__

        from aiida.plugins import entry_point as ep

        def deserialize_this(obj):
            for entry_point in ep.eps().select(
                    group='aiida_python.serializers'):
                if entry_point.name in serializers:
                    obj = entry_point.load().deserialize(obj)
            return obj

        if ERRFILE in self.retrieved.list_object_names():
            with self.retrieved.open(ERRFILE, 'r') as fhandle:
                self.out('error_message', Str(fhandle.read()))

        if OUTFILE not in self.retrieved.list_object_names():
            return ExitCode(300)

        with self.retrieved.open(OUTFILE, 'rb') as handle:
            import pickle
            everything = pickle.load(handle)
            for key, value in everything.items():
                save_output = deserialize_this(value)
                self.out(key, save_output)

        with self.retrieved.open(input_filename, 'r') as handle:
            code = handle.read()
            self.out('run_code', Str(code))

        if not docs: docs = ''
        for line in docs.split('\n'):
            m = re.match(r'.*!!file\s+(.+):\s*([_a-zA-Z0-9]+)\s*$', line)
            if m:
                with self.retrieved.open(m.group(2), 'rb') as fhandle_input:
                    file = SinglefileData(file=fhandle_input)
                    self.out(m.group(1), file)

        return ExitCode(0)
