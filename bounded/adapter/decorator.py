from typing import Type

from bounded.exception import AnnotationMissing


def Adapter(cls: Type):
    attrs = (getattr(cls, name) for name in dir(cls))
    methods = filter(callable, attrs)
    for method in methods:
        if getattr(method, "__isabstractmethod__", False):
            raise AnnotationMissing()
