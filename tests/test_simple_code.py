from aiida.orm import (Int, Float, Str, List)
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

class ClassThatCannotStartWithTestStr(CalcJobPython):

    @classmethod
    def define(cls, spec):
        super().define(spec)

        spec.input('koza', valid_type=Str)
        spec.output('ovca', valid_type=Str)

    def run_python(self):
        a = self.inputs.koza
        if a == "sina toki uta e toki pona anu seme?":
            b = "mi toki e toki pona lili"
        else:
            b = "mi sona ala"
        self.outputs.ovca = b

class ClassThatCannotStartWithTestList(CalcJobPython):

    @classmethod
    def define(cls, spec):
        super().define(spec)

        spec.input('koza', valid_type=List)
        spec.output('ovca', valid_type=Int)
        spec.output('krava', valid_type=List)

    def run_python(self):
        a = self.inputs.koza
        b = sum(a)
        c = a
        c[0] += 1
        self.outputs.ovca = b
        self.outputs.krava = c

class ClassThatCannotStartWithTestArrayData(CalcJobPython):

    @classmethod
    def define(cls, spec):
        super().define(spec)

        spec.input('koza', valid_type=ArrayData)
        spec.output('ovca', valid_type=Int)
        spec.output('krava', valid_type=ArrayData)

    def run_python(self):
        import numpy as np

        a = self.inputs.koza
        b = np.sum(a)
        c = a
        c[0] += 1
        self.outputs.ovca = b
        self.outputs.krava = c

def test_simple_code_int(aiida_local_code_factory, clear_database):
    from aiida.plugins import CalculationFactory
    from aiida.engine import run

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

    executable = 'python3'
    entry_point = 'test.calc_float'

    code = aiida_local_code_factory(entry_point=entry_point, executable=executable)
    calculation = CalculationFactory(entry_point)

    inputs = { 'code': code,
               'koza': Float(1.0)}

    result = run(calculation, **inputs)

    assert result['ovca'] == 2.0

def test_simple_code_str(aiida_local_code_factory, clear_database):
    from aiida.plugins import CalculationFactory
    from aiida.engine import run

    executable = 'python3'
    entry_point = 'test.calc_str'

    code = aiida_local_code_factory(entry_point=entry_point, executable=executable)
    calculation = CalculationFactory(entry_point)

    inputs = { 'code': code,
               'koza': Str("sina toki uta e toki pona anu seme?")}

    result = run(calculation, **inputs)

    assert result['ovca'] == "mi toki e toki pona lili"

    inputs = { 'code': code,
               'koza': Str("Excuse me do you speak my language?")}

    result = run(calculation, **inputs)

    assert result['ovca'] == "mi sona ala"

def test_simple_code_list(aiida_local_code_factory, clear_database):
    from aiida.plugins import CalculationFactory
    from aiida.engine import run

    executable = 'python3'
    entry_point = 'test.calc_list'

    code = aiida_local_code_factory(entry_point=entry_point, executable=executable)
    calculation = CalculationFactory(entry_point)

    inputs = { 'code': code,
               'koza': List([1, 2, 3])}

    result = run(calculation, **inputs)

    assert result['ovca'] == 6

    import functools
    # o linja mute mute
    assert functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,[2,2,3],result['krava']), True)
