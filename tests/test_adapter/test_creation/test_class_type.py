from pytest import raises

from bounded import Adapter


def test_should_raise_TypeError_when_applying_Adapter_to_non_ABC():
    with raises(TypeError) as ex:

        @Adapter
        class MyAdapter:
            pass

    assert str(ex.value) == "@Adapter only applies to abstract classes (inherited from ABC)"
