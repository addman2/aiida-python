from aiida.orm import (Int,
                       List)
from aiida.plugins import CalculationFactory

from aiida_python.serializers import Serializer

class SerializerList(Serializer):

    def __new__(cls, obj):
        from aiida.orm import List
        cls.philemon = List
        cls.baukis = list
        return Serializer.__new__(cls, obj)

    @classmethod
    def serialize(cls, obj):
        import os
        import numpy as np
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
class ClassThatCannotStartWithTestAndWorksWithNumpy(CalcJobPython):

  @classmethod
  def define(cls, spec):
      super().define(spec)

      spec.input('koza', valid_type=List)
      spec.input('krava', valid_type=Int)
      spec.output('ovca', valid_type=Int)

      serializers = spec.inputs['metadata']['options']['serializers'].default
      serializers.append("test.serializerlist")

  def run_python(self):
      a = self.inputs.koza * self.krava
      a = sum(a)
      self.outputs.ovca = 9 #int(a)
