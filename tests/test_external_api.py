import pytest
from unittest.mock import Mock, patch
import sys
import os
from src.external_api import external_api


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


class TestExternalApi:

    def test_external_api_success(self):

        with patch("external_api.os.getenv") as mock_getenv, patch("external_api.requests.request") as mock_request:
            mock_getenv.return_value = "fake_api_key"
            mock_response = Mock()
            mock_response.json.return_value = {"query": {"from": "EUR", "amount": "53"}, "result": 4200.50}
            mock_request.return_value = mock_response

            test_currency = {"operationAmount": {"currency": {"code": "EUR"}, "amount": "53"}}

            result = external_api(test_currency)

            assert result == 4200.50
            assert isinstance(result, float)

    def test_external_api_failure(self):
        with patch("external_api.os.getenv") as mock_getenv, patch(
            "external_api.requests.request", side_effect=Exception("Network error")
        ):
            mock_getenv.return_value = "fake_api_key"

            test_currency = {"operationAmount": {"currency": {"code": "EUR"}, "amount": "53"}}

            with pytest.raises(Exception):
                external_api(test_currency)
