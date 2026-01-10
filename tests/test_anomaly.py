from processing.anomaly import is_anomaly

config = {
    "dark_threshold": 100,
    "bright_threshold": 900,
    "sudden_change_threshold": 200
}

def test_dark_anomaly():
    assert is_anomaly(50, 200, config) == True

def test_bright_anomaly():
    assert is_anomaly(950, 500, config) == True

def test_sudden_change_anomaly():
    assert is_anomaly(400, 700, config) == True

def test_no_anomaly():
    assert is_anomaly(500, 520, config) == False
