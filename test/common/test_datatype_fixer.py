from common import datatype_fixer

def test_for_int_val():
    assert datatype_fixer.fix_datatype('3') == 3
    assert datatype_fixer.fix_datatype('0') == 0
    assert datatype_fixer.fix_datatype('-8') == -8

    assert type(datatype_fixer.fix_datatype('4')) == int

def test_for_float_val():
    assert datatype_fixer.fix_datatype('3.3') == 3.3
    assert datatype_fixer.fix_datatype('.3') == .3
    assert datatype_fixer.fix_datatype('-0.3') == -0.3

    assert type(datatype_fixer.fix_datatype('0.3')) == float

def test_for_bool_val():
    assert datatype_fixer.fix_datatype('true') == True
    assert datatype_fixer.fix_datatype('false') == False

    assert type(datatype_fixer.fix_datatype('true')) == bool

def test_for_string_val():
    assert datatype_fixer.fix_datatype('qwerty') == 'qwerty'
    assert datatype_fixer.fix_datatype('') == ''

def test_for_none_val():
    assert datatype_fixer.fix_datatype(None) is None

def test_for_list():
    list_with_one_datatype = ['3', '6', '8', '55', '0', '-43']
    list_with_different_datatypes = ['5', '4.4', 'true', '0', '.333', '']

    assert datatype_fixer.fix_datatype(list_with_one_datatype) == [3, 6, 8, 55, 0, -43]
    assert datatype_fixer.fix_datatype(list_with_different_datatypes) == [5, 4.4, True, 0, .333, '']

def test_for_dict():
    dict_with_one_datatype = {
        'key_1': '3',
        'key_2': '7',
        'key_3': '88'
    }
    fixed_dict_with_one_datatype = {
        'key_1': 3,
        'key_2': 7,
        'key_3': 88
    }
    assert datatype_fixer.fix_datatype(dict_with_one_datatype) == fixed_dict_with_one_datatype

    dict_with_different_datatypes = {
        'key_1': '3',
        'key_2': '7.65',
        'key_3': '0.321',
        'key_4': 'false',
        'key_5': ''
    }
    fixed_dict_with_different_datatypes = {
        'key_1': 3,
        'key_2': 7.65,
        'key_3': 0.321,
        'key_4': False,
        'key_5': ''
    }
    assert datatype_fixer.fix_datatype(dict_with_different_datatypes) == fixed_dict_with_different_datatypes
