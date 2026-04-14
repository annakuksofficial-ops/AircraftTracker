import pytest
import json
import os
from src.aeroplane import Aeroplane
from src.file_saver import JSONSaver


class TestJSONSaver:
    def setup_method(self):
        self.test_filename = "data/test_aeroplanes.json"
        self.saver = JSONSaver(self.test_filename)

    def teardown_method(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        if os.path.exists("data") and not os.listdir("data"):
            os.rmdir("data")

    def test_add_and_get_aeroplane(self):
        a = Aeroplane("abc123", "TEST", "Russia", 100.5, 5000.0, 30.0, 60.0)
        self.saver.add_aeroplane(a)

        aeroplanes = self.saver.get_aeroplanes()
        assert len(aeroplanes) == 1
        assert aeroplanes[0].icao24 == "abc123"

    def test_no_duplicates(self):
        a = Aeroplane("abc123", "TEST", "Russia", 100.5, 5000.0, 30.0, 60.0)
        self.saver.add_aeroplane(a)
        self.saver.add_aeroplane(a)

        aeroplanes = self.saver.get_aeroplanes()
        assert len(aeroplanes) == 1

    def test_delete_aeroplane(self):
        a = Aeroplane("abc123", "TEST", "Russia", 100.5, 5000.0, 30.0, 60.0)
        self.saver.add_aeroplane(a)

        self.saver.delete_aeroplane(a)
        aeroplanes = self.saver.get_aeroplanes()
        assert len(aeroplanes) == 0
