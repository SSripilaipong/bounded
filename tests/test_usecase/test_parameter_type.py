from pytest import raises

from bounded import Usecase
from bounded.exception import AnnotationError


def test_should_raise_AnnotationError_when_define_method_my_method_with_unannotated_parameter():
    with raises(AnnotationError) as ex:

        class MyUsecase(Usecase):
            def my_method(self, a) -> int:
                pass

    assert str(ex.value) == "Usecase's public method 'my_method()' must have all parameters annotated"


def test_should_raise_AnnotationError_when_define_method_another_method_with_unannotated_parameter():
    with raises(AnnotationError) as ex:

        class MyUsecase(Usecase):
            def another_method(self, a) -> int:
                pass

    assert str(ex.value) == "Usecase's public method 'another_method()' must have all parameters annotated"


def test_should_allow_creating_usecase_with_proper_method():
    class MyUsecase(Usecase):
        def my_method(self, a: str) -> int:
            pass


def test_should_raise_AnnotationError_when_define_method_my_method_with_parameter_annotation_that_is_not_a_type():
    with raises(AnnotationError) as ex:

        class MyUsecase(Usecase):
            def my_method(self, a: 1234) -> int:
                pass

    assert str(ex.value) == "Parameters of usecase's public method 'my_method()' must be annotated with types"


def test_should_raise_AnnotationError_when_define_method_another_method_with_parameter_annotation_that_is_not_a_type():
    with raises(AnnotationError) as ex:

        class MyUsecase(Usecase):
            def another_method(self, a: 1234) -> int:
                pass

    assert str(ex.value) == "Parameters of usecase's public method 'another_method()' must be annotated with types"
