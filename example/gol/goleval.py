import numpy as np
from aiida.orm import Int
from aiida.plugins import ( CalculationFactory,
                            DataFactory,
                          )

CalcJobPython = CalculationFactory("aiida_python.calc")
GolSystem = DataFactory("aiida_python.gol.system")

class GOLEval(CalcJobPython):

    @classmethod
    def define(cls, spec):
        super().define(spec)

        spec.input('input_system', valid_type=GolSystem)
        spec.input('steps', valid_type=Int)
        spec.output('output_system', valid_type=GolSystem)

        spec.inputs['metadata']['options']['serializers'].default = ["int", "aiida_python.gol.system"]


    def run_python(self):

        import numpy as np

        def _do_step(array):
            # Create a copy of the array to store the next state
            next_array = np.zeros_like(array)

            # Determine the number of rows and columns in the array
            num_rows, num_cols = array.shape

            # Loop over each cell in the array and determine its next state
            for i in range(num_rows):
                for j in range(num_cols):
                    # Count the number of live neighbors for the current cell
                    num_neighbors = np.sum(array[max(0, i-1):min(i+2, num_rows), max(0, j-1):min(j+2, num_cols)]) - array[i, j]

                    # Apply the rules of the Game of Life to determine the next state of the cell
                    if array[i, j]:
                        next_array[i, j] = num_neighbors == 2 or num_neighbors == 3
                    else:
                        next_array[i, j] = num_neighbors == 3

            # Return the next state of the array
            return next_array

        array = self.inputs.input_system
        for ii in range(self.inputs.steps):
            array = _do_step(np.array(array))
        self.outputs.output_system = np.array(array)

