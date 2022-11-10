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

def test_SerializerStr():

    from aiida.orm import Int
    from aiida.orm import Str

    from aiida_python import SerializerStr

    message = "Anitta DUMU Pithaana LUGAL Kuusara QIBI"
    obj = Str(message)
    ans = SerializerStr.serialize(obj)

    assert isinstance(ans, str)
    assert ans == message

    obj = Int(2)
    ans = SerializerStr.serialize(obj)

    assert ans is obj

    ans = SerializerStr.deserialize(message)

    assert isinstance(ans, Str)
