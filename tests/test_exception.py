# -*- coding: utf-8 -*-
from aiida.orm import (Int, Float, Str, List, ArrayData)
from aiida.plugins import CalculationFactory

CalcJobPython = CalculationFactory('aiida-python.calc')


class ClassThatCannotStartWithTestException(CalcJobPython):
    @classmethod
    def define(cls, spec):
        super().define(spec)

        spec.input('koza', valid_type=Int)
        spec.output('ovca', valid_type=Int)

    def run_python(self):
        self.outputs.ovca = 0
        raise Exception('ijo ike')


def test_simple_code_exception(aiida_local_code_factory, clear_database,
                               entry_points):
    from aiida.plugins import CalculationFactory
    from aiida.engine import run

    executable = 'python3'
    entry_point = 'test.calc_exception'
    group = 'aiida.calculations'

    entry_points.add(ClassThatCannotStartWithTestException,
                     f'{group}:{entry_point}')

    code = aiida_local_code_factory(entry_point=entry_point,
                                    executable=executable)
    calculation = CalculationFactory(entry_point)

    inputs = {'code': code, 'koza': Int(1)}

    result = run(calculation, **inputs)

    assert result['ovca'] == 0
    assert result['error_message'].value == 'ijo ike'
