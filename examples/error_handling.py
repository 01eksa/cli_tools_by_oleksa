import random, time

from cli_tools.exceptions import (CLIError,         # Base class for all raised errors
                                  APIError,         # Error that raised when you pass invalid data to a function.
                                  ValidationError,  # Data not validated
                                  ConversionError)  # The transferred converter caused an error
from cli_tools import safe_run, try_until_ok, print_header

print_header('Safe Execution Demo')

with safe_run(debug=False, exit_on_error=False):
    print("Press Ctrl+C to test graceful exit, or wait for the error...")

    for i in range(3, 0, -1):
        print(f"Crashing in {i}...")
        time.sleep(1)

    raise CLIError("Something went wrong inside the app!")

print("App still working.")

###

print_header('Retry Logic Demo')


def unstable_network_request():
    """Simulates a connection that fails 70% of the time."""
    if random.random() < 0.7:
        raise ConnectionError("Connection timed out")
    return "200 OK"


print("Attempting to connect to server...")

status = try_until_ok(
    unstable_network_request,
    exceptions=ConnectionError,
    on_exception="Connection failed. Retrying..."
)

print(f"Success! Server response: {status}")
