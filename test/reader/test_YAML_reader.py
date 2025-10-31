import logging

from reader import YAML_reader

CORRECT_YAML = (
"""
name:
    first: Alice
    last: White
age: 30
active: true
"""
)

# INCORRECT_YAML_PARSER_ERROR = (
# """
# name:
#         first: Alice
#     last: White
# age: 30
# active: true
# """
# )
#
# INCORRECT_YAML_SCANNER_ERROR = (
# """
# name:first: Alice
#     last: White
# age: 30
# active: true
# """
# )

def test_on_correct_yaml(caplog):
    with caplog.at_level(logging.INFO):
        formatted_data = YAML_reader.process(CORRECT_YAML)

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

    assert len(formatted_data) == 3

    assert "YAML read" in caplog.messages