import logging
import os.path

from output import file_writer

FILEPATH = "test.txt"

def test_on_correct_data(caplog):
    with caplog.at_level(logging.INFO):
        file_writer.write_to_file(FILEPATH, "data\nfor\n\ntests#@!123")

    assert "Data writen to file" in caplog.messages
    assert os.path.exists(FILEPATH) is True

    with open(FILEPATH, 'r') as file:
        assert file.read() == "data\nfor\n\ntests#@!123"

    _clean_after_tests()

def test_on_incorrect_data(caplog):
    with caplog.at_level(logging.INFO):
        file_writer.write_to_file(FILEPATH, 123)

    assert 'Something went wrong when writing to file: write() argument must be str, not int' in caplog.messages
    assert os.path.exists(FILEPATH) is False

def _clean_after_tests():
    os.remove(FILEPATH)