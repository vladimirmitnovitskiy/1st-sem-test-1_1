import pytest
import random

from src.fast_pow import fastPow

#def cases
def test_two_power_two():
    assert fastPow(2, 2) == 4


def test_negative():
    assert fastPow(-1, 4) == 1
    assert fastPow(-3, 3) == -27
    assert fastPow(-3 ,-3) == '1/-27'

#extrem cases

def test_zero_power():
    assert fastPow(123, 0) == 1

def test_power_one():
    assert fastPow(111, 1) == 111

#poperty-based tests

@pytest.mark.parametrize("_", range(100))
def test_random_power_random(_):
    a, b = random.randint(1,1000), random.randint(1,1000)
    assert fastPow(a, b) == a**b
