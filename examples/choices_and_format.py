from cli_tools import print_header, get_choice, menu, yes_no, print_iterable, print_table


# Defines the main menu options for the menu() function.
# Keys (int) are the expected user input; values (str) are the displayed option text.
main_menu = {
    1: 'New game',
    2: 'Best players',
    3: 'Show results',
    0: 'Quit',
}

# Simple list of players for print_iterable demonstration.
players = [
    'You',
    'Not you',
    'Who?'
]

# Dictionary of results for print_table demonstration.
# The items (key-value pairs) will be unpacked into table rows.
results = {
    'Easy': 2308,
    'Medium': 1841,
    'Hard': 1550,
}


def play():
    """Starts the game flow, handling difficulty selection."""

    modes = ['Easy', 'Medium', 'Hard']

    # get_choice() validates user input against a list of options (modes).
    # show=True displays the options automatically before prompting.
    mode = get_choice(
        options = modes,
        prompt = 'Choose difficulty: ',
        if_invalid = 'Please, enter a valid mode name.',
        show = True
    ).lower()

    print(f'Some game logic for {mode} mode...')


def main():
    """Main loop for the CLI application, controlling flow via the menu."""

    # print_header() adds visual separation and a centered title to the console.
    print_header('Choices And Format Demo', char='=', space=3)

    while True:
        # menu() handles display, validates input against the dictionary keys, and returns the selected key (int).
        match menu(main_menu, 'What would you like to do? '):
            case 1:
                play()
            case 2:
                # print_iterable() outputs a one-dimensional list with custom formatting.
                print_iterable(
                    players,
                    start='\nBest players:\n',
                    item_pattern='- {}'
                )
            case 3:
                # print_table() iterates over results.items() and unpacks each pair into the row_pattern.
                print_table(
                    results.items(),
                    # Pattern uses format specifiers for alignment:
                    # {:<6} for left-aligned string, {:>8} for right-aligned integer
                    row_pattern = '{:<6}{:>8}',
                    start = '\nMode\tResults\n'
                )
            case 0:
                # yes_no() prompts for confirmation and returns a boolean (True for 'yes', False for 'no').
                if yes_no('Exit? [y/N]: '):
                    break

    print('Bye!')


if __name__ == '__main__':
    main()
