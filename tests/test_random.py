import pytest

from nicks_pylib import nick

def test_random():
    num = nick.generate_random_number(3, 6)
    assert num >= 3
    assert num < 6