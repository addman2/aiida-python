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

def setup_gol(func):
    """Add entry point to the entry_points fixture"""

    # Get full path of this file using pathlib
    file_path = pathlib.Path(__file__).parent.parent.absolute() / 'serializer.py'
    SerializerGOLSystem = load_class_from_file(file_path, 'SerializerGOLSystem')

    module_name  = sys.modules[__name__].__name__

    @functools.wraps(func)
    def wrapper(entry_points, *args, **kwargs):
        sys.modules[__name__].SerializerGOLSystem = SerializerGOLSystem
        entry_points.add(group='aiida_python.serializers',
                         name='aiida_python.gol.system',
                         value=f"{module_name}:SerializerGOLSystem"   )
        ret = func(*args, entry_points = entry_points, **kwargs)

        # Clean up
        del sys.modules[__name__].SerializerGOLSystem
        return ret

    return wrapper
