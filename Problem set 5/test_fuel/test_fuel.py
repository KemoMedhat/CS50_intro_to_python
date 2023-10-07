from fuel import convert, gauge
import pytest


def test_Zero_Division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_nun_numaric():
    with pytest.raises(ValueError):
        convert("three/four")


def test_X_greater_Y():
    with pytest.raises(ValueError):
        convert("10/4")


def test_empty_tank0():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_full_tank100():
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_print_percent_char():
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"


def test_normal_fraction():
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75
