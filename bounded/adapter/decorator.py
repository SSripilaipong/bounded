from types import FunctionType
from typing import Type, Iterable

from bounded.exception import AnnotationMissing


def Adapter(cls: Type):
    attrs = (getattr(cls, name) for name in dir(cls))
    methods: Iterable[FunctionType] = filter(callable, attrs)

    for method in methods:
        _validate_abstract_method(method)


def _validate_abstract_method(method: FunctionType):
    if _is_abstract_method(method):
        if not method.__annotations__:
            raise AnnotationMissing()


def _is_abstract_method(method: FunctionType) -> bool:
    return getattr(method, "__isabstractmethod__", False)
