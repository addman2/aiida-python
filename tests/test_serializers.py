# -*- coding: utf-8 -*-
"""
Test serializers
"""


def test_SerializerInt():

    from aiida.orm import Int
    from aiida.orm import Float

    from aiida_python import SerializerInt

    obj = Int(2)
    ans = SerializerInt.serialize(obj)

    assert isinstance(ans, int)
    assert ans == 2

    obj = Float(2)
    ans = SerializerInt.serialize(obj)

    assert ans is obj

    ans = SerializerInt.deserialize(2)

    assert isinstance(ans, Int)

    ans = SerializerInt.deserialize(2.0)

    assert ans == 2.0


def test_SerializerFloat():

    from aiida.orm import Int
    from aiida.orm import Float

    from aiida_python import SerializerFloat

    obj = Float(2.0)
    ans = SerializerFloat.serialize(obj)

    assert isinstance(ans, float)
    assert ans == 2

    obj = Int(2)
    ans = SerializerFloat.serialize(obj)

    assert ans is obj

    ans = SerializerFloat.deserialize(2.0)

    assert isinstance(ans, Float)

    ans = SerializerFloat.deserialize(2)

    assert ans == 2


def test_SerializerStr():

    from aiida.orm import Int
    from aiida.orm import Str

    from aiida_python import SerializerStr

    message = 'Anitta DUMU Pithaana LUGAL Kuusara QIBI'
    obj = Str(message)
    ans = SerializerStr.serialize(obj)

    assert isinstance(ans, str)
    assert ans == message

    obj = Int(2)
    ans = SerializerStr.serialize(obj)

    assert ans is obj

    ans = SerializerStr.deserialize(message)

    assert isinstance(ans, Str)

    ans = SerializerStr.deserialize(2)

    assert ans == 2


def test_SerializerList():

    import functools

    from aiida.orm import Int
    from aiida.orm import List

    from aiida_python import SerializerList

    l = [1, 2, 3]
    obj = List(l)
    ans = SerializerList.serialize(obj)

    assert isinstance(ans, list)

    # o linja mute mute
    assert functools.reduce(lambda x, y: x and y,
                            map(lambda p, q: p == q, l, ans), True)

    obj = Int(2)
    ans = SerializerList.serialize(obj)

    assert ans is obj

    ans = SerializerList.deserialize(l)

    assert isinstance(ans, List)

    ans = SerializerList.deserialize(2)

    assert ans == 2


def test_SerializerArrayData():

    import functools
    import numpy as np

    from aiida.orm import Int
    from aiida.orm import ArrayData

    from aiida_python import SerializerArrayData

    a = np.array([[1, 2], [3, 4]])
    obj = ArrayData()
    obj.set_array('only_one', a)
    ans = SerializerArrayData.serialize(obj)

    assert isinstance(ans, np.ndarray)

    assert np.sum(ans - a) < 0.0001

    obj = Int(2)
    ans = SerializerArrayData.serialize(obj)

    assert ans is obj

    ans = SerializerArrayData.deserialize(a)

    assert isinstance(ans, ArrayData)

    ans = SerializerArrayData.deserialize(2)

    assert ans is 2
