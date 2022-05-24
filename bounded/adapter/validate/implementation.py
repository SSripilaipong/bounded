import inspect

from bounded.exception import ImplementationError


def validate_implementation(result):
    abstract_methods = inspect.getmembers(result, predicate=_is_abstract_method)
    if abstract_methods:
        raise ImplementationError(_ERROR_IMPLEMENTATION_MISSING_ABSTRACT_CLASS)


_ERROR_IMPLEMENTATION_MISSING_ABSTRACT_CLASS = "Adapter's implementation 'MyImpl' must implement abstract method " \
                                               "'my_method()'"


def _is_abstract_method(x) -> bool:
    return inspect.isfunction(x) and getattr(x, "__isabstractmethod__", False)
