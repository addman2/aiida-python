# -*- coding: utf-8 -*-

class Serializer():

    pass

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
