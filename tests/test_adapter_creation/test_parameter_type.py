from abc import ABC, abstractmethod

from pytest import raises

from bounded import Adapter
from bounded.exception import AnnotationError


def test_should_raise_AnnotationError_when_abstract_method_my_method_has_parameter_a_without_type_annotation():
    with raises(AnnotationError) as ex:

        @Adapter
        class MyAdapter(ABC):

            @abstractmethod
            def my_method(self, a) -> int:
                pass

    assert str(ex.value) == "Parameter 'a' in method 'my_method()' must be annotated"


def test_should_raise_AnnotationError_when_abstract_method_another_method_has_parameter_b_without_type_annotation():
    with raises(AnnotationError) as ex:

        @Adapter
        class MyAdapter(ABC):

            @abstractmethod
            def another_method(self, b) -> int:
                pass

    assert str(ex.value) == "Parameter 'b' in method 'another_method()' must be annotated"


def test_should_raise_AnnotationError_when_abstract_method_parameter_a_of_my_method_with_annotation_that_is_not_a_type():
    with raises(AnnotationError) as ex:

        @Adapter
        class MyAdapter(ABC):

            @abstractmethod
            def my_method(self, a: 1234) -> int:
                pass

    assert str(ex.value) == "The annotation of parameter 'a' in method 'my_method()' must be a type"


def test_should_raise_AnnotationError_when_abstract_method_parameter_b_of_anothor_method_with_annotation_that_is_not_a_type():
    with raises(AnnotationError) as ex:

        @Adapter
        class MyAdapter(ABC):

            @abstractmethod
            def another_method(self, b: 1234) -> int:
                pass

    assert str(ex.value) == "The annotation of parameter 'b' in method 'another_method()' must be a type"
