import pytest
from src.aeroplane import Aeroplane
from src.utils import filter_by_country, filter_by_altitude, get_top_n_by_altitude, sort_by_velocity


class TestUtils:
    def test_filter_by_country(self):
        a1 = Aeroplane("1", None, "Russia", 100, 5000, 0, 0)
        a2 = Aeroplane("2", None, "USA", 100, 6000, 0, 0)
        a3 = Aeroplane("3", None, "Russia", 100, 7000, 0, 0)
        aeroplanes = [a1, a2, a3]

        filtered = filter_by_country(aeroplanes, ["Russia"])
        assert len(filtered) == 2
        assert filtered[0].origin_country == "Russia"

    def test_filter_by_altitude(self):
        a1 = Aeroplane("1", None, "RU", 100, 5000, 0, 0)
        a2 = Aeroplane("2", None, "RU", 100, 10000, 0, 0)
        a3 = Aeroplane("3", None, "RU", 100, 15000, 0, 0)
        aeroplanes = [a1, a2, a3]

        filtered = filter_by_altitude(aeroplanes, 8000, 12000)
        assert len(filtered) == 1
        assert filtered[0].altitude == 10000

    def test_get_top_n_by_altitude(self):
        a1 = Aeroplane("1", None, "RU", 100, 5000, 0, 0)
        a2 = Aeroplane("2", None, "RU", 100, 10000, 0, 0)
        a3 = Aeroplane("3", None, "RU", 100, 15000, 0, 0)
        aeroplanes = [a1, a2, a3]

        top2 = get_top_n_by_altitude(aeroplanes, 2)
        assert len(top2) == 2
        assert top2[0].altitude == 15000
        assert top2[1].altitude == 10000

    def test_sort_by_velocity(self):
        a1 = Aeroplane("1", None, "RU", 100, 5000, 0, 0)
        a2 = Aeroplane("2", None, "RU", 300, 6000, 0, 0)
        a3 = Aeroplane("3", None, "RU", 200, 7000, 0, 0)
        aeroplanes = [a1, a2, a3]

        sorted_asc = sort_by_velocity(aeroplanes, reverse=False)
        assert sorted_asc[0].velocity == 100
        assert sorted_asc[1].velocity == 200
        assert sorted_asc[2].velocity == 300
