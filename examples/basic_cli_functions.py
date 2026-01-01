from cli_tools import print_header, get_input, get_int, get_number
from cli_tools.validators import is_in_range


print_header('Basic CLI Functions')

name = get_input(
    'What is your name? ',
    # DEMO: converter can modify input before return.
    # NOTE: For simple string ops like this, get_input().strip().capitalize() is cleaner.
    converter=lambda s: s.strip().capitalize(),
    # returns 'Anonim' if the user presses Enter.
    default='Anonim'
)


# get_int ensures integer format.
age = get_int(
    'How old are you? ',
    # validator checks if the number is within the range [10, 100].
    validator=is_in_range(10, 100),
    # message to show if input is incorrect
    if_invalid='Age must be an integer between 10 and 100.',
)

# get_number passes int and float numbers (returns always float).
num = get_number(
    'What is your favourite number? ',
    if_invalid='Please, enter a number.'
)


print(f"Nice to meet you, {name}! You are {age} years old and your favorite number is {num}. I like it!")
