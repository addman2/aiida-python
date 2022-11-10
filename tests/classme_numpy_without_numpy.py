from aiida.orm import (Int,
                       List)
from aiida.plugins import CalculationFactory

from aiida_python.serializers import Serializer
from aiida.orm import List

class SerializerList(Serializer):

    #def __new__(cls, obj):
    #    from aiida.orm import List
    #    cls.philemon = List
    #    cls.baukis = list
    #    return Serializer.__new__(cls, obj)

    @classmethod
    def serialize(cls, obj):
        import os
        import numpy as np
        os.system("echo ser >> /home/addman/g")
        if isinstance(obj, List):
            return np.array(obj.get_list())
        return obj

    @classmethod
    def deserialize(cls, obj):
        import os
        if isinstance(obj, list):
            return list(obj)
        return obj

CalcJobPython = CalculationFactory("aiida_python.calc")
class ClassThatCannotStartWithTestAndWorksWithNumpyButIsWithoutNumpy(CalcJobPython):

    @classmethod
    def define(cls, spec):
        super().define(spec)

        spec.input('koza', valid_type=List)
        spec.input('krava', valid_type=Int)
        spec.output('ovca', valid_type=Int)

        #serializers = spec.inputs['metadata']['options']['serializers'].default
        #serializers.append("test.serializerlist")
        #serializers.append("int")
        #spec.inputs['metadata']['options']['serializers'].default = serializers

    def run_python(self):
        a = sum(self.inputs.koza)
        b = a * self.krava
        self.outputs.ovca = 9
