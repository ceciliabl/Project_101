import pytest
from ..syracuse import syracuse

def test_syracuse():
    suite=syracuse(14)
    assert suite==[14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
