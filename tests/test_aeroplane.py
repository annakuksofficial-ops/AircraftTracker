import pytest
from src.aeroplane import Aeroplane


class TestAeroplane:
    def test_aeroplane_creation(self):
        a = Aeroplane("abc123", "TEST",
                      "Russia", 100.5,
                      5000.0, 30.0, 60.0)
        assert a.icao24 == "abc123"
        assert a.callsign == "TEST"
        assert a.origin_country == "Russia"

    def test_aeroplane_comparison(self):
        a1 = Aeroplane("a", None,
                       "RU", 100,
                       5000, 0, 0)
        a2 = Aeroplane("b", None,
                       "RU", 100,
                       10000, 0, 0)
        assert a1 < a2
        assert a2 > a1

    def test_from_state_vector(self):
        state = ["abc123", "TEST", "Russia", None, None,
                 30.0, 60.0, 5000.0, False, 100.5, 90.0, 0, None, None, None,
                 False, 0, 0]
        a = Aeroplane.from_state_vector(state)
        assert a.icao24 == "abc123"
        assert a.callsign == "TEST"
        assert a.origin_country == "Russia"
