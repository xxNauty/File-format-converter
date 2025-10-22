import logging

from readers import JSON_reader

CORRECT_JSON = '{"name": {"first": "Alice", "last": "White"}, "age": 30, "active": true}'
INCORRECT_JSON = '{"name": {"first": "Alice, "last" "White"}, "age": 30 "active": true}'

def test_on_correct_json(caplog):
    with caplog.at_level(logging.INFO):
        formatted_data = JSON_reader.process(CORRECT_JSON)

    assert "name" in formatted_data
    assert "first" not in formatted_data
    assert "first" in formatted_data['name']
    assert "last" not in formatted_data
    assert "last" in formatted_data['name']
    assert "age" in formatted_data
    assert "active" in formatted_data

    assert formatted_data['name']['first'] == "Alice"
    assert formatted_data['name']['last'] == "White"
    assert formatted_data['age'] == 30
    assert formatted_data['active'] == True

    assert "JSON read" in caplog.messages

def test_on_incorrect_json(caplog):
    with caplog.at_level(logging.ERROR):
        formatted_data = JSON_reader.process(INCORRECT_JSON)

    assert formatted_data is None

    assert ("An error occurred with JSON structure: "
            "Expecting ',' delimiter: line 1 column 29 (char 28)") in caplog.messages

def test_on_incorrect_datatype(caplog):
    with caplog.at_level(logging.ERROR):
        JSON_reader.process(123)

    assert ("Type error during conversion: the JSON object must be "
            "str, bytes or bytearray, not int") in caplog.messages