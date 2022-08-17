# -*- coding: utf-8 -*-

class Serializer():

    def __new__(cls, obj):
        return cls.process(obj)

    @classmethod
    def process(cls, obj):
        return cls.serialize(obj)

    @classmethod
    def serialize(cls, obj):
        return obj

    @classmethod
    def deserialize(cls, obj):
        return obj

    @classmethod
    def __invert__(cls):
        dictionary = dict(cls.__dict__)
        dictionary["serialize"] = dictionary["deserialize"]
        return type('x', cls.__bases__, dictionary)

    @classmethod
    def i(cls):
        """
        My idea was to create a new class for deserialization
        when invert operator is invoked. However python does
        not supports operator overloading for classes unfortunatelly.
        """
        return cls.__invert__()

class SerializerInt(Serializer):

    from aiida.orm import Int
    philemon = Int
    baukis = int

    @classmethod
    def serialize(cls, obj):
        if isinstance(obj, cls.philemon):
            return obj.value
        return obj

    @classmethod
    def deserialize(cls, obj):
        if isinstance(obj, cls.baukis):
            return cls.philemon(obj)
        return obj

class SerializerFloat(Serializer):

    from aiida.orm import Float
    philemon = Float
    baukis = float

    @classmethod
    def serialize(cls, obj):
        if isinstance(obj, cls.philemon):
            return obj.value
        return obj

    @classmethod
    def deserialize(cls, obj):
        if isinstance(obj, cls.baukis):
            return cls.philemon(obj)
        return obj

class SerializerStr(Serializer):

    from aiida.orm import Str
    philemon = Str
    baukis = str

    @classmethod
    def serialize(cls, obj):
        if isinstance(obj, cls.philemon):
            return obj.value
        return obj

    @classmethod
    def deserialize(cls, obj):
        if isinstance(obj, cls.baukis):
            return cls.philemon(obj)
        return obj
