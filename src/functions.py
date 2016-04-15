from src.utils.func_utils import extract_filter_value


def simple_if(a, b):
    if a:
        return a
    return b


def simple_if_no_if(a, b):
    return extract_filter_value(filter(lambda item: item, (a, b)))
