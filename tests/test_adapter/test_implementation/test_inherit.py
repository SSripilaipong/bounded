from abc import abstractmethod
from pytest import raises

from bounded import Adapter
from bounded.exception import ImplementationError


def test_should_inherit_from_abstract_adapter():
    class AbstractAdapter(Adapter):
        pass

    class ImplementationAdapter(AbstractAdapter):
        pass


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
