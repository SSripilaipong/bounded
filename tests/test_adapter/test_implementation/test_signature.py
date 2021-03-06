from abc import abstractmethod

from pytest import raises

from bounded import Adapter
from bounded.exception import ImplementationError, AnnotationError


def test_should_raise_ImplementationError_when_abstract_method_my_method_is_missing_from_MyImpl():
    class AbstractAdapter(Adapter):
        @abstractmethod
        def my_method(self) -> int:
            pass

    with raises(ImplementationError) as ex:

        class MyImpl(AbstractAdapter):
            pass

    assert str(ex.value) == "Adapter's implementation 'MyImpl' must implement abstract method 'my_method()'"


def test_should_raise_ImplementationError_when_abstract_method_another_method_is_missing_from_AnotherImpl():
    class AbstractAdapter(Adapter):
        @abstractmethod
        def another_method(self) -> int:
            pass

    with raises(ImplementationError) as ex:

        class AnotherImpl(AbstractAdapter):
            pass

    assert str(ex.value) == "Adapter's implementation 'AnotherImpl' must implement abstract method 'another_method()'"


def test_should_raise_AnnotationError_when_implemented_method_my_method_has_no_return_type():

    class AbstractAdapter(Adapter):
        @abstractmethod
        def my_method(self) -> int:
            pass

    with raises(AnnotationError) as ex:

        class MyImpl(AbstractAdapter):
            def my_method(self):
                pass

    assert str(ex.value) == "Implemented method 'my_method()' must have same return type as the abstract adapter"


def test_should_raise_AnnotationError_when_implemented_method_another_method_has_no_return_type():

    class AbstractAdapter(Adapter):
        @abstractmethod
        def another_method(self) -> int:
            pass

    with raises(AnnotationError) as ex:

        class MyImpl(AbstractAdapter):
            def another_method(self):
                pass

    assert str(ex.value) == "Implemented method 'another_method()' must have same return type as the abstract adapter"


def test_should_raise_AnnotationError_when_implemented_method_my_method_with_different_return_type():

    class AbstractAdapter(Adapter):
        @abstractmethod
        def my_method(self) -> int:
            pass

    with raises(AnnotationError) as ex:

        class MyImpl(AbstractAdapter):
            def my_method(self) -> str:
                pass

    assert str(ex.value) == "Implemented method 'my_method()' must have same return type as the abstract adapter"


def test_should_raise_ImplementationError_when_implemented_method_my_method_has_different_parameter_set():

    class AbstractAdapter(Adapter):
        @abstractmethod
        def my_method(self, a: int, b: str = "") -> str:
            pass

    with raises(ImplementationError) as ex:

        class MyImpl(AbstractAdapter):
            def my_method(self, x: int, y, z: str = "", a="") -> str:
                pass

    assert str(ex.value) == "Implemented method 'my_method()' must have same parameters as the abstract adapter"


def test_should_raise_ImplementationError_when_implemented_method_another_method_has_different_parameter_set():

    class AbstractAdapter(Adapter):
        @abstractmethod
        def another_method(self, a: int, b: str = "") -> str:
            pass

    with raises(ImplementationError) as ex:

        class MyImpl(AbstractAdapter):
            def another_method(self, x: int, y, z: str = "", a="") -> str:
                pass

    assert str(ex.value) == "Implemented method 'another_method()' must have same parameters as the abstract adapter"
