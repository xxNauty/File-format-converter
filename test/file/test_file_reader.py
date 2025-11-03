import logging
import os

from input import file_reader

def test_on_existing_file(caplog):
    _prepare_file_for_tests()

    with caplog.at_level(logging.INFO):
        data_from_file = file_reader.read_file("test/file/file_for_test.txt")

    assert "File read" in caplog.messages
    assert data_from_file == 'somedata\nfor testing pur\nposes123_312!@#'

    _cleanup_after_tests()

def test_on_non_existing_file(caplog):
    with caplog.at_level(logging.INFO):
        data_from_file = file_reader.read_file("../test/file/non_existing_file.txt")

    assert "There is no such file" in caplog.messages
    assert data_from_file is None

def _prepare_file_for_tests() -> None:
    with open("test/file/file_for_test.txt", 'w') as file:
        file.write('somedata\nfor testing pur\nposes123_312!@#')
        file.close()

def _cleanup_after_tests() -> None:
    os.remove("test/file/file_for_test.txt")
