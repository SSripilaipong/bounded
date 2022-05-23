import inspect
from abc import ABC
from inspect import Signature, Parameter
from types import FunctionType
from typing import Type, Iterable, Tuple

from bounded.exception import AnnotationError


_EMPTY = Signature.empty


def Adapter(cls: Type):
    if not issubclass(cls, ABC):
        raise TypeError(_ERROR_ABC_ONLY)

    attrs = ((name, getattr(cls, name)) for name in dir(cls))
    methods: Iterable[Tuple[str, FunctionType]] = filter(lambda attr: callable(attr[1]), attrs)

    for name, method in methods:
        _validate_method(name, method)


def _validate_method(name: str, method: FunctionType):
    if _is_abstract_method(method):
        _validate_abstract_method(name, method)


def _validate_abstract_method(name: str, method: FunctionType):
    signature = inspect.signature(method)

    _validate_abstract_method_return_type(name, signature)
    _validate_abstract_method_parameter_type(name, signature)


def _validate_abstract_method_parameter_type(method_name: str, signature: Signature):
    parameters = list(signature.parameters.items())
    for name, param in parameters[1:]:
        _validate_abstract_method_parameter(method_name, param)


def _validate_abstract_method_parameter(method_name: str, param: Parameter):
    annotation = param.annotation
    if annotation is _EMPTY:
        raise AnnotationError(_ERROR_PARAM_NO_ANNOTATION.format(param=param.name, method=method_name))
    if not isinstance(annotation, type):
        raise AnnotationError(_ERROR_PARAM_ANNOTATION_NOT_TYPE.format(param=param.name, method=method_name))


def _validate_abstract_method_return_type(method_name: str, signature: Signature):
    return_annotation = signature.return_annotation
    if return_annotation is _EMPTY:
        raise AnnotationError(_ERROR_NO_RETURN_ANNOTATION.format(method=method_name))
    if not isinstance(return_annotation, type):
        raise AnnotationError()


def _is_abstract_method(method: FunctionType) -> bool:
    return getattr(method, "__isabstractmethod__", False)


_ERROR_ABC_ONLY = "@Adapter only applies to abstract classes (inherited from ABC)"
_ERROR_PARAM_ANNOTATION_NOT_TYPE = "The annotation of parameter '{param}' in method '{method}()' must be a type"
_ERROR_PARAM_NO_ANNOTATION = "Parameter '{param}' in method '{method}()' must be annotated"
_ERROR_NO_RETURN_ANNOTATION = "Abstract method '{method}()' must have return type annotation"
