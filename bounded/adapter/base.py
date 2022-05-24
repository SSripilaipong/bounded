from abc import ABCMeta
from typing import Tuple, Dict, Any

from bounded.adapter.validate import validate_adapter
from bounded.adapter.validate.implementation import validate_implementation


class AdapterMeta(ABCMeta):
    def __new__(cls, name: str, bases: Tuple[type, ...], dct: Dict[str, Any]):
        result = super().__new__(cls, name, bases, dct)

        is_implementation = _is_implementation(bases)
        is_adapter = not _is_adapter_base_itself(name) and not is_implementation

        if is_adapter:
            validate_adapter(result)
        elif is_implementation:
            validate_implementation(name, bases, result)
        return result


def _is_implementation(bases):
    return bases and Adapter not in bases


def _is_adapter_base_itself(name: str) -> bool:
    try:
        has_adapter_base = bool(Adapter)
    except NameError:
        has_adapter_base = False
    return not has_adapter_base and name == "AdapterBase"


class Adapter(metaclass=AdapterMeta):
    pass
