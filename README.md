# AiiDA Python

This package is an AiiDA plugin allowing you to run python code as `CalcJob` on a remote computer. Usage is easy one has to inherit CalcJobPython class and instead of `prepare_for_submition` method one ahs to overload `run_python`. Parser is generated automatically one does not have to write its own.


```from aiida.orm import (Int, Float, Str, List, ArrayData)
from aiida.plugins import CalculationFactory

CalcJobPython = CalculationFactory("aiida_python.calc")

class ClassThatCannotStartWithTestExample(CalcJobPython):

    @classmethod
    def define(cls, spec):
        super().define(spec)

        spec.input('inputarray', valid_type=ArrayData)
        spec.input('repeats', valid_type=Int)
        spec.output('value', valid_type=Float)

    def run_python(self):
        import numpy as np

        a = self.inputs.inputarray
        repeats = self.inputs.repeats
        a_inv = np.linalg.inv(a)

        for ii in range(repeats):
            a_inv = np.matmul(a_inv, a_inv)
            a_inv = a_inv/sum(a_inv)

        a = np.linalg.inv(a)

        c = float(np.sum(a))
        self.outputs.value = c
```
Here is a test case example
```
def test_example(aiida_local_code_factory, clear_database):
    from aiida.plugins import CalculationFactory
    from aiida.engine import run
    import numpy as np

    executable = 'python3'
    entry_point = 'test.calc_example'

    code = aiida_local_code_factory(entry_point=entry_point, executable=executable)
    calculation = CalculationFactory(entry_point)

    np_a = np.array([[1,2,1],[3,4,3],[0,1,1]])
    a = ArrayData()
    a.set_array("only_one", np_a)

    inputs = { 'code': code,
               'inputarray': a,
               'repeats': Int(10)}

    result = run(calculation, **inputs)
```

For more information look at this [link](https://aiida-python.readthedocs.io/en/latest/).
