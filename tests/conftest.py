import pytest

from src.oop import OopExample, Formatters


@pytest.fixture
def oop_obj():
    return OopExample()


@pytest.fixture
def formatter():
    return Formatters.SomeFormatting()