from aiida.orm import (Int, Float)
from aiida.plugins import CalculationFactory

CalcJobPython = CalculationFactory("aiida_python.calc")
class ClassThatCannotStartWithTestInt(CalcJobPython):

    @classmethod
    def define(cls, spec):
        super().define(spec)

        spec.input('koza', valid_type=Int)
        spec.output('ovca', valid_type=Int)

    def run_python(self):
        a = self.inputs.koza
        b = a + 1
        self.outputs.ovca = b

class ClassThatCannotStartWithTestFloat(CalcJobPython):

    @classmethod
    def define(cls, spec):
        super().define(spec)

        spec.input('koza', valid_type=Float)
        spec.output('ovca', valid_type=Float)

    def run_python(self):
        a = self.inputs.koza
        b = a + 1
        self.outputs.ovca = b

def test_simple_code_int(aiida_local_code_factory, clear_database):
    from aiida.plugins import CalculationFactory
    from aiida.engine import run
    from aiida.orm import Int

    executable = 'python3'
    entry_point = 'test.calc_int'

    code = aiida_local_code_factory(entry_point=entry_point, executable=executable)
    calculation = CalculationFactory(entry_point)

    inputs = { 'code': code,
               'koza': Int(1)}

    result = run(calculation, **inputs)

    assert result['ovca'] == 2

def test_simple_code_float(aiida_local_code_factory, clear_database):
    from aiida.plugins import CalculationFactory
    from aiida.engine import run
    from aiida.orm import Int

    executable = 'python3'
    entry_point = 'test.calc_float'

    code = aiida_local_code_factory(entry_point=entry_point, executable=executable)
    calculation = CalculationFactory(entry_point)

    inputs = { 'code': code,
               'koza': Float(1.0)}

    result = run(calculation, **inputs)

    assert result['ovca'] == 2.0
