import pytest

from src.functions import *


class TestFunctions:
    @pytest.mark.parametrize("inputs", [
        (None, 10),
        (10, None),
        (10, 20)
    ])
    def test_simple_if(self, inputs):
        assert simple_if(*inputs) == simple_if_no_if(*inputs)
