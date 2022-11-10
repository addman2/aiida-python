# -*- coding: utf-8 -*-

from aiida.orm import Int

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
