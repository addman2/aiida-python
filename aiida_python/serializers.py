# -*- coding: utf-8 -*-

from aiida.orm import (Int, Float)

class Serializer():

    pass

class SerializerInt(Serializer):

    @classmethod
    def baukis(cls):
        return int

    @classmethod
    def philemon(cls):
        return Int

    @classmethod
    def serialize(cls, obj):
        if isinstance(obj, cls.philemon()):
            return obj.value
        return obj

    @classmethod
    def deserialize(cls, obj):
        if isinstance(obj, cls.baukis()):
            return cls.philemon()(obj)
        return obj

class SerializerFloat(Serializer):

    @classmethod
    def baukis(cls):
        return float

    @classmethod
    def philemon(cls):
        return Float

    @classmethod
    def serialize(cls, obj):
        if isinstance(obj, cls.philemon()):
            return obj.value
        return obj

    @classmethod
    def deserialize(cls, obj):
        if isinstance(obj, cls.baukis()):
            return cls.philemon()(obj)
        return obj
