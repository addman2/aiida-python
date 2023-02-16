# -*- coding: utf-8 -*-

"""
Test goleval
"""

def test_GOLEval(aiida_local_code_factory, clear_database, entry_points):

    import numpy as np
    from aiida.engine import run
    from aiida.orm import Int
    from aiida.plugins import CalculationFactory
    from aiida.plugins import DataFactory

    calc_entry_point = 'aiida_python.example.goleval'
    data_entry_point = 'aiida_python.gol.system'
    executable = 'python3'

    goleval = CalculationFactory(calc_entry_point)
    golsystem = DataFactory(data_entry_point)

    code = aiida_local_code_factory(entry_point=calc_entry_point, executable=executable)
    gs = golsystem(np.array([[True, False],[False, False]]))

    inputs = { "input_system" : gs,
               "steps" : Int(1),
               "code" : code }

    result = run(goleval, **inputs)
    array = result["output_system"].as_array()

    assert not array[0][0]
    assert not array[0][1]
    assert not array[1][0]
    assert not array[1][1]
