from seasons import sing
from seasons import calcualte_minutes
from datetime import date


def test_calcualte_minutes():
    assert calcualte_minutes(date.fromisoformat("1998-10-25")) == 13121280
    assert calcualte_minutes(date.fromisoformat("2022-10-06")) == 525600


def test_sing():
    assert (
        sing(13121280)
        == "Thirteen million, one hundred twenty-one thousand, two hundred eighty minutes"
    )
    assert sing(525600) == "Five hundred twenty-five thousand, six hundred minutes"
