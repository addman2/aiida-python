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

File Storing
------------

Very often one wants to use SinglefileData file and directly store the file in the working directory of the code. In ``aiida-python`` there is an easy shortcut to do it with doc strings:

.. code-block:: python

    class ClassThatCannotStartWithTestCopyFile(CalcJobPython):
        @classmethod
        def define(cls, spec):
            super().define(spec)

            spec.input('repeats', valid_type=Int)
            spec.input('inputfile', valid_type=SinglefileData)
            spec.output('value', valid_type=Float)
            spec.output('output', valid_type=SinglefileData)

        def run_python(self):
            """
            This is commentary

            This file will be stored in the working directory:
            !file inputfile: data

            Unset ports will be ignored:
            !file inputfile2: data2

            Store output
            !!file output: output
            """

            # Code comes here

Game of Life
------------

In ``examples/gol/`` there is a special implementaion of Play John Conway's Game of Life.

More Examples
-------------

For more examples, see the ``example`` directory in the source code.
