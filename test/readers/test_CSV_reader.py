import logging

from readers import CSV_reader

CORRECT_CSV = "id,name,age\n100,Alice,30\n101,Bob,25\n"

def test_on_correct_csv():
    formatted_data = CSV_reader.process(CORRECT_CSV, "id")

    assert '100' in formatted_data
    assert '101' in formatted_data

    assert formatted_data['100']['name'] == "Alice"
    assert formatted_data['100']['age'] == "30"

    assert formatted_data['101']['name'] == "Bob"
    assert formatted_data['101']['age'] == "25"

    assert len(formatted_data) == 2
    assert len(formatted_data['100']) == 2
    assert len(formatted_data['101']) == 2

def test_on_incorrect_key_column(caplog):
    with caplog.at_level(logging.ERROR):
        formatted_data = CSV_reader.process(CORRECT_CSV, "idd")

    assert formatted_data is None
    assert 'An error occurred while conversion: "Key column \'idd\' not found in CSV headers"' in caplog.messages

def test_wrong_delimiter(caplog):
    with caplog.at_level(logging.ERROR):
        formatted_data = CSV_reader.process(CORRECT_CSV, "id", ":")

    assert formatted_data is None
    assert 'An error occurred while conversion: There is no such character in data' in caplog.messages