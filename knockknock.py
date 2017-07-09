from __future__ import print_function, division

from pronounce import read_dictionary

import random

import re

def make_word_list():
    l = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        l.append(word)

    return l

def in_phone():
    # create list of words that are in the phonetic dictionary
    l = []
    for word in word_list:
        if word in phonetic:
            l.append(word)

    return(l)

def knockknock():
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