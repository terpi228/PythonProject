# from unittest.mock import mock_open, patch
# from src.utils import read_json
#
#
# class TestUtils:
#
#     @patch("builtins.open", mock_open(read_data='{"key": "value"}'))
#     @patch("src.logs.json.load")  # Изменено с "json.load" на "src.logs.json.load"
#     def test_utils_success(self, mock_json_load):
#         mock_json_load.return_value = {"test": "data"}
#         result = utils("test.json")
#         assert result == {"test": "data"}
#
#     @patch("builtins.open", side_effect=FileNotFoundError)
#     def test_utils_file_not_found(self, mock_file):
#         result = utils("nonexistent.json")
#         assert result == []  # Изменено с is на == для сравнения списков
#
#     @patch("builtins.open", mock_open(read_data="invalid json"))
#     @patch("src.logs.json.load", side_effect=Exception("JSON error"))  # Изменено здесь
#     def test_utils_json_error(self, mock_json_load):
#         result = utils("bad_json.json")
#         assert result == []  # Изменено с is на ==
#
#     @patch("builtins.open", side_effect=Exception("Unexpected error"))
#     def test_utils_general_exception(self, mock_file):
#         result = utils("problematic.json")
#         assert result == []  # Изменено с is на ==
