from numb3rs import validate

def test_octet_formate():
    assert validate(r"192.168.1.1") == True
    assert validate(r"192.168.2.10.5") == False
    assert validate(r"192.168.1") == False

def test_octet_range():
    assert validate(r"255.12.15.0") == True
    assert validate(r"300.12.15.0") == False
    assert validate(r"192.300.15.0") == False
    assert validate(r"192.168.300.0") == False
    assert validate(r"192.168.1.300") == False
