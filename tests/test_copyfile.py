# -*- coding: utf-8 -*-
from aiida.orm import (Int, Float, Str, List, ArrayData, SinglefileData)
from aiida.plugins import CalculationFactory
import pytest

CalcJobPython = CalculationFactory('aiida-python.calc')

SUCCESS_MSG = 'Succesfull run'


class ClassThatCannotStartWithTestCopyFile(CalcJobPython):
    @classmethod
    def define(cls, spec):
        super().define(spec)

        spec.input('repeats', valid_type=Int)
        spec.input('inputfile', valid_type=SinglefileData)
        spec.output('value', valid_type=Float)
        spec.output('output', valid_type=SinglefileData)

    def run_python(self):
        """
        This is commentary

        This file will be stored in the working directory:
        !file inputfile: data

        Unset ports will be ignored:
        !file inputfile2: data2

        Store output
        !!file output: output
        """
        import numpy as np
        import pickle as pkl

        with open('data', 'rb') as fhandle:
            x = pkl.load(fhandle)
        with open('output', 'w') as fhandle:
            fhandle.write('Succesfull run')
        average = np.average(x)
        self.outputs.value = average


@pytest.mark.filterwarnings('ignore:Creating AiiDA')
def test_copyfile(aiida_local_code_factory, clear_database, entry_points):

    from aiida.plugins import CalculationFactory
    from aiida.engine import run
    from . import TEST_DIR

    executable = 'python3'
    entry_point = 'test.calc_copyfile'
    group = 'aiida.calculations'

    entry_points.add(ClassThatCannotStartWithTestCopyFile,
                     f'{group}:{entry_point}')

    code = aiida_local_code_factory(entry_point=entry_point,
                                    executable=executable)
    calculation = CalculationFactory(entry_point)
    with open(TEST_DIR / 'file', 'rb') as fhandle:
        inputfile = SinglefileData(file=fhandle)

    inputs = {'code': code, 'inputfile': inputfile, 'repeats': Int(10)}

    correct_average = 0.49740618733672
    result = run(calculation, **inputs)
    assert abs(result['value'].value - correct_average) < 0.01
    assert 'output' in result
    with result['output'].open(mode='r') as fhandle:
        assert fhandle.read() == SUCCESS_MSG
