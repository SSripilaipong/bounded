from pytest import raises

from bounded import Usecase
from bounded.exception import AnnotationError


def test_should_raise_AnnotationError_when_define_method_my_method_without_return_type():
    with raises(AnnotationError) as ex:

        class MyUsecase(Usecase):
            def my_method(self):
                pass

    assert str(ex.value) == "Usecase's public method 'my_method()' must have return type"


def test_should_raise_AnnotationError_when_define_method_another_method_without_return_type():
    with raises(AnnotationError) as ex:

        class MyUsecase(Usecase):
            def another_method(self):
                pass

    assert str(ex.value) == "Usecase's public method 'another_method()' must have return type"


def test_should_raise_AnnotationError_when_define_method_my_method_with_return_type_that_is_not_a_type():
    with raises(AnnotationError) as ex:

        class MyUsecase(Usecase):
            def my_method(self) -> 123:
                pass

    assert str(ex.value) == "Return type of 'my_method()' must be a type"


def test_should_raise_AnnotationError_when_define_method_another_method_with_return_type_that_is_not_a_type():
    with raises(AnnotationError) as ex:

        class MyUsecase(Usecase):
            def another_method(self) -> 123:
                pass

    assert str(ex.value) == "Return type of 'another_method()' must be a type"
