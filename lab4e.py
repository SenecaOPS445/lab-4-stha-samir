#!/usr/bin/env python3
# Author ID: [sshrestha80]

def is_digits(sobj):
    """Returns True if all characters in the string are digits, otherwise False."""
    return sobj.isdigit()

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')
