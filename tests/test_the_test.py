# -*- coding: utf-8 -*-

"""
Test the functionality
"""

def test_the_test(aiida_local_code_factory, clear_database):
    from aiida.plugins import CalculationFactory
    from aiida.engine import run
    from aiida.orm import Int

    executable = 'python3'
    entry_point = 'test.calc'

    code = aiida_local_code_factory(entry_point=entry_point, executable=executable)
    calculation = CalculationFactory(entry_point)

    inputs = { 'code': code,
               'koza': Int(1)}

    result = run(calculation, **inputs)

    assert result['ovca'] == 2

def test_the_test_bad_indent(aiida_local_code_factory, clear_database):
    from aiida.plugins import CalculationFactory
    from aiida.engine import run
    from aiida.orm import Int

    executable = 'python3'
    entry_point = 'test.calc_bi'

    code = aiida_local_code_factory(entry_point=entry_point, executable=executable)
    calculation = CalculationFactory(entry_point)

    inputs = { 'code': code,
               'koza': Int(10)}

    result = run(calculation, **inputs)

    assert result['ovca'] == 12
