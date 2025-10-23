import logging

from readers import YAML_reader

CORRECT_YAML = (
"""
name:
    first: Alice
    last: White
age: 30
active: true
"""
)

INCORRECT_YAML_PARSER_ERROR = (
"""
name:
        first: Alice
    last: White
age: 30
active: true
"""
)

INCORRECT_YAML_SCANNER_ERROR = (
"""
name:first: Alice
    last: White
age: 30
active: true
"""
)

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

# def test_on_incorrect_yaml_for_parser_error(caplog):
#     with caplog.at_level(logging.ERROR):
#         formatted_data = YAML_reader.process(INCORRECT_YAML_PARSER_ERROR)
#
#     assert formatted_data is None
#
#     assert ('There was an error with YAML structure: while parsing a '
#             'block mapping\n  in "<unicode string>", line 2, column '
#             '1:\n    name:\n    ^\nexpected <block end>, but found '
#             '\'<block mapping start>\'\n  in "<unicode string>", line 4, '
#             'column 5:\n        last: White\n        ^') in caplog.messages
#
# def test_on_incorrect_yaml_for_scanner_error(caplog):
#     with caplog.at_level(logging.ERROR):
#         formatted_data = YAML_reader.process(INCORRECT_YAML_SCANNER_ERROR)
#
#     assert formatted_data is None
#
#     assert ('There was an error with YAML structure: mapping values are '
#             'not allowed here\n  in "<unicode string>", line 3, column '
#             '9:\n        last: White\n            ^') in caplog.messages
#
# def test_wrong_datatype(caplog):
#     with caplog.at_level(logging.ERROR):
#         formatted_data = YAML_reader.process("qwe")
#
#     assert formatted_data is None
#
#     assert ("There was an error with given data: YAML top-level value is not"
#             " a mapping, actual type: <class 'str'>") in caplog.messages