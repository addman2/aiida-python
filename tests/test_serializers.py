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

def test_SerializerFloat():

    from aiida.orm import Int
    from aiida.orm import Float

    from aiida_python import SerializerFloat

    obj = Float(2)
    ans = SerializerFloat.serialize(obj)

    assert isinstance(ans, float)
    assert ans == 2

    obj = Int(2)
    ans = SerializerFloat.serialize(obj)

    assert ans is obj

def test_SerializerStr():

    from aiida.orm import Int
    from aiida.orm import Str

    from aiida_python import SerializerStr

    message = "Anitta hassuwas"

    obj = Str(message)
    ans = SerializerStr.serialize(obj)

    assert isinstance(ans, str)
    assert ans == message

    obj = Int(2)
    ans = SerializerStr.serialize(obj)

    assert ans is obj

def test_de_SerializerInt():

    from aiida.orm import Int
    from aiida.orm import Float

    from aiida_python import SerializerInt

    obj = int(42)
    ans = SerializerInt.deserialize(obj)

    assert isinstance(ans, Int)
    assert ans == 42

    obj = float(42)
    ans = SerializerInt.deserialize(obj)

    assert isinstance(ans, float)
    assert ans == 42

def test_de_SerializerFloat():

    from aiida.orm import Int
    from aiida.orm import Float

    from aiida_python import SerializerFloat

    obj = float(2)
    ans = SerializerFloat.deserialize(obj)

    assert isinstance(ans, Float)
    assert ans == 2

    obj = int(2)
    ans = SerializerFloat.deserialize(obj)

    assert isinstance(ans, int)
    assert ans == 2

def test_de_SerializerStr():

    from aiida.orm import Int
    from aiida.orm import Str

    from aiida_python import SerializerStr

    message = "Anitta hassuwas"

    obj = str(message)
    ans = SerializerStr.deserialize(obj)

    assert isinstance(ans, Str)
    assert ans == message

    obj = int(2)
    ans = SerializerStr.deserialize(obj)

    assert isinstance(ans, int)
    assert ans == 2
