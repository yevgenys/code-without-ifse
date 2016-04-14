from src.utils.func_utils import extract_filter_value

"""
EXAMPLE 1
"""


def simple_if(a, b):
    if a:
        return a
    else:
        return b


def simple_if_no_if(a, b):
    return extract_filter_value(filter(lambda item: item, (a, b)))


"""
END EXAMPLE 1
"""