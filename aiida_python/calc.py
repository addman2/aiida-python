# -*- coding: utf-8 -*-

from aiida.common import datastructures
from aiida.engine import CalcJob
from aiida.orm import (Data, Int, Float, Str)

INFILE = '.__data_mia.inpkl'
OUTFILE = '.__data_mia.outpkl'
ERRFILE = '.__data_mia.errpkl'


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

        spec.input('metadata.options.serializers',
                   valid_type=list,
                   required=False,
                   help='Dont leave this empty')

        spec.inputs['metadata']['options'][
            'parser_name'].default = 'aiida-python.parser'
        spec.inputs['metadata']['options'][
            'input_filename'].default = '__noone_will_ever_use_this_name.input'
        spec.inputs['metadata']['options'][
            'output_filename'].default = '__noone_will_ever_use_this_name.output'

        spec.inputs['metadata']['options']['serializers'].default = [
            'int',
            'float',
            'str',
            'list',
            'arraydata',
        ]
        spec.output('run_code', valid_type=Str, help='Code that had been run')

        spec.output('error_message',
                    valid_type=Str,
                    help='Error message if exception was raised')

        spec.exit_code(
            300,
            'ERROR_MISSING_OUTPUT_VARIABLES',
            message='Calculation did not produce all expected output files.')

    def serialize(self, fhandle):
        """
        """

        from aiida.plugins import entry_point as ep

        def serialize_this(obj):
            for entry_point in ep.eps().select(
                    group='aiida_python.serializers'):
                if entry_point.name in self.inputs['metadata']['options'][
                        'serializers']:
                    obj = entry_point.load().serialize(obj)
            return obj

        """
        o linja mute mute ...
        """
        data = {
            inp: serialize_this(self.inputs[inp])
            for inp in self.inputs if inp not in ('metadata', 'code')
        }
        """
        fixme: Make a warning if something was not serialized
        """
        data = {
            key: val
            for key, val in data.items() if not isinstance(val, Data)
        }

        import pickle
        pickle.dump(data, fhandle)

    def prepare_for_submission(self, folder):

        run_python = getattr(self, 'run_python', None)
        if not callable(run_python):
            # None type is not callable, right?
            raise NoRunPythonMethod()

        self.helper = {}
        docs = run_python.__doc__
        self._process_docs(folder, docs)
        import inspect
        source_code, _ = inspect.getsourcelines(run_python)
        """
        Unindent the source code

        TODO: Do it properly

        There is indent of the code the 'if True:'
        statement fixes unexpected indent.
        """

        #source_code = [ l[4:-1] for l in source_code ]
        source_code = [
            'import os', 'os.system("mkdir ihyh")',
            'os.system("echo \'from .ihyh import IHideYouHolder\' > ihyh/__init__.py")',
            'os.system("cp ihyh.py ihyh")', 'from ihyh import IHideYouHolder',
            'if True:'
        ] + source_code

        arguments = f'infile="{INFILE}", outfile="{OUTFILE}"'
        runline = f'run_python(IHideYouHolder({arguments}))'
        trailing_code = [
            'try:', f'    {runline}', 'except Exception as exc:',
            f'    with open("{ERRFILE}", "w") as fhandle:',
            '        fhandle.write(str(exc))'
        ]
        #source_code.append(f'try:\n    run_python(IHideYouHolder({arguments}))\nexcept:\n    os.system("echo ijo ike > {ERRFILE}")')
        source_code = '\n'.join(source_code + trailing_code)

        import os
        from pathlib import Path

        directory = Path(__file__).resolve().parent
        ihyh_file = Path(directory) / 'data' / 'ihyh.py'

        with folder.open('ihyh.py', 'w') as fhandle_destination, \
             open(ihyh_file, 'r') as fhandle_source:
            fhandle_destination.write(fhandle_source.read())

        with folder.open(self.inputs.metadata.options.input_filename,
                         'w') as fhandle:
            fhandle.write(source_code)

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

        calcinfo.retrieve_list = [
            self.inputs.metadata.options.output_filename,
            self.inputs.metadata.options.input_filename,
            OUTFILE,
            ERRFILE,
        ]
        if 'retrieve_list' in self.helper:
            calcinfo.retrieve_list.extend(self.helper['retrieve_list'])

        return calcinfo

    def _process_docs(self, folder, docs):

        if not docs: return

        import re
        import os

        for line in docs.split('\n'):
            m = re.match(r'.*!file\s+(.+):\s*([_a-zA-Z0-9]+)\s*$', line)
            if m:
                self._op_file_in(folder, m.group(1), m.group(2))
                self._op_file_out(folder, m.group(2))

    def _op_file_out(self, folder, filename):
        if 'retrieve_list' not in self.helper:
            self.helper['retrieve_list'] = []
        self.helper['retrieve_list'].append(filename)

    def _op_file_in(self, folder, inputname, filename):
        try:
            with folder.open(filename, 'wb') as fhandle_destination, \
                 getattr(self.inputs, inputname).open(mode='rb') as fhandle_source:
                fhandle_destination.write(fhandle_source.read())
        except AttributeError:
            """
            If input port does not exists do nothing
            """
            pass
