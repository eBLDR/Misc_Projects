#! /usr/bin/python3

# multiclipboard.py - saves and loads pieces of text to the clipboard

import shelve
import sys
import pyperclip


def invalid_argv():
    print("""Usage:
    
    multiclipboard.py save <keyword> - saves clipboard to keyword
    multiclipboard.py load <keyword> - loads keyword text to clipboard
    multiclipboard.py delete <keyword> - deletes keyword data entry
                      delete all - deletes all entries
    multiclipboard.py list - prints a list of current keywords
    """)
    sys.exit()


def save_entry(shelve_file, key):
    input('Paste text to be saved . . .')
    if pyperclip.paste():
        shelve_file[key] = pyperclip.paste()
        print('Data saved into <{}>.'.format(key))


def load_entry(shelve_file, key):
    data = shelve_file.get(key, '')
    if data:
        pyperclip.copy(shelve_file[key])
        print('Data for <{}> loaded into clipboard.'.format(key))
    else:
        print('Keyword not existing.')
        sys.exit()


def delete_entry(shelve_file, key):
    check = input('Delete <{}> [y/n]? '.format(key)).lower()
    if check == 'y':
        if key == 'all':
            shelve_file.clear()
            print('All entries deleted.')
        else:
            del shelve_file[key]
            print('<{}> deleted.'.format(key))


def keyword_list(shelve_file):
    if shelve_file.keys():
        print(str(list(shelve_file.keys())))
    else:
        print('No data saved.')


mcbShelf = shelve.open('mcb.dat')

# checking task
if len(sys.argv) == 2 and sys.argv[1] == 'list':
    keyword_list(mcbShelf)
elif len(sys.argv) == 3 and sys.argv[1] == 'save':
    save_entry(mcbShelf, sys.argv[2])
elif len(sys.argv) == 3 and sys.argv[1] == 'load':
    load_entry(mcbShelf, sys.argv[2])
elif len(sys.argv) == 3 and sys.argv[1] == 'delete':
    delete_entry(mcbShelf, sys.argv[2])
else:
    invalid_argv()

mcbShelf.close()
