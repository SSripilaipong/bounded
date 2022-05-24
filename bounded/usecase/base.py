import inspect
from inspect import Signature
from typing import Tuple, Dict, Any

from bounded.exception import AnnotationError


class UsecaseMeta(type):
    def __new__(cls, name: str, bases: Tuple[type, ...], dct: Dict[str, Any]):
        result = super().__new__(cls, name, bases, dct)

        methods = inspect.getmembers(result, predicate=inspect.isfunction)
        for method_name, method in methods:
            signature = inspect.signature(method)

            _validate_method(method_name, signature)

        return result


def _validate_method(name: str, signature: Signature):
    if signature.return_annotation is _EMPTY:
        raise AnnotationError(_ERROR_METHOD_NO_RETURN_TYPE.format(method=name))
    if not isinstance(signature.return_annotation, type):
        raise AnnotationError(_ERROR_METHOD_RETURN_TYPE_MUST_BE_A_TYPE)


_EMPTY = Signature.empty
_ERROR_METHOD_NO_RETURN_TYPE = "Usecase's public method '{method}()' must have return type"
_ERROR_METHOD_RETURN_TYPE_MUST_BE_A_TYPE = "Return type of 'my_method()' must be a type"


class Usecase(metaclass=UsecaseMeta):
    pass
