from processing.validator import validate_light

def test_valid_values():
    assert validate_light(0) == True
    assert validate_light(512) == True
    assert validate_light(1023) == True

def test_invalid_values():
    assert validate_light(-1) == False
    assert validate_light(1024) == False
    assert validate_light(None) == False
