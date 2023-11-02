# -*- coding: utf-8 -*-

import pathlib
import pytest

from conftest import setup_gol

TEST_DIR = pathlib.Path(__file__).resolve().parent
"""
Test goleval
"""


@pytest.mark.filterwarnings('ignore:Creating AiiDA',
                            'ignore:uknown type string')
@setup_gol
def test_GOLEval_1(aiida_local_code_factory, clear_database, entry_points):

    import numpy as np
    from aiida.engine import run
    from aiida.orm import Int
    from aiida.plugins import CalculationFactory
    from aiida.plugins import DataFactory

    calc_entry_point = 'aiida-python.example.goleval'
    data_entry_point = 'aiida-python.gol.system'
    executable = 'python3'

    goleval = CalculationFactory(calc_entry_point)
    golsystem = DataFactory(data_entry_point)

    code = aiida_local_code_factory(entry_point=calc_entry_point,
                                    executable=executable)
    gs = golsystem(np.array([[True, False], [False, False]]))

    inputs = {'input_system': gs, 'steps': Int(1), 'code': code}

    result = run(goleval, **inputs)
    array = result['output_system'].as_array()

    assert not array[0][0]
    assert not array[0][1]
    assert not array[1][0]
    assert not array[1][1]


@pytest.mark.filterwarnings('ignore:Creating AiiDA',
                            'ignore:uknown type string')
@setup_gol
def test_GOLEval_2(aiida_local_code_factory, clear_database, entry_points):

    import numpy as np
    from aiida.engine import run
    from aiida.orm import Int
    from aiida.plugins import CalculationFactory
    from aiida.plugins import DataFactory

    calc_entry_point = 'aiida-python.example.goleval'
    data_entry_point = 'aiida-python.gol.system'
    executable = 'python3'

    goleval = CalculationFactory(calc_entry_point)
    golsystem = DataFactory(data_entry_point)

    code = aiida_local_code_factory(entry_point=calc_entry_point,
                                    executable=executable)
    gs = golsystem(
        np.array([[False, False, False], [False, True, False],
                  [False, False, False]]))

    inputs = {'input_system': gs, 'steps': Int(1), 'code': code}

    result = run(goleval, **inputs)
    array = result['output_system'].as_array()

    assert not array[0][0]
    assert not array[0][1]
    assert not array[0][2]
    assert not array[1][0]
    assert not array[1][1]
    assert not array[1][2]
    assert not array[2][0]
    assert not array[2][1]
    assert not array[2][2]


@pytest.mark.filterwarnings('ignore:Creating AiiDA')
@setup_gol
def test_GOLEval_3(aiida_local_code_factory, clear_database, entry_points):

    import numpy as np
    from aiida.engine import run
    from aiida.orm import Int
    from aiida.plugins import CalculationFactory
    from aiida.plugins import DataFactory

    calc_entry_point = 'aiida-python.example.goleval'
    data_entry_point = 'aiida-python.gol.system'
    executable = 'python3'

    goleval = CalculationFactory(calc_entry_point)
    golsystem = DataFactory(data_entry_point)

    code = aiida_local_code_factory(entry_point=calc_entry_point,
                                    executable=executable)
    gs = golsystem(
        np.array([[False, False, False], [True, True, False],
                  [True, True, False]]))

    inputs = {'input_system': gs, 'steps': Int(1), 'code': code}

    result = run(goleval, **inputs)
    array = result['output_system'].as_array()

    assert not array[0][0]
    assert not array[0][1]
    assert not array[0][2]
    assert array[1][0]
    assert array[1][1]
    assert not array[1][2]
    assert array[2][0]
    assert array[2][1]
    assert not array[2][2]


@pytest.mark.filterwarnings('ignore:Creating AiiDA')
@setup_gol
def test_GOLEval_4(aiida_local_code_factory, clear_database, entry_points):

    import numpy as np
    from aiida.engine import run
    from aiida.orm import Int
    from aiida.plugins import CalculationFactory
    from aiida.plugins import DataFactory

    calc_entry_point = 'aiida-python.example.goleval'
    data_entry_point = 'aiida-python.gol.system'
    executable = 'python3'

    goleval = CalculationFactory(calc_entry_point)
    golsystem = DataFactory(data_entry_point)

    code = aiida_local_code_factory(entry_point=calc_entry_point,
                                    executable=executable)
    gs = golsystem(
        np.array([[False, True, False], [False, True, False],
                  [False, True, False]]))

    inputs = {'input_system': gs, 'steps': Int(1), 'code': code}

    result = run(goleval, **inputs)
    array = result['output_system'].as_array()

    assert not array[0][0]
    assert not array[0][1]
    assert not array[0][2]
    assert array[1][0]
    assert array[1][1]
    assert array[1][2]
    assert not array[2][0]
    assert not array[2][1]
    assert not array[2][2]

    gs = golsystem(
        np.array([[False, True, False], [False, True, False],
                  [False, True, False]]))

    inputs = {'input_system': gs, 'steps': Int(2), 'code': code}

    result = run(goleval, **inputs)
    array = result['output_system'].as_array()

    assert not array[0][0]
    assert array[0][1]
    assert not array[0][2]
    assert not array[1][0]
    assert array[1][1]
    assert not array[1][2]
    assert not array[2][0]
    assert array[2][1]
    assert not array[2][2]

    gs = golsystem(
        np.array([[False, True, False], [False, True, False],
                  [False, True, False]]))

    inputs = {'input_system': gs, 'steps': Int(3), 'code': code}

    result = run(goleval, **inputs)
    array = result['output_system'].as_array()

    assert not array[0][0]
    assert not array[0][1]
    assert not array[0][2]
    assert array[1][0]
    assert array[1][1]
    assert array[1][2]
    assert not array[2][0]
    assert not array[2][1]
    assert not array[2][2]


