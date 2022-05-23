from abc import ABC, abstractmethod

from pytest import raises

from bounded import Adapter
from bounded.exception import AnnotationError


def test_should_not_raise_AnnotationError_on_normal_method():

    @Adapter
    class MyAdapter(ABC):

        def not_abstract(self, p) -> int:
            pass


def test_should_raise_AnnotationError_when_creating_adapter_abstract_method_my_method_without_return_type():
    with raises(AnnotationError) as ex:

        @Adapter
        class MyAdapter(ABC):

            @abstractmethod
            def my_method(self):
                pass

    assert str(ex.value) == "Abstract method 'my_method()' must have return type annotation"


def test_should_raise_AnnotationError_when_creating_adapter_abstract_method_another_method_without_return_type():
    with raises(AnnotationError) as ex:

        @Adapter
        class MyAdapter(ABC):

            @abstractmethod
            def another_method(self):
                pass

    assert str(ex.value) == "Abstract method 'another_method()' must have return type annotation"


def test_should_not_raise_error_when_creating_adapter_abstract_method_with_return_type_and_no_parameters():

    @Adapter
    class MyAdapter(ABC):

        @abstractmethod
        def my_method(self) -> int:
            pass


def test_should_raise_AnnotationError_when_creating_adapter_abstract_method_my_method_with_return_type_that_is_not_type():
    with raises(AnnotationError) as ex:

        @Adapter
        class MyAdapter(ABC):

            @abstractmethod
            def my_method(self) -> 123:
                pass

    assert str(ex.value) == "The return type of 'my_method()' must be a type"
