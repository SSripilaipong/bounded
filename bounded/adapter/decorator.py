import inspect
from inspect import Signature
from types import FunctionType
from typing import Type, Iterable

from bounded.exception import AnnotationError


EMPTY = Signature.empty


def Adapter(cls: Type):
    attrs = (getattr(cls, name) for name in dir(cls))
    methods: Iterable[FunctionType] = filter(callable, attrs)

    for method in methods:
        _validate_method(method)


def _validate_method(method: FunctionType):
    if _is_abstract_method(method):
        _validate_abstract_method(method)


def _validate_abstract_method(method: FunctionType):
    signature = inspect.signature(method)

    _validate_abstract_method_return_type(signature)
    _validate_abstract_method_parameter_type(signature)


def _validate_abstract_method_parameter_type(signature: Signature):
    parameters = list(signature.parameters.items())
    for name, param in parameters[1:]:
        if param.annotation is EMPTY:
            raise AnnotationError()


def _validate_abstract_method_return_type(signature: Signature):
    return_annotation = signature.return_annotation
    if return_annotation is EMPTY:
        raise AnnotationError()
    if not isinstance(return_annotation, type):
        raise AnnotationError()


def _is_abstract_method(method: FunctionType) -> bool:
    return getattr(method, "__isabstractmethod__", False)
