from time import sleep
from cli_tools import progress_bar


with progress_bar(1000, 'Processing...', length=20) as bar:
    for i in range(500):
        sleep(0.01)             # do your job here
        bar.update(steps=2)

print('Done')
