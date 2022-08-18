# -*- coding: utf-8 -*-

from aiida.common import datastructures
from aiida.engine import CalcJob
from aiida.orm import (Int,
                       Float,
                       Str)

INFILE = ".__data_mia.inpkl"
OUTFILE = ".__data_mia.outpkl"

class NoRunPythonMethod(Exception):
    pass

class CalcJobPython(CalcJob):
    """
    AiiDA Python calculation class
    """

    @classmethod
    def define(cls, spec):
        super().define(spec)

        spec.inputs['metadata']['options']['resources'].default = {
            'num_machines': 1,
            'num_mpiprocs_per_machine': 1,
        }

        spec.inputs['metadata']['options']['parser_name'].default = 'aiida_python.parser'
        spec.inputs['metadata']['options']['input_filename'].default = '__noone_will_ever_use_this_name.input'
        spec.inputs['metadata']['options']['output_filename'].default = '__noone_will_ever_use_this_name.output'

        from aiida_python import serializers
        cls.serializers = map( lambda x: getattr(serializers, x),
                               [ "SerializerInt",
                                 "SerializerFloat",
                                 "SerializerStr" ] )

    def serialize(self, fhandle):
        """
        """

        def serialize_this(obj):
            for s in self.serializers:
                obj = s(obj)
            return obj

        """
        o linja mute mute ...
        """
        data = { inp: serialize_this(self.inputs[inp]) for inp in self.inputs if inp not in ('metadata', 'code') }
        import pickle
        pickle.dump(data, fhandle)

    def prepare_for_submission(self, folder):

        run_python = getattr(self, "run_python", None)
        if not callable(run_python):
            # None type is not callable, right?
            raise NoRunPythonMethod()

        import inspect
        source_code, _ = inspect.getsourcelines(run_python)
        """
        Unindent the source code
        
        TODO: Do it properly
        """
        source_code = [ l[4:-1] for l in source_code ]
        source_code = ['import os',
                       'os.system("mkdir ihyh")',
                       'os.system("echo \'from .ihyh import IHideYouHolder\' > ihyh/__init__.py")',
                       'os.system("cp ihyh.py ihyh")',
                       'from ihyh import IHideYouHolder'] + source_code

        arguments = f'infile="{INFILE}", outfile="{OUTFILE}"'
        source_code.append(f'run_python(IHideYouHolder({arguments}))')
        source_code = '\n'.join(source_code)

        import os
        from pathlib import Path

        directory = Path(__file__).resolve().parent
        ihyh_file = Path(directory) / 'data' / 'ihyh.py'

        with folder.open('ihyh.py', 'w') as fhandle_destination, \
             open(ihyh_file, 'r') as fhandle_source:
            fhandle_destination.write(fhandle_source.read())

        with folder.open(self.inputs.metadata.options.input_filename, "w") as fhandle:
            fhandle.write(source_code)

        data = {}
        for inp in self.inputs:
            if inp in ('metadata', 'code'): continue
            data[inp] = self.inputs[inp].value

        with folder.open(INFILE, 'wb') as fhandle:
            self.serialize(fhandle)

        codeinfo = datastructures.CodeInfo()
        codeinfo.code_uuid = self.inputs.code.uuid
        codeinfo.cmdline_params = []
        codeinfo.stdin_name = self.inputs.metadata.options.input_filename
        codeinfo.stdout_name = self.inputs.metadata.options.output_filename

        calcinfo = datastructures.CalcInfo()
        calcinfo.codes_info = [codeinfo]
        calcinfo.local_copy_list = []

        calcinfo.retrieve_list = [self.inputs.metadata.options.output_filename,
                                  OUTFILE]

        return calcinfo
