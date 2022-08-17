# -*- coding: utf-8 -*-

"""
Test serializers
"""

def test_SerializerInt():

    from aiida.orm import Int
    from aiida.orm import Float

    from aiida_python import SerializerInt

    obj = Int(2)
    ans = SerializerInt(obj)

    assert isinstance(ans, int)
    assert ans == 2

    obj = Float(2)
    ans = SerializerInt(obj)

    assert ans is obj

def test_SerializerFloat():

    from aiida.orm import Int
    from aiida.orm import Float

    from aiida_python import SerializerFloat

    obj = Float(2)
    ans = SerializerFloat(obj)

    assert isinstance(ans, float)
    assert ans == 2

    obj = Int(2)
    ans = SerializerFloat(obj)

    assert ans is obj

def test_SerializerStr():

    from aiida.orm import Int
    from aiida.orm import Str

    from aiida_python import SerializerStr

    message = "Anitta hassuwas"

    obj = Str(message)
    ans = SerializerStr(obj)

    assert isinstance(ans, str)
    assert ans == message

    obj = Int(2)
    ans = SerializerStr(obj)

    assert ans is obj
