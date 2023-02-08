from aiida_python import Serializer
from aiida.plugins import DataFactory

class SerializerInt(Serializer):

    @classmethod
    def baukis(cls):
        return np.array

    @classmethod
    def philemon(cls):
        return DataFactory("aiida_python.gol.system")

    @classmethod
    def serialize(cls, obj):
        if isinstance(obj, cls.philemon()):
            return obj.attributes["array"]
        return obj

    @classmethod
    def deserialize(cls, obj):
        if isinstance(obj, cls.baukis()):
            return cls.philemon()(array = obj)
        return obj

