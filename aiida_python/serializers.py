# -*- coding: utf-8 -*-

from aiida.orm import (Int, Float, Str, List)

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

class SerializerStr(Serializer):

    @classmethod
    def baukis(cls):
        return str

    @classmethod
    def philemon(cls):
        return Str

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

class SerializerList(Serializer):

    @classmethod
    def baukis(cls):
        return list

    @classmethod
    def philemon(cls):
        return List

    @classmethod
    def serialize(cls, obj):
        if isinstance(obj, cls.philemon()):
            return obj.get_list()
        return obj

    @classmethod
    def deserialize(cls, obj):
        if isinstance(obj, cls.baukis()):
            return cls.philemon()(obj)
        return obj
