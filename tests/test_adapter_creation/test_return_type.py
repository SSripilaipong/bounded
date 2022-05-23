from abc import ABC, abstractmethod

from pytest import raises

from bounded import Adapter
from bounded.exception import AnnotationMissing


def test_should_raise_AnnotationMissing_when_creating_adapter_abstract_method_without_return_type():
    with raises(AnnotationMissing):

        @Adapter
        class MyAdapter(ABC):

            @abstractmethod
            def my_method_without_return_type(self):
                pass
