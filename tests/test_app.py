import pytest

MOCK_DICTIONARY = {
    "first_name":"Paola",
    "last_name":"Cortes",
    "active":1,
    "age": 100,
    "username":"PaolaCortes"
}

def test_dictionary_has_valid_age():
    assert isinstance(MOCK_DICTIONARY["age"], int)

def test_dictionary_has_valid_username():
    assert MOCK_DICTIONARY.get("username") == "PaolaCortes"