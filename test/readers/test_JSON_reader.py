import pytest
import logging

from readers import JSON_reader

CORRECT_JSON = '{"name": "Alice", "age": 30, "active": true}'
INCORRECT_JSON = '{"name": "Alice, "age": 30, "active": True}'

def test_on_correct_json():
    formatted_data = JSON_reader.process(CORRECT_JSON)

    assert formatted_data['name'] == "Alice"
    assert formatted_data['age'] == 30
    assert formatted_data['active'] == True


def test_on_incorrect_json():
    formatted_data = JSON_reader.process(INCORRECT_JSON)

    assert formatted_data is None

def test_input_type():
    with pytest.raises(TypeError):
        JSON_reader.process(123)

def test_logging_on_success(caplog):
    with caplog.at_level(logging.INFO):
        JSON_reader.process(CORRECT_JSON)

    assert "JSON read" in caplog.messages

def test_logging_on_error(caplog):
    with caplog.at_level(logging.ERROR):
        JSON_reader.process(INCORRECT_JSON)

    assert "An error occurred with JSON structure" in caplog.messages