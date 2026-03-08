from unittest.mock import patch
from datetime import datetime
import pytest

from cli_tools import get_input, get_password, get_choice, menu, yes_no
import cli_tools
from cli_tools.exceptions import ValidationError, ConversionError


GEN_FUNCS = [
    ('get_int', ['9.0', '0x8', '10'], 10),
    ('get_float', ['8', '0x7', '10.5'], 10.5),
    ('get_number', ['0xa', '8', '7.0'], 8.0),
    ('get_number', ['0xa', '7.0', '8'], 7.0),
    ('get_username', ['0not', 'username001_'], 'username001_'),
    ('get_username', ['0not', '_username001'], '_username001'),
    ('get_email', ['wrong@email', 'test@mail.com'], 'test@mail.com'),
    ('get_hex_rgb', ['ffffff', '#ff00ff'], '#ff00ff'),
    ('get_time', ['25:67', '23:59'], datetime.strptime('23:59', '%H:%M').time())
]


@pytest.mark.parametrize('inputs, expected', [
    (['25', 'abc', 'ab cd', '40, 40', '0 123', '25 13'], (25, 13)),
    (['23 102', '', '50 50'], (None, None))
])
def test_get_input(inputs, expected):
    with patch('builtins.input', side_effect=inputs):
        result = get_input(
            '> ',
            r'\d+ \d+',
            lambda s: all(0 <= int(el) <= 100 for el in s.split(' ')),
            lambda s: tuple(int(el) for el in s.split()),
            default=(None, None)
        )
        assert result == expected


@pytest.mark.parametrize('input_text, expected_error', [
    ('abc', ValidationError),
    ('12a', ConversionError)
])
def test_get_input_exceptions(input_text, expected_error):
    with patch('builtins.input', return_value=input_text):
        with pytest.raises(expected_error):
            get_input(
                '> ',
                r'\d+.',
                converter=int,
                retry=False
            )


@pytest.mark.parametrize('inputs, expected', [
    (['25', 'abc', 'ab cd', '40, 40', '0 123', '25 13'], '25 13'),
    (['23 102', '', '50 50'], '50 50')
])
def test_get_password(inputs, expected):
    with patch('getpass.getpass', side_effect=inputs):
        result = get_password(
            '> ',
            r'\d+ \d+',
            lambda s: all(0 <= int(el) <= 100 for el in s.split(' ')),
        )
        assert result == expected


@pytest.mark.parametrize('input_text, expected_error', [
    ('abc', ValidationError),
])
def test_get_password_exceptions(input_text, expected_error):
    with patch('getpass.getpass', return_value=input_text):
        with pytest.raises(expected_error):
            get_password(
                '> ',
                r'\d+.',
                retry=False
            )


@pytest.mark.parametrize('inputs, case_sensitive, expected', [
    (['option 1', 'Option 2'], True, 'Option 2'),
    (['option1', 'option 3'], False, 'option 3'),
])
def test_get_choice(inputs, case_sensitive, expected):
    with patch('builtins.input', side_effect=inputs):
        result = get_choice(
            options=['Option 1', 'Option 2', 'Option 3'],
            case_sensitive=case_sensitive,
        )
        assert result == expected


@pytest.mark.parametrize('inputs, expected', [
    (['option 1', 'Option 2', '3'], 3),
    (['option 2', 'Option 3', '1'], 1),
    (['   0    ', '2'], 2)
])
def test_menu(inputs, expected):
    with patch('builtins.input', side_effect=inputs):
        result = menu(
            options={
                1: 'Option 1',
                2: 'Option 2',
                3: 'Option 3'
            },
        )
        assert result == expected


@pytest.mark.parametrize('inputs, expected', [
    (['yess', 'no'], False),
    (['123', 'Y'], True),
    (['no!', 'yes'], True),
    (['ye', 'N'], False)
])
def test_yes_no(inputs, expected):
    with patch('builtins.input', side_effect=inputs):
        result = yes_no()
        assert result == expected


@pytest.mark.parametrize('func_name, inputs, expected', GEN_FUNCS)
def test_gen_func(func_name, inputs, expected):
    func = getattr(cli_tools, func_name)
    with patch('builtins.input', side_effect=inputs):
        assert func('> ') == expected
