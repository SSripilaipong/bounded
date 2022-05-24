from pytest import raises

from bounded import Adapter
from bounded.exception import ImplementationError


def test_should_inherit_from_abstract_adapter():
    class AbstractAdapter(Adapter):
        pass

    class ImplementationAdapter(AbstractAdapter):
        pass


def test_should_raise_ImplementationError_when_implementing_multiple_adapters():

    class AdapterA(Adapter):
        pass

    class AdapterB(Adapter):
        pass

    with raises(ImplementationError) as ex:

        class Impl(AdapterA, AdapterB):
            pass

    assert str(ex.value) == "Cannot implement multiple adapters in the same class"
