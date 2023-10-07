from plates import is_valid


def test_valid():
    assert is_valid("CS50") == True


def test_beginning_alphabetical():
    assert is_valid("50") == False

def test_zero_at_digit2():
    assert is_valid("CS05") == False


def test_char_after_num():
    assert is_valid("CS50P") == False


def test_punctuation():
    assert is_valid("PI3.14") == False


def test_Les_number_of_chars():
    assert is_valid("H") == False


def test_mor_number_of_chars():
    assert is_valid("Helloworld") == False


def test_Upper_Lower_chars():
    assert is_valid("cSCs23") == True


