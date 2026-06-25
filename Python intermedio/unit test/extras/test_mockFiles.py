import unittest
from unittest.mock import patch, mock_open
from mockFiles import read_lines


class TestReadLines(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="line 1\nline 2\n")
    def test_read_lines_success(self, mock_file):
        result = read_lines("test.txt")
        self.assertEqual(result, ["line 1\n", "line 2\n"])
        mock_file.assert_called_once_with("test.txt", "r")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_lines_file_not_found(self, mock_file):
        with self.assertRaises(FileNotFoundError):
            read_lines("no_file.txt")

        mock_file.assert_called_once_with("no_file.txt", "r")
