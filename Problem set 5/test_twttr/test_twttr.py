from twttr import shorten


def test_twttr():
    assert shorten("kareem") == "krm"
    assert shorten("hussam") == "hssm"


def test_capitalized_vowel():
    assert shorten("KArEEm") == "Krm"
    assert shorten("HOssAAm") == "Hssm"


def test_omitting_numbers():
    assert shorten("0ne") == "0n"
    assert shorten("7ossam") == "7ssm"


def test_omitting_punctuation():
    assert shorten("k@reem.") == "k@rm."
    assert shorten("h@$$@m.") == "h@$$@m."



