import pytest

from cli_tools.validators import *


def fake_validator(ret: bool):
    return lambda x: ret


@pytest.mark.parametrize('validators, expected', [
    ((fake_validator(True), fake_validator(True)), True),
    ((fake_validator(False), fake_validator(False)), False),
    ((fake_validator(True), fake_validator(False)), True),
    ((fake_validator(False), fake_validator(True)), True),
])
def test_any_of(validators, expected):
    assert any_of(*validators)('') == expected


@pytest.mark.parametrize('validators, expected', [
    ((fake_validator(True), fake_validator(True)), True),
    ((fake_validator(False), fake_validator(False)), False),
    ((fake_validator(True), fake_validator(False)), False),
    ((fake_validator(False), fake_validator(True)), False),
])
def test_all_of(validators, expected):
    assert all_of(*validators)('') == expected


@pytest.mark.parametrize('string, expected', [
    ('-1', False),
    ('10.0', True),
    ('1', True),
    ('1.1', True),
    ('0', False),
    ('11', False),
    ('abc', False),
    ('5.67', True)
])
def test_is_in_range(string, expected):
    assert is_in_range(1, 10)(string) == expected


@pytest.mark.parametrize('string, expected', [
    ('-1', False),
    ('10.0', False),
    ('1', False),
    ('1.1', True),
    ('0', False),
    ('11', False),
    ('abc', False),
    ('5.67', True)
])
def test_is_between(string, expected):
    assert is_between(1, 10)(string) == expected


@pytest.mark.parametrize('validator, string, expected', [
    (more(5), '5', False),
    (more(5), '5.0001', True),
    (more_or_equal(5), '5', True),
    (more_or_equal(5), '10243', True),
    (less(5), '5', False),
    (less(5), '4.99', True),
    (less_or_equal(5), '5', True),
    (less_or_equal(5), '4.99', True),
])
def test_compare_validators(validator, string, expected):
    assert validator(string) == expected


@pytest.mark.parametrize('validator, string, expected', [
    (is_in_list(['opt_1', 'opt_2', 'opt_3',]), 'Opt_3', False),
    (is_in_list(['opt_1', 'opt_2', 'opt_3',], False), 'Opt_3', True),
    (not_in_list(['opt_1', 'opt_2', 'opt_3',], ), 'Opt_1', True),
    (not_in_list(['opt_1', 'opt_2', 'opt_3',], False), 'Opt_1', False),
])
def test_is_in_list_validators(validator, string, expected):
    assert validator(string) == expected


@pytest.mark.parametrize('validator, string, expected', [
    (is_list_of(r'\d+'), ' 1 2   3  ', True),
    (is_list_of(r'\d+', ' '), ' 1 2   3', False),
    (is_list_of(r'\d+', ','), '1,2,3', True),
    (is_list_of(r'\d+', ','), '1 2 3', False),
    (is_list_of(r'.+', ';'), 'some;separated;words;123', True)
])
def test_is_list_of(validator, string, expected):
    assert validator(string) == expected


@pytest.mark.parametrize('validator, string, expected', [
    (is_date('%Y.%m.%d'), '2026.01.01', True),
    (is_date('%Y.%m.%d'), '2026.13.01', False),
    (is_date('%Y.%m.%d'), '2026.01.32', False),
    (is_date('%Y.%m.%d'), '2026:01:01', False),
    (is_time('%H:%M'), '00:00', True),
    (is_time('%H:%M'), '00:61', False),
    (is_time('%H:%M'), '24:01', False),
    (is_time('%H:%M'), '13 00', False),
    (is_time('%H:%M:%S'), '23:59:34', True),
    (is_time('%H:%M:%S'), '23:59:61', False),
])
def test_datetime_validators(validator, string, expected):
    assert validator(string) == expected
