#!/usr/bin/env python3
"""Retrive and Print words from a URL.

Usage:

    python3 words.py <URL>

"""

def banner(message, border = '-'):
    line = border * len(message)
    print (line)
    print (message)
    print (line)

def main():
    """Print each word from a text document from a URL.

    :param url:
        The URL of a UTF-8 text document.

    :return:
        None
    """
    banner("This is cool!", "~")

if (__name__ == '__main__'):
    main() # the 0th arg is the module filename
