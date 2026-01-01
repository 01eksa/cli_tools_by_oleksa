import re
from cli_tools import (print_header, get_input,
                           extract_match) # extract list of all matches, optionally convert every match
from cli_tools.patterns import NUMBER     # Ready-made pattern: accepts both int and float

# Pattern <number> <operator> <number>, spaces ignored
simple_expr_pattern = re.compile(fr' *({NUMBER.pattern}) *([+\-*/^]) *({NUMBER.pattern}) *')
# Accepts either numbers or operators. Converts numbers to float
converter = lambda x: float(x) if x not in '+-*/^' else x

print_header('| Simple calculator |', '—')
print('Supports simple expressions in format <number> <operator> <number>. Press Ctrl+C to exit.')

while True:
    # Guaranteed to pass only input that matches the pattern
    expr = get_input('> ', pattern=simple_expr_pattern, if_invalid='Wrong format!')
    # Unpack the input, immediately converting the numbers
    left, operator, right = extract_match(expr, simple_expr_pattern, converter=converter)

    match operator:
        case '+':
            print(left+right)
        case '-':
            print(left-right)
        case '*':
            print(left*right)
        case '/':
            if right == 0:
                print('Division by zero is not allowed!')
                continue
            print(left/right)
        case '^':
            print(left**right)
        case _:
            print('Wrong operator!')
