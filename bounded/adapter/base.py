import inspect
from abc import ABCMeta
from typing import Tuple, Dict, Any

from bounded.exception import ImplementationError


class AdapterMeta(ABCMeta):
    def __new__(cls, name: str, bases: Tuple[type, ...], dct: Dict[str, Any]):
        result = super().__new__(cls, name, bases, dct)
        if bases and AdapterBase not in bases:
            abstract_methods = inspect.getmembers(result, predicate=_is_abstract_method)
            if abstract_methods:
                raise ImplementationError(_ERROR_IMPLEMENTATION_MISSING_ABSTRACT_CLASS)
        return result


class AdapterBase(metaclass=AdapterMeta):
    pass


def _is_abstract_method(x):
    return inspect.isfunction(x) and getattr(x, "__isabstractmethod__", False)


_ERROR_IMPLEMENTATION_MISSING_ABSTRACT_CLASS = "Adapter's implementation 'MyImpl' must implement abstract method " \
                                               "'my_method()'"
