import logging

from readers import TOML_reader

CORRECT_TOML = """
age = 30
active = true

[name]
first = "Alice"
last = "White"
"""

def test_on_correct_toml(caplog):
    with caplog.at_level(logging.INFO):
        formatted_data = TOML_reader.process(CORRECT_TOML)

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

    assert "TOML read" in caplog.messages