@pytest.mark.filterwarnings('ignore:Creating AiiDA')
@setup_gol
def test_GOLEval_5(aiida_local_code_factory, clear_database, entry_points):

    import numpy as np
    from aiida.engine import run
    from aiida.orm import Int, List
    from aiida.plugins import CalculationFactory
    from aiida.plugins import DataFactory

    calc_entry_point = 'aiida-python.example.goleval'
    data_entry_point = 'aiida-python.gol.system'
    executable = 'python3'

    goleval = CalculationFactory(calc_entry_point)
    golsystem = DataFactory(data_entry_point)

    code = aiida_local_code_factory(entry_point=calc_entry_point,
                                    executable=executable)
    gs = golsystem(
        np.array([[False, False, False], [False, True, False],
                  [False, False, False]]))

    inputs = {
        'input_system': gs,
        'steps': Int(1),
        'survive': List([0, 1, 2, 3]),
        'code': code
    }

    result = run(goleval, **inputs)
    array = result['output_system'].as_array()

    assert not array[0][0]
    assert not array[0][1]
    assert not array[0][2]
    assert not array[1][0]
    assert array[1][1]
    assert not array[1][2]
    assert not array[2][0]
    assert not array[2][1]
    assert not array[2][2]


@pytest.mark.filterwarnings('ignore:Creating AiiDA')
@setup_gol
def test_GOLEval_6(aiida_local_code_factory, clear_database, entry_points):

    import numpy as np
    from aiida.engine import run
    from aiida.orm import Int, List
    from aiida.plugins import CalculationFactory
    from aiida.plugins import DataFactory

    calc_entry_point = 'aiida-python.example.goleval'
    data_entry_point = 'aiida-python.gol.system'
    executable = 'python3'

    goleval = CalculationFactory(calc_entry_point)
    golsystem = DataFactory(data_entry_point)

    code = aiida_local_code_factory(entry_point=calc_entry_point,
                                    executable=executable)
    gs = golsystem(
        np.array([[False, False, False], [False, True, False],
                  [False, False, False]]))

    inputs = {
        'input_system': gs,
        'steps': Int(1),
        'survive': List([0, 1, 2, 3]),
        'born': List([1]),
        'code': code
    }

    result = run(goleval, **inputs)
    array = result['output_system'].as_array()

    assert array[0][0]
    assert array[0][1]
    assert array[0][2]
    assert array[1][0]
    assert array[1][1]
    assert array[1][2]
    assert array[2][0]
    assert array[2][1]
    assert array[2][2]

    inputs = {
        'input_system': result['output_system'],
        'steps': Int(1),
        'survive': List([0, 1, 2, 3]),
        'born': List([1]),
        'code': code
    }

    result = run(goleval, **inputs)
    array = result['output_system'].as_array()

    assert array[0][0]
    assert not array[0][1]
    assert array[0][2]
    assert not array[1][0]
    assert not array[1][1]
    assert not array[1][2]
    assert array[2][0]
    assert not array[2][1]
    assert array[2][2]


@pytest.mark.filterwarnings('ignore:Creating AiiDA')
@setup_gol
def test_GOLEval_7(aiida_local_code_factory, clear_database, entry_points):

    import numpy as np
    from aiida.engine import run
    from aiida.orm import Int, List
    from aiida.plugins import CalculationFactory
    from aiida.plugins import DataFactory
    from PIL import Image

    calc_entry_point = 'aiida-python.example.goleval'
    data_entry_point = 'aiida-python.gol.system'
    executable = 'python3'

    goleval = CalculationFactory(calc_entry_point)
    golsystem = DataFactory(data_entry_point)

    code = aiida_local_code_factory(entry_point=calc_entry_point,
                                    executable=executable)
    gs = golsystem(Image.open(TEST_DIR / 'Situation_1.bmp'))

    inputs = {'input_system': gs, 'steps': Int(20), 'code': code}

    result = run(goleval, **inputs)
    array = result['output_system'].as_array()

    height, width = gs.get_dimensions()

    assert height == 20
    assert width == 20
