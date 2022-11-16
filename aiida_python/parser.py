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
        x = CalculationFactory(self.node.process_type.split(':')[1])._process_docs

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

        return ExitCode(0)
