import math

import pytest


def calculate_square_root(data):
    if not  (isinstance(data, float) or isinstance(data, int)):
        raise ValueError("number has an invalid string")

    ans = math.sqrt(data)
    return ans


def test_calculate_square_root():
    assert calculate_square_root(4)==2


def test_calculate_square_root_error():
    with pytest.raises(ValueError):
        calculate_square_root("dad")



if __name__ == "__main__":
    pass