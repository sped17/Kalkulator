import pytest 
import kalkulator as k

def test_dodawanie():
    assert k.dodawanie(0, 0) == 0
    assert k.dodawanie(5, 7) == 12
    assert k.dodawanie(3.5, 7) == 10.5
    with pytest.raises(ValueError):
        k.dodawanie("p",0)


def test_odejmowanie():
    assert k.odejmowanie(0, 0) == 0
    assert k.odejmowanie(5, 7) == -2
    assert k.odejmowanie(3.5, 7) == -3.5
    with pytest.raises(ValueError):
        k.odejmowanie("p", 0)

def test_mnozenie():
    assert k.mnozenie(0, 0) == 0
    assert k.mnozenie(5, 7) == 35
    assert k.mnozenie(3.5, 7) == 24.5
    assert k.mnozenie(-1, -1) == 1
    assert k.mnozenie(-1, 1) == -1
    with pytest.raises(ValueError):
        k.mnozenie("p", 0)

def test_dzielenie():
    assert k.dzielenie(0, 0) == "Blad! Nie mozna dzielic przez 0!"
    assert k.dzielenie(7, 8) == 0.875
    assert k.dzielenie(7, 3.5) == 2
    assert k.dzielenie(-1, -1) == 1
    assert k.dzielenie(-1, 1) == -1
    with pytest.raises(ValueError):
        k.dzielenie("p", 0)
        
def test_potegowanie():
    assert k.potegowanie(0, 0) == 1
    assert k.potegowanie(2, 3) == 8
    assert k.potegowanie(3, 2) == 9

