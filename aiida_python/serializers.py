# -*- coding: utf-8 -*-

from aiida.orm import (Int, Float, Str, List, ArrayData)
import numpy as np


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


class SerializerArrayData(Serializer):
    @classmethod
    def baukis(cls):
        return np.ndarray

    @classmethod
    def philemon(cls):
        return ArrayData

    @classmethod
    def serialize(cls, obj):
        if isinstance(obj, cls.philemon()):
            return obj.get_array('only_one')
        return obj

    @classmethod
    def deserialize(cls, obj):
        if isinstance(obj, cls.baukis()):
            ret = cls.philemon()()
            ret.set_array('only_one', obj)
            return ret
        return obj
