from aiida.orm import (Int, Float, Str, List, ArrayData, SinglefileData)
from aiida.plugins import CalculationFactory

CalcJobPython = CalculationFactory("aiida_python.calc")

class ClassThatCannotStartWithTestCopyFile(CalcJobPython):

    @classmethod
    def define(cls, spec):
        super().define(spec)

        spec.input('repeats', valid_type=Int)
        spec.input('inputfile', valid_type=SinglefileData)
        spec.output('value', valid_type=Float)

    def run_python(self):
        """
        This is commentary

        !file inputfile: data
        """
        import numpy as np
        import pickle as pkl

        with open("data", "rb") as fhandle:
            x = pkl.load(fhandle)
        average = np.average(x)
        self.outputs.value = 0.0

def test_example(aiida_local_code_factory, clear_database):

    from aiida.plugins import CalculationFactory
    from aiida.engine import run
    from . import TEST_DIR

    executable = 'python3'
    entry_point = 'test.calc_copyfile'

    code = aiida_local_code_factory(entry_point=entry_point, executable=executable)
    calculation = CalculationFactory(entry_point)
    with open(TEST_DIR/"file", "rb") as fhandle:
        inputfile = SinglefileData(file=fhandle)

    inputs = { 'code': code,
               'inputfile': inputfile,
               'repeats': Int(10)}

    result = run(calculation, **inputs)
