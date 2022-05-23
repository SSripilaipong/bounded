from types import FunctionType
from typing import Type, Iterable

from bounded.exception import AnnotationError


def Adapter(cls: Type):
    attrs = (getattr(cls, name) for name in dir(cls))
    methods: Iterable[FunctionType] = filter(callable, attrs)

    for method in methods:
        _validate_abstract_method(method)


def _validate_abstract_method(method: FunctionType):
    if _is_abstract_method(method):
        return_annotation = method.__annotations__.get("return", None)
        if not return_annotation:
            raise AnnotationError()
        if not isinstance(return_annotation, type):
            raise AnnotationError()


def _is_abstract_method(method: FunctionType) -> bool:
    return getattr(method, "__isabstractmethod__", False)
