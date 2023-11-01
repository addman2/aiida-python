# -*- coding: utf-8 -*-
from aiida.orm import (Int, Float, Str, List, ArrayData)
from aiida.plugins import CalculationFactory
import pytest

CalcJobPython = CalculationFactory('aiida-python.calc')


class ClassThatCannotStartWithTestExample(CalcJobPython):
    @classmethod
    def define(cls, spec):
        super().define(spec)

        spec.input('inputarray', valid_type=ArrayData)
        spec.input('repeats', valid_type=Int)
        spec.output('value', valid_type=Float)

    def run_python(self):
        helpme = 'o pona e mi!'
        import numpy as np

        a = self.inputs.inputarray
        repeats = self.inputs.repeats
        a_inv = np.linalg.inv(a)

        for ii in range(repeats):
            a_inv = np.matmul(a_inv, a_inv)
            a_inv = a_inv / sum(a_inv)

        a = np.linalg.inv(a)

        c = float(np.sum(a))
        self.outputs.value = c


@pytest.mark.filterwarnings('ignore:Creating AiiDA')
def test_example(aiida_local_code_factory, clear_database, entry_points):

    from aiida.plugins import CalculationFactory
    from aiida.engine import run
    import numpy as np

    executable = 'python3'
    entry_point = 'test.calc_example'
    group = 'aiida.calculations'

    entry_points.add(ClassThatCannotStartWithTestExample,
                     f'{group}:{entry_point}')

    code = aiida_local_code_factory(entry_point=entry_point,
                                    executable=executable)
    calculation = CalculationFactory(entry_point)

    np_a = np.array([[1, 2, 1], [3, 4, 3], [0, 1, 1]])
    a = ArrayData()
    a.set_array('only_one', np_a)

    inputs = {'code': code, 'inputarray': a, 'repeats': Int(10)}

    result = run(calculation, **inputs)


@pytest.mark.filterwarnings('ignore:Creating AiiDA')
def test_example_codelog(aiida_local_code_factory, clear_database,
                         entry_points):

    from aiida.plugins import CalculationFactory
    from aiida.engine import run
    import numpy as np

    executable = 'python3'
    entry_point = 'test.calc_example'
    group = 'aiida.calculations'

    entry_points.add(ClassThatCannotStartWithTestExample,
                     f'{group}:{entry_point}')

    code = aiida_local_code_factory(entry_point=entry_point,
                                    executable=executable)
    calculation = CalculationFactory(entry_point)

    np_a = np.array([[1, 2, 1], [3, 4, 3], [0, 1, 1]])
    a = ArrayData()
    a.set_array('only_one', np_a)

    inputs = {'code': code, 'inputarray': a, 'repeats': Int(10)}

    result = run(calculation, **inputs)
    assert 'o pona e mi!' in result['run_code'].value
