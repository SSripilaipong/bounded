import inspect
from inspect import Signature
from typing import Type, Tuple

from bounded.exception import ImplementationError, AnnotationError


_EMPTY = Signature.empty


def validate_implementation(name: str, bases: Tuple[type, ...], cls: Type):
    base = _validate_base(bases)
    _validate_no_abstract_method_left(cls, name)
    _validate_implemented_method_signature(base, cls)


def _validate_base(bases):
    if len(bases) != 1:
        raise ImplementationError(_ERROR_IMPLEMENT_MULTIPLE_ADAPTERS)
    base = bases[0]
    return base


def _validate_implemented_method_signature(base: Type, cls: Type):
    required_abstract_method_names = inspect.getmembers(base, predicate=_is_abstract_method)
    for method_name, method in required_abstract_method_names:
        abstract = inspect.signature(method)
        implementation = inspect.signature(getattr(cls, method_name))
        if implementation.return_annotation is _EMPTY:
            raise AnnotationError(_ERROR_IMPLEMENTED_METHOD_WITH_DIFFERENT_RETURN_TYPE.format(method=method_name))
        if implementation.return_annotation is not abstract.return_annotation:
            raise AnnotationError(_ERROR_IMPLEMENTED_METHOD_WITH_DIFFERENT_RETURN_TYPE.format(method=method_name))


def _validate_no_abstract_method_left(cls: Type, class_name: str):
    abstract_methods = inspect.getmembers(cls, predicate=_is_abstract_method)
    for method_name, method in abstract_methods:
        msg = _ERROR_NOT_IMPLEMENT_ABSTRACT_METHOD.format(cls=class_name, method=method_name)
        raise ImplementationError(msg)


def _is_abstract_method(x) -> bool:
    return inspect.isfunction(x) and getattr(x, "__isabstractmethod__", False)


_ERROR_NOT_IMPLEMENT_ABSTRACT_METHOD = "Adapter's implementation '{cls}' must implement abstract method " \
                                       "'{method}()'"
_ERROR_IMPLEMENTED_METHOD_WITH_DIFFERENT_RETURN_TYPE = "Implemented method '{method}()' must have same return type " \
                                                "as the abstract adapter"
_ERROR_IMPLEMENT_MULTIPLE_ADAPTERS = "Cannot implement multiple adapters in the same class"
