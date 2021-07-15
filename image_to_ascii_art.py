"""Image to ASCII art by Phan Huynh Thien Phuc
This ascii_magic module can transform a normal picture to an ASCII art.
See that empty string? Enter the file's name in it. Make sure it's in
the same folder with this .py file, or you'll have to type the entire path to it.
You can try changing the "columns" and "char" parameters and see what happens.
Important: You MUST run this .py file with the terminal/command prompt."""

import ascii_magic
output = ascii_magic.from_image_file("", columns=100, char="#")
ascii_magic.to_terminal(output)
