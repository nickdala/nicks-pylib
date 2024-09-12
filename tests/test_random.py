import pytest

from nickspylib.random import generate_random_number

def test_generate_random_number():
    num = generate_random_number(3, 10)
    assert num >= 3
    assert num < 10
