import pytest
from unittest.mock import Mock, patch
from src.api_client import OpenSkyClient, NominatimClient


class TestOpenSkyClient:
    @patch('src.api_client.requests.Session.get')
    def test_get_data(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"states": []}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        client = OpenSkyClient()
        result = client.get_data(45, 47, 5, 10)

        assert result == {"states": []}
        mock_get.assert_called_once()


class TestNominatimClient:
    @patch('src.api_client.requests.Session.get')
    def test_get_data(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = [{"boundingbox": ["45", "47", "5", "10"]}]
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        client = NominatimClient()
        result = client.get_data("Russia")

        assert result["boundingbox"] == ["45", "47", "5", "10"]
