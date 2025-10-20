import pytest
import logging

from readers import XML_reader

CORRECT_XML = "<person><id>123</id><name>Jane Doe</name><email>jane.doe@example.com</email></person>"
INCORRECT_XML = "<person<id>123</id><name>Jane Doe<name><email>jane.doe@example.com</email></person>"

def test_on_correct_xml():
    formatted_data = XML_reader.process(CORRECT_XML)

    assert formatted_data['person']['id'] == '123'
    assert formatted_data['person']['name'] == "Jane Doe"
    assert formatted_data['person']['email'] == "jane.doe@example.com"

def test_on_incorrect_xml():
    formatted_data = XML_reader.process(INCORRECT_XML)

    assert formatted_data is None

def test_logging_on_incorrect_xml(caplog):
    with caplog.at_level(logging.ERROR):
        XML_reader.process(INCORRECT_XML)

    assert "XML parse error: not well-formed (invalid token): line 1, column 7" in caplog.messages

def test_logging_on_type_error(caplog):
    with caplog.at_level(logging.ERROR):
        XML_reader.process(123)

    assert ("Type error during conversion: a bytes-like object is required, not 'int'" in caplog.messages)