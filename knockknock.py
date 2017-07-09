from __future__ import print_function, division

import random

import re

def make_word_list():
    # make a word list from word textfile
    l = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        l.append(word)

    return l

def read_dictionary(filename='c06d'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

def in_phone():
    # create list of words that are in the phonetic dictionary
    l = []
    for word in word_list:
        if word in phonetic:
            l.append(word)

    return(l)

def knockknock():
    # picks a random 'seed' word
    first = random.choice(shortwords)
    secondlist = []

    for key in phonetic.keys():
        # Use assumption that average syllable length is 3 lettersRr
        if (phonetic[first] == phonetic[key][:len(phonetic[first])]) and ((len(key) - len(first)) > 2):
            secondlist.append(key)

    if len(secondlist) > 0:
        # remove the parenthesis for multiple pronounciations
        secondlist = [re.sub("[\(].*?[\)]", "", x) for x in secondlist]


        print("knock knock")
        print("who's there?")
        print(first)
        print(first + " who?")
        print(random.choice(secondlist))
    else:
        knockknock()

phonetic = read_dictionary()
word_list = make_word_list()
wordphone = in_phone()
shortwords = [i for i in wordphone if len(i) < 7]

knockknock()