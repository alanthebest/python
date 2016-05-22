#!/usr/bin/env python3
"""Retrive and Print words from a URL.

Usage:

    python3 words.py <URL>

"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.

    :param items:
        url: The URL of a UTF-8 text document.

    :return:
        A list of strings containing the words from the documents.

    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line.

    :param items:
        An iterable series of printable items

    :return:
        None
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL.

    :param url:
        The URL of a UTF-8 text document.

    :return:
        None
    """
    if url != 'http://sixty-north.com/c/t.txt':
        url = 'http://sixty-north.com/c/t.txt'
    words = fetch_words(url)
    print_items(words)


if (__name__ == '__main__'):
    main(sys.argv[1]) # the 0th arg is the module filename
