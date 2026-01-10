from processing.smoothing import moving_average

def test_moving_average_basic():
    values = [10, 20, 30, 40, 50]
    assert moving_average(values, 3) == (30+40+50)/3
    assert moving_average(values, 10) == sum(values)/len(values)

def test_moving_average_empty():
    assert moving_average([], 5) == None
