from aiida.orm import Int
from aiida.plugins import CalculationFactory

CalcJobPython = CalculationFactory("aiida_python.calc")
class ClassThatCannotStartWithTestAndHasBadIndent(CalcJobPython):

  @classmethod
  def define(cls, spec):
      super().define(spec)

      spec.input('koza', valid_type=Int)
      spec.output('ovca', valid_type=Int)

  def run_python(self):
   a = self.inputs.koza
   b = a + 2
   self.outputs.ovca = b
   print(a)
