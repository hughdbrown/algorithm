#!/usr/bin/env python
from __future__ import with_statement
import re

def twitterCompress(text):
    def transform(word):
        if word in replacements:
            word = replacements[word]
        elif word.startswith('@'):
            word += ' '
        elif len(word) > (3 + word.count("'")):
            word = word[0] + vowels.sub("", word[1:])
        return word.title()
    vowels = re.compile("[aeiou]")
    replacements = {'the':'da', 'i':'i', 'that':'dat', 'to':'2', 'then':'den'}
    return "".join(transform(word.lower()) for word in text.split(' '))

if __name__ == '__main__':
    import sys
    for arg in sys.argv[1:]:
        with open(arg, "r") as f:
            text = f.read()
            print twitterCompress(text)