from pytest import raises

from bounded.exception import AnnotationError
from bounded.usecase.base import Usecase


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
