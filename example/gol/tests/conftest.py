# -*- coding: utf-8 -*-
import sys
import pytest
import importlib
import pathlib
import functools

# This is the dummy version of the plugin
__version__ = '0.0.0'


def load_class_from_file(file_path, class_name):
    """Load class from file"""

    spec = importlib.util.spec_from_file_location(class_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    class_obj = getattr(module, class_name)
    return class_obj


def try_to_load(class_name):
    # Get full path of this file using pathlib
    for file in pathlib.Path(__file__).parent.parent.absolute().glob(
            '**/*.py'):
        try:
            obj = load_class_from_file(file, class_name)
            obj.__version__ = '0.0.0'
            return obj
        except AttributeError:
            pass
    raise AttributeError(f'Could not find class {class_name}')


def setup_gol(func):
    """
        This is a decorator that adds the entry point to the entry_points fixture

        It also adds the class to the current module so that it can be imported,
        and then removes it after the test is run. Why this module? Because it
        it has to stored somewhere, and this is the only module that is guaranteed
        to be loaded before the entry_points fixture is run.

        """

    module_name = sys.modules[__name__].__name__

    entry_data = [
        (
            'aiida_python.serializers',
            'aiida_python.gol.system',
            'SerializerGOLSystem',
        ),
        (
            'aiida.data',
            'aiida-python.gol.system',
            'GOLSystem',
        ),
        (
            'aiida.calculations',
            'aiida-python.example.goleval',
            'GOLEval',
        ),
    ]

    @functools.wraps(func)
    def wrapper(entry_points, *args, **kwargs):
        for group, name, object_name in entry_data:
            obj = try_to_load(object_name)
            obj.__module__ = __name__
            setattr(sys.modules[__name__], object_name, obj)
            entry_points.add(group=group,
                             name=name,
                             value=f'{module_name}:{object_name}')

        ret = func(*args, entry_points=entry_points, **kwargs)

        # Clean up
        for group, name, object_name in entry_data:
            delattr(sys.modules[__name__], object_name)
        return ret

    return wrapper
