from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    jar.deposit(5)
    print(jar)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    jar.deposit(5)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(5)


def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.withdraw(6)
