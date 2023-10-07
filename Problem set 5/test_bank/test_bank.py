from bank import value


def test_hello():
    assert value("hello world") == 0


def test_hey():
    assert value("hey") == 20


def test_alse():
    assert value("good morning") == 100


def test_hello_upper():
    assert value("HELLO WORLD") == 0


def test_hey_upper():
    assert value("Hey") == 20


def test_alse_upper():
    assert value("Ghood Morning") == 100
