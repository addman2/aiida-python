from aiida.orm import (Int, Float, Str, List, ArrayData)
from aiida.plugins import CalculationFactory
from aiida.engine import calcfunction
import pytest
import numpy as np

CalcJobPython = CalculationFactory("aiida_python.calc")

class ClassThatCannotStartWithTestLastTime(CalcJobPython):

    @classmethod
    def define(cls, spec):
        super().define(spec)

        spec.input('inputarray', valid_type=ArrayData)
        spec.input('repeats', valid_type=Int)
        spec.output('value', valid_type=Float)

    def run_python(self):
        import numpy as np

        H = self.inputs.inputarray
        H_inv = np.linalg.inv(H)
        vec = np.random.rand(len(H))

        for _ in range(self.inputs.repeats):
            vec = H_inv @ vec
            vec /= np.linalg.norm(vec)

        self.outputs.value = np.average((H @ vec) / vec)

@calcfunction
def prepare_kinetic(size, inv_mass):
    arr = np.zeros((size.value,size.value))
    arr[0,0] = -2*inv_mass.value
    for ii in range(1,size.value):
        arr[ii, ii] = -2*inv_mass.value
        arr[ii-1, ii] = inv_mass.value
        arr[ii, ii-1] = inv_mass.value
    ret = ArrayData()
    ret.set_array("only_one", arr)
    return ret

@calcfunction
def prepare_potential(size, spring):
    arr = np.eye(size.value)
    for ii in range(size.value):
        arr[ii, ii] *= 0.5*spring.value*(ii - (size.value-1)/2)**2
    ret = ArrayData()
    ret.set_array("only_one", arr)
    return ret

@calcfunction
def add_operators(x, y):
    xa = x.get_array("only_one")
    ya = y.get_array("only_one")
    za = xa + ya
    ret = ArrayData()
    ret.set_array("only_one", za)
    return ret

@calcfunction
def plot_eigen(E):
    from matplotlib import pyplot as plt
    from io import BytesIO

    buffer = BytesIO()

    plt.plot(E)
    plt.savefig(buffer)
    buffer.seek(0)

    return SinglefileData(buffer)

@pytest.mark.filterwarnings("ignore:Creating AiiDA")
def test_diagonalize_hamiltonian(aiida_local_code_factory, clear_database):
    from aiida.plugins import CalculationFactory
    from aiida.engine import run
    import numpy as np

    executable = 'python3'
    entry_point = 'test.calc_diag'

    code = aiida_local_code_factory(entry_point=entry_point, executable=executable)
    calculation = CalculationFactory(entry_point)

    T = prepare_kinetic(Int(30),Float(1.8))
    U = prepare_potential(Int(30),Float(0.1))

    H = add_operators(T, U)

    inputs = { 'code': code,
               'inputarray': H,
               'repeats': Int(220)}

    result = run(calculation, **inputs)

    print(abs(result["value"].value))
    assert abs(result["value"].value) < 3
