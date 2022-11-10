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

def test_SerializerInt():

    from aiida.orm import Int
    from aiida.orm import Float

    from aiida_python import SerializerFloat

    obj = Float(2.0)
    ans = SerializerFloat.serialize(obj)

    assert isinstance(ans, float)
    assert ans == 2

    obj = Int(2)
    ans = SerializerInt.serialize(obj)

    assert ans is obj

    ans = SerializerInt.deserialize(2.0)

    assert isinstance(ans, Float)
