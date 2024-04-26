import pytest
from unittest.mock import patch, MagicMock
from requests import Response
from ..src.services import fetch_polygon_data, scrape_marketwatch_data

class TestFetchPolygonData:
    @patch('requests.get')
    def test_fetch_polygon_data_successful(self, mock_get):
        symbol = "AAPL"
        with patch("requests.get") as mocked_get:
      
            mocked_response = Response()
            mocked_response.status_code = 200
            mocked_response.json = MagicMock(return_value={"some": "data"})

            mocked_get.return_value = mocked_response

            result = fetch_polygon_data(symbol)
            assert result == {"some": "data"}

    @patch('requests.get')
    def test_fetch_polygon_data_invalid_symbol(self, mock_get):
        symbol = "INVALID"
        with patch("requests.get") as mocked_get:
            mocked_response = Response()
            mocked_response.status_code = 404
            mocked_get.return_value = mocked_response

            result = fetch_polygon_data(symbol)
            assert result == {}

    @pytest.mark.asyncio
    async def test_scrape_marketwatch_data(self):
        symbol = "AAPL"
        result = await scrape_marketwatch_data(symbol)
        expected_data = {
            "1 Day": 1.23,
            "5 Day": 4.56,
            "1 Month": 7.89,
            "3 Month": 12.34,
            "YTD": 15.67,
            "1 Year": 18.90,
            "3 Year": 23.45,
            "5 Year": 26.78,
            "10 Year": 29.01
        }
        assert result == expected_data
