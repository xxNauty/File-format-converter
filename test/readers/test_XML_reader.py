import logging

from readers import XML_reader

CORRECT_XML = "<person><name><first>Alice</first><last>White</last></name><age>30</age><active>true</active></person>"
INCORRECT_XML = "<person>name><first>Alice</first><last>White</last><name><age>30</age><active>true</active></person>"

def test_on_correct_xml(caplog):
    with caplog.at_level(logging.INFO):
        formatted_data = XML_reader.process(CORRECT_XML)

    assert "name" in formatted_data['person']
    assert "first" not in formatted_data['person']
    assert "first" in formatted_data['person']['name']
    assert "last" not in formatted_data['person']
    assert "last" in formatted_data['person']['name']
    assert "age" in formatted_data['person']
    assert "active" in formatted_data['person']

    assert formatted_data['person']['name']['first'] == "Alice"
    assert formatted_data['person']['name']['last'] == "White"
    assert formatted_data['person']['age'] == 30
    assert formatted_data['person']['active'] == True

    assert "XML read" in caplog.messages

# def test_on_incorrect_xml(caplog):
#     with caplog.at_level(logging.ERROR):
#         formatted_data = XML_reader.process(INCORRECT_XML)
#
#     assert formatted_data is None
#
#     assert 'XML parse error: mismatched tag: line 1, column 93' in caplog.messages
#
# def test_on_type_error(caplog):
#     with caplog.at_level(logging.ERROR):
#         XML_reader.process(123)
#
#     assert ("Type error during conversion: a bytes-like object is required, not 'int'" in caplog.messages)