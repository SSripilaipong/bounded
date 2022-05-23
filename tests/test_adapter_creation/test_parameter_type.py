from abc import ABC, abstractmethod

from pytest import raises

from bounded import Adapter
from bounded.exception import AnnotationError


def test_should_raise_AnnotationError_when_abstract_method_has_parameter_without_type_annotation():
    with raises(AnnotationError):

        @Adapter
        class MyAdapter(ABC):

            @abstractmethod
            def my_method(self, a) -> int:
                pass
