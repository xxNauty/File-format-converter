import logging

from readers import CSV_reader

CORRECT_CSV = "name.first,name.last,age,active\nAlice,White,30,true"

def test_on_correct_csv(caplog):
    with caplog.at_level(logging.INFO):
        formatted_data = CSV_reader.process(CORRECT_CSV)

    assert len(formatted_data) == 1

    assert 0 in formatted_data
    assert "name.first" in formatted_data[0]
    assert "name.last" in formatted_data[0]
    assert "age" in formatted_data[0]
    assert "active" in formatted_data[0]

    assert formatted_data[0]['name.first'] == 'Alice'
    assert formatted_data[0]['name.last'] == 'White'
    # assert formatted_data[0]['age'] == 30
    # assert formatted_data[0]['active'] == True

    assert "CSV read" in caplog.messages

# def test_on_incorrect_datatype(caplog):
#     with caplog.at_level(logging.ERROR):
#         CSV_reader.process(123)
#
#     assert "An error occurred: initial_value must be str or None, not int" in caplog.messages