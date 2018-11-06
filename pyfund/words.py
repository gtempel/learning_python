#! /usr/bin/env python3
"""Retrieve and print words from a URL.

Usage:

  python3 words.py <URL>
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
  """Fetch a list of words from a URL,
  
  Args:
    url: the URL of a UTF-8 text document.
  
  Returns:
    A list of strings containing the words from
    the document.
  """
  # the above docstring can be displayed in the REPL
  # via help(words.fetch_words)

  # the 'with' binds the http response to 'story'
  # 'http://sixty-north.com/c/t.txt'
  with urlopen(url) as story:
    story_words = []
    for line in story:
      # stuff comes back as bytes...need to decode it
      line_words = line.decode('utf-8').split()
      for word in line_words:
        story_words.append(word)
  return story_words


def print_items(items):
  """Print items one per line.

  Args:
    An iterable series of printable items.
  """
  for item in items:
    print(item)


# could be called anything
def main(url):
  """Print each word form a text document from a URL

  Args:
    url: the URL of a UTF-8 text document.
  """
  words = fetch_words(url)
  print_items(words)


if __name__ == '__main__':
  # refactored body to a method which could then be tested separately
  main(sys.argv[1])  # 0 is the module filename
