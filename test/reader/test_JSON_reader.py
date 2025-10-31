import logging

from reader import JSON_reader

CORRECT_JSON = '{"name": {"first": "Alice", "last": "White"}, "age": 30, "active": true}'
# INCORRECT_JSON = '{"name": {"first": "Alice, "last" "White"}, "age": 30 "active": true}'

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
