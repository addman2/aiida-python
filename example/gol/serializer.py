# -*- coding: utf-8 -*-
from aiida_python import Serializer
from aiida.plugins import DataFactory


class SerializerGOLSystem(Serializer):
    @classmethod
    def baukis(cls):
        import numpy as np
        return np.ndarray

    @classmethod
    def philemon(cls):
        return DataFactory('aiida-python.gol.system')

    @classmethod
    def serialize(cls, obj):
        if isinstance(obj, cls.philemon()):
            return obj.attributes['array']
        return obj

    @classmethod
    def deserialize(cls, obj):
        if isinstance(obj, cls.baukis()):
            return cls.philemon()(array=obj)
        return obj
