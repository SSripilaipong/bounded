import inspect
from inspect import Signature
from typing import Type, Tuple

from bounded.exception import ImplementationError, AnnotationError


_EMPTY = Signature.empty


def validate_implementation(name: str, bases: Tuple[type, ...], cls: Type):
    base = bases[0]
    _validate_no_abstract_method_left(cls, name)
    _validate_implemented_method_signature(base, cls)


def _validate_implemented_method_signature(base, cls):
    required_abstract_method_names = inspect.getmembers(base, predicate=_is_abstract_method)
    for name, method in required_abstract_method_names:
        signature = inspect.signature(getattr(cls, name))
        if signature.return_annotation is _EMPTY:
            raise AnnotationError(_ERROR_IMPLEMENTED_METHOD_MISSING_RETURN_TYPE)


def _validate_no_abstract_method_left(cls, name):
    abstract_methods = inspect.getmembers(cls, predicate=_is_abstract_method)
    for method_name, method in abstract_methods:
        msg = _ERROR_NOT_IMPLEMENT_ABSTRACT_METHOD.format(cls=name, method=method_name)
        raise ImplementationError(msg)


def _is_abstract_method(x) -> bool:
    return inspect.isfunction(x) and getattr(x, "__isabstractmethod__", False)


_ERROR_NOT_IMPLEMENT_ABSTRACT_METHOD = "Adapter's implementation '{cls}' must implement abstract method " \
                                       "'{method}()'"
_ERROR_IMPLEMENTED_METHOD_MISSING_RETURN_TYPE = "Implemented method 'my_method()' must have same return type " \
                                                "as the abstract adapter"
