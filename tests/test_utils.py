from unittest.mock import mock_open, patch
from src.utils import utils


class TestUtils:

    @patch("builtins.open", mock_open(read_data='{"key": "value"}'))
    @patch("json.load")
    def test_utils_success(self, mock_json_load):
        mock_json_load.return_value = {"test": "data"}
        result = utils("test.json")
        assert result == {"test": "data"}

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_utils_file_not_found(self, mock_file):
        result = utils("nonexistent.json")
        assert result is False

    @patch("builtins.open", mock_open(read_data="invalid json"))
    @patch("json.load", side_effect=Exception("JSON error"))
    def test_utils_json_error(self, mock_json_load):
        result = utils("bad_json.json")
        assert result is False

    @patch("builtins.open", side_effect=Exception("Unexpected error"))
    def test_utils_general_exception(self, mock_file):
        result = utils("problematic.json")
        assert result is False
