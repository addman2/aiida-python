# -*- coding: utf-8 -*-
"""
Test system serializer
"""

import sys
import pathlib
import pytest
import functools
import importlib

from conftest import setup_gol

from aiida.plugins import DataFactory

@pytest.mark.filterwarnings('ignore:Creating AiiDA')
@setup_gol
def test_SerializerGOL(aiida_local_code_factory, clear_database, entry_points):

    import functools
    import numpy as np

    from aiida.orm import Int
    from aiida.orm import ArrayData

    serializer = tuple(
        entry_points.eps().select(group='aiida_python.serializers',
                                  name='aiida_python.gol.system'))[0].load()

    data = tuple(
        entry_points.eps().select(group='aiida.data',
                                  name='aiida_python.gol.system'))[0].load()

    DataFactory("aiida.gol.system")
    from aiida.plugins import load_entry_point
    load_entry_point("aiida.data", "aiida_python.gol.system")

    #obj = serializer.deserialize(np.array([[True, True], [True, False]]))
    #array = serializer.serialize(obj)

    #assert array[0][0]
    #assert array[0][1]
    #assert array[1][0]
    #assert not array[1][1]

