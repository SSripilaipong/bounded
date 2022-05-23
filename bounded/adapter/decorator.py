from typing import Type

from bounded.exception import AnnotationMissing


def Adapter(cls: Type):
    raise AnnotationMissing()
