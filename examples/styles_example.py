import cli_tools.styles as s
from cli_tools.styles import (
    rgb,       # Converts full-range RGB (HEX or tuple) into an ANSI color code.
    stylize    # Applies one or more style codes (color, background, format) to text.
)


# These functions apply a default foreground color and return the styled string.
error_msg = s.error('Error message')
warning_msg = s.warning('Warning message')
success_msg = s.success('Success message')
info_msg = s.info('Info message')

print(error_msg)
print(warning_msg)
print(success_msg)
print(info_msg)

# Define custom color using an RGB tuple (24-bit color).
tuple_yellow = (240, 240, 100)

# Apply the tuple color as foreground (text).
print(
    stylize('Yellow text', rgb(tuple_yellow))
)

# Apply the tuple color as background (using is_bg=True) and combine with BLACK foreground (text).
print(
    stylize('Yellow background', rgb(tuple_yellow, is_bg=True), s.BLACK)
)

# Define custom colors using the rgb function with HEX codes.
# The first color is foreground (text), the second specifies the background (bg#).
gray = rgb('#dddddd')
darkblue_bg = rgb('bg#0a0a88')

# wrap() applies multiple styles (foreground, background, and formatting constants).
print(
    stylize('Styled message', gray, darkblue_bg, s.ITALIC, s.UNDERLINE)
)
