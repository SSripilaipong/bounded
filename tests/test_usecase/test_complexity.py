from pytest import raises

from bounded import Usecase
from bounded.exception import ComplexityError


def test_should_raise_ComplexityError_when_method_my_method_have_optional_parameters():
    with raises(ComplexityError) as ex:

        class MyUsecase(Usecase):
            def my_method(self, a: str = None) -> int:
                pass

    assert str(ex.value) == "Usecase's method 'my_method()' should have no optional parameters"


def test_should_raise_ComplexityError_when_method_another_method_have_optional_parameters():
    with raises(ComplexityError) as ex:

        class MyUsecase(Usecase):
            def another_method(self, a: str = None) -> int:
                pass

    assert str(ex.value) == "Usecase's method 'another_method()' should have no optional parameters"
