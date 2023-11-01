# -*- coding: utf-8 -*-

import numpy as np
from aiida.plugins import DataFactory

import pathlib

TEST_DIR = pathlib.Path(__file__).resolve().parent
"""
Test golsystem
"""


def test_GOLSystem(aiida_local_code_factory, clear_database):

    golsystem = DataFactory('aiida_python.gol.system')
    gs = golsystem(np.array([[True, False], [False, False]]))
    gs.store()

    assert gs.attributes['array'][0][0] == True
    assert gs.attributes['array'][0][1] == False
    assert gs.attributes['array'][1][0] == False
    assert gs.attributes['array'][1][1] == False


def test_GOLSystem_as_array(aiida_local_code_factory, clear_database):

    golsystem = DataFactory('aiida_python.gol.system')
    gs = golsystem(np.array([[True, False], [False, False]]))
    gs.store()

    array = gs.as_array()

    assert array[0][0] == True
    assert array[0][1] == False
    assert array[1][0] == False
    assert array[1][1] == False


def test_GOLSystem_load_from_bitmap(aiida_local_code_factory, clear_database):

    from PIL import Image

    img = Image.open(TEST_DIR / 'Situation_1.bmp')

    golsystem = DataFactory('aiida_python.gol.system')
    gs = golsystem(img)
    gs.store()

    height, width = gs.get_dimensions()

    assert height == 20
    assert width == 20


def test_GOLSystem_load_from_bitmap_2(aiida_local_code_factory,
                                      clear_database):

    from PIL import Image

    img = Image.open(TEST_DIR / 'Situation_1.bmp')

    golsystem = DataFactory('aiida_python.gol.system')
    gs = golsystem(img)
    gs.store()

    height, width = gs.get_dimensions()

    gs.get_bitmap().save('Situation_2.bmp')
