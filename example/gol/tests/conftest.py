import sys
import pytest
import importlib
import pathlib
import functools

def load_class_from_file(file_path, class_name):
    """Load class from file"""

    spec = importlib.util.spec_from_file_location(class_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    class_obj = getattr(module, class_name)
    return class_obj

def try_to_load(class_name):
    # Get full path of this file using pathlib
    for file in pathlib.Path(__file__).parent.parent.absolute().glob('**/*.py'):
        try:
            obj = load_class_from_file(file, class_name)
            obj.__version__ = "0.0.0"
            return obj
        except AttributeError:
            pass
    return None

def setup_gol(func):
    """Add entry point to the entry_points fixture"""

    module_name  = sys.modules[__name__].__name__

    entry_data = [ ( "aiida_python.serializers",
                     "aiida_python.gol.system",
                     "SerializerGOLSystem",
                     ),
                   ( "aiida.data",
                     "aiida_python.gol.system",
                     "DataGOLSystem",
                     ),
                   ( "aiida.calculations",
                     "aiida_python.example.goleval",
                     "GOLEval",
                     ),
                 ]

    @functools.wraps(func)
    def wrapper(entry_points, *args, **kwargs):
        for group, name, object_name in entry_data:
            obj = try_to_load(object_name)
            setattr(sys.modules[__name__], object_name, obj)
            entry_points.add(group=group,
                             name=name,
                             value=f"{module_name}:{object_name}"   )

        ret = func(*args, entry_points = entry_points, **kwargs)

        # Clean up
        for group, name, object_name in entry_data:
            delattr(sys.modules[__name__], object_name)
        return ret

    return wrapper
