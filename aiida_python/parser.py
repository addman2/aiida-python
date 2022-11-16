# -*- coding: utf-8 -*-

from aiida.engine import ExitCode
from aiida.parsers.parser import Parser
from aiida.plugins import CalculationFactory
from aiida.common import exceptions
from aiida.orm import (Int,
                       Float,
                       SinglefileData)
from aiida_python.data import IHideYouHolder
from aiida_python.calc import (INFILE,
                               OUTFILE)
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

        output_filename = self.node.get_option("output_filename")
        files_retrieved = self.retrieved.list_object_names()
        serializers = self.node.get_option("serializers")
        docs = CalculationFactory(self.node.process_type.split(':')[1]).run_python.__doc__
        print(self.get_outputs_for_parsing())

        import pkg_resources
        def deserialize_this(obj):
            for entry_point in pkg_resources.iter_entry_points('aiida_python.serializers'):
                if entry_point.name in serializers:
                    obj = entry_point.load().deserialize(obj)
            return obj

        with self.retrieved.open(OUTFILE, 'rb') as handle:
            import pickle
            everything = pickle.load(handle)
            for key, value in everything.items():
                save_output = deserialize_this(value)
                self.out(key, save_output)

        if not docs: docs = ""
        for line in docs.split("\n"):
            m = re.match(r'.*!!file\s+(.+):\s*([_a-zA-Z0-9]+)\s*$', line)
            if m:
                #if m.group(1) not in self.outputs: continue
                with self.retrieved.open(m.group(2), "rb") as fhandle_input:
                     file = SinglefileData(file=fhandle_input)
                     print(f"Setting {m.group(1)} as {m.group(2)}")
                     self.out(m.group(1), file)

        print(self.outputs)
        return ExitCode(0)
