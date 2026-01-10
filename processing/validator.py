def validate_light(value):
    if value is None:
        return False
    return 0 <= value <= 1023
