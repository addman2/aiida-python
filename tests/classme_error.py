from aiida.orm import (Int,
                       List)
from aiida.plugins import CalculationFactory

from aiida_python.serializers import Serializer

CalcJobPython = CalculationFactory("aiida_python.calc")
class ClassThatCannotStartWithTestAndDoesError(CalcJobPython):

  @classmethod
  def define(cls, spec):
      super().define(spec)

      spec.input('koza', valid_type=List)
      spec.input('krava', valid_type=Int)
      spec.output('ovca', valid_type=Int)

  def run_python(self):
      self.outputs.ovca = 9
