from time import sleep
from cli_tools import progress_bar


with progress_bar(1000, 'Processing...', length=20) as bar:
    for i in range(1000):
        sleep(0.01)
        bar.update(steps=3)

print('Done')
