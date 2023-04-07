import pytest
from ..factorielle import factorielle,syracuse,decroissant

def test_factorielle():
    result=factorielle(2)
    assert result==2
    result=factorielle(-1)
    assert result=="erreur"
    result=factorielle(None)
    assert result=="erreur"

def test_syracuse():
    suite=syracuse.l(14)
    assert suite==[14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

def test_decroissant():
    assert decroissant (8)== "8 7 6 5 4 3 2 1"
