# -*- coding: utf-8 -*-

from aiida.engine import ExitCode
from aiida.parsers.parser import Parser
from aiida.plugins import CalculationFactory
from aiida.common import exceptions
from aiida.orm import Int, Float, SinglefileData
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

        :returns: an exit code, if parsing fails (or nothing if parsing succeeds)
        """

        output_filename = self.node.get_option("output_filename")
        files_retrieved = self.retrieved.list_object_names()

        with self.retrieved.open(OUTFILE, 'rb') as handle:
            import pickle
            everything = pickle.load(handle)
            for key, value in everything.items():
                save_output = {int: Int,
                               float: Float}[type(value)](value)
                self.out(key, save_output)

        return ExitCode(0)
