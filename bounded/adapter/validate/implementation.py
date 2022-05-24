import inspect
from typing import Type

from bounded.exception import ImplementationError


def validate_implementation(name: str, cls: Type):
    abstract_methods = inspect.getmembers(cls, predicate=_is_abstract_method)
    for method_name, method in abstract_methods:
        msg = _ERROR_IMPLEMENTATION_MISSING_ABSTRACT_CLASS.format(cls=name, method=method_name)
        raise ImplementationError(msg)


def _is_abstract_method(x) -> bool:
    return inspect.isfunction(x) and getattr(x, "__isabstractmethod__", False)


_ERROR_IMPLEMENTATION_MISSING_ABSTRACT_CLASS = "Adapter's implementation '{cls}' must implement abstract method " \
                                               "'{method}()'"
