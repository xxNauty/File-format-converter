import logging

from input import file_reader

def test_on_existing_file(caplog):
    with caplog.at_level(logging.INFO):
        data_from_file = file_reader.read_file("test/file/file_for_test.txt")

    assert "File read" in caplog.messages
    assert data_from_file == 'somedata\nfor testing pur\nposes123_312!@#'

def test_on_non_existing_file(caplog):
    with caplog.at_level(logging.INFO):
        data_from_file = file_reader.read_file("../test/file/non_existing_file.txt")

    assert "There is no such file" in caplog.messages
    assert data_from_file is None