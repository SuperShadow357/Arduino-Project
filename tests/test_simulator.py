from main import Simulator

def test_simulator_range():
    sim = Simulator()
    for _ in range(100):
        val = sim.read_value()
        assert 0 <= val <= 1023
