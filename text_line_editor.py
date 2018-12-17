#! /usr/bin/python3

# text_line_editor.py - adds certain text pattern to each line, modifies text
# copied in clipboard, and returns it ready to paste

import sys
import pyperclip


def invalid():
    # invalid call
    print("""Usage: text_line_editor.py [action]
    Actions:
    - [bullet]: adds bullet points at the start of each line.""")
    sys.exit()


def add_bullet(lines_list):
    for i in range(len(lines_list)):
        lines_list[i] = '* ' + lines_list[i]
    return lines_list


# options dictionary
options = {'bullet': add_bullet}

ok = False

if len(sys.argv) == 2:  # check right number of arguments
    if sys.argv[1] in options.keys():  # check valid argument
        ok = True

if not ok:
    invalid()

# giving chance to copy text
input('Copy text to clipboard if it\'s not there yet . . .')

# importing text
text = pyperclip.paste()

# separate lines
lines = text.split('\n')

# modify lines
lines_edited = options[sys.argv[1]](lines)

# merge lines
text = '\n'.join(lines_edited)

# exporting text
pyperclip.copy(text)
