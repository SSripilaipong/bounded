import inspect
from inspect import Signature, Parameter
from typing import Tuple, Dict, Any, List

from bounded.exception import AnnotationError, ComplexityError


class UsecaseMeta(type):
    def __new__(cls, name: str, bases: Tuple[type, ...], dct: Dict[str, Any]):
        result = super().__new__(cls, name, bases, dct)

        methods = inspect.getmembers(result, predicate=inspect.isfunction)
        for method_name, method in methods:
            signature = inspect.signature(method)

            _validate_method(method_name, signature)

        return result


def _validate_method(name: str, signature: Signature):
    _validate_method_return_type(name, signature)
    _validate_method_parameter_type(name, signature)


def _validate_method_parameter_type(method_name: str, signature: Signature):
    params: List[Tuple[str, Parameter]] = list(signature.parameters.items())[1:]
    for name, param in params:
        if param.annotation is _EMPTY:
            raise AnnotationError(_ERROR_METHOD_PARAMETER_MUST_BE_ANNOTATED.format(method=method_name))
        if not isinstance(param.annotation, type):
            raise AnnotationError(_ERROR_METHOD_PARAMETER_ANNOTATION_MUST_BE_A_TYPE.format(method=method_name))
        if param.default is not _EMPTY:
            raise ComplexityError(_ERROR_METHOD_PARAMETER_SHOULD_NOT_BE_OPTIONAL.format(method=method_name))


def _validate_method_return_type(name: str, signature: Signature):
    if signature.return_annotation is _EMPTY:
        raise AnnotationError(_ERROR_METHOD_NO_RETURN_TYPE.format(method=name))
    if not isinstance(signature.return_annotation, type):
        raise AnnotationError(_ERROR_METHOD_RETURN_TYPE_MUST_BE_A_TYPE.format(method=name))


_EMPTY = Signature.empty
_ERROR_METHOD_NO_RETURN_TYPE = "Usecase's public method '{method}()' must have return type"
_ERROR_METHOD_RETURN_TYPE_MUST_BE_A_TYPE = "Return type of '{method}()' must be a type"
_ERROR_METHOD_PARAMETER_MUST_BE_ANNOTATED = "Usecase's public method '{method}()' must have all parameters annotated"
_ERROR_METHOD_PARAMETER_ANNOTATION_MUST_BE_A_TYPE = "Parameters of usecase's public method '{method}()' " \
                                                    "must be annotated with types"
_ERROR_METHOD_PARAMETER_SHOULD_NOT_BE_OPTIONAL = "Usecase's method '{method}()' should have no optional parameters"


class Usecase(metaclass=UsecaseMeta):
    pass
