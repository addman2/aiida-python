Usage
=====

Installation
------------

To use ``aiida-python``, first install it using pip:

.. code-block:: console

   $ pip install aiida-python
   $ # directly from the source
   $ pip install <path-to-the-source>

Assuming you have AiiDA installed and configured, you can then use the
``verdi`` command to check if you see your plugin listed:

.. code-block:: console

   $ verdi plugin list aiida.calculations

   Registered entry points for aiida.calculations:
   * aiida-python.calc

If you need to run tests, you can install the package in editable mode, with testing dependencies:

.. code-block:: console

   $ pip install -e <path-to-the-source>[testing]


Example
-------

The following example shows how to create a plugin that uses the
``aiida_python`` plugin to run a python script. Here we are inverting a
matrix and mutliplying it with a random vector specified by the user
(variable ``repeats``). After each multiplication, the vector is normalised.
This way we can find the eigenvector of the matrix with the largest eigenvalue.
And therefore the smallest eigenvalue of the original matrix.

.. code-block:: python

    from aiida.orm import (Int, Float, Str, List, ArrayData)
    from aiida.plugins import CalculationFactory

    CalcJobPython = CalculationFactory("aiida_python.calc")

    class EigenValue(CalcJobPython):

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

More Examples
-------------

For more examples, see the ``example`` directory in the source code.
