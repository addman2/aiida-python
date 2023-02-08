# -*- coding: utf-8 -*-

"""
Test system serializer
"""

def test_SerializerGOL(aiida_local_code_factory, clear_database):

    import functools
    import numpy as np

    from aiida.orm import Int
    from aiida.orm import ArrayData

    from aiida_python import SerializerArrayData

    a = np.array([[True,True],[True,False]])

    #assert isinstance(ans, np.ndarray)

    #assert np.sum(ans - a) < 0.0001

    #obj = Int(2)
    #ans = SerializerArrayData.serialize(obj)

    #assert ans is obj

    #ans = SerializerArrayData.deserialize(a)

    #assert isinstance(ans, ArrayData)

    #ans = SerializerArrayData.deserialize(2)

    #assert ans is 2
