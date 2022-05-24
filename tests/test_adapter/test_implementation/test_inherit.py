from abc import ABC

from bounded import Adapter


def test_should_inherit_from_abstract_adapter():
    @Adapter
    class AbstractAdapter(ABC):
        pass

    class ImplementationAdapter(AbstractAdapter):
        pass
