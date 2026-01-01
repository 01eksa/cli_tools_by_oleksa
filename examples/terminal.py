from time import sleep
from cli_tools import terminal as t


t.clear_screen()
t.home_cursor()
t.set_title('Title')

print('Hello!')

print('This text will disappear in a second.')
sleep(1)
t.move_up(1)
t.clear_line()

print('Simple progress bar example: ')
pattern = '[{:<10}]'

for i in range(1, 11):
    t.clear_line()
    t.move_to_column(1)
    print(pattern.format('='*i), end='', flush=True)
    sleep(0.2)
print()

print('Simple spinner example: ', end='')
for i in range(4):
    for status in ['|', '/', '—', '\\']:
        print(status, end='', flush=True)
        sleep(0.1)
        t.move_backward(1)

print('Done')
