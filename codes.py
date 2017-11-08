#!/usr/bin/env python3

from itertools import product
import random
import sys

def get_words(filename):
    with open(filename, 'r') as f:
        words = [word.strip() for word in f.readlines()]
    word_lists = list()
    word_lists.append(list())
    for word in words:
        if word == '':
            word_lists.append(list())
        else:
            word_lists[-1].append(word)
    return word_lists

def generate_codes(word_lists, seed=None):
    random.seed(seed)
    codes = list()
    components = product(*word_lists)
    for c in components:
        codes.append('{}-{}'.format('-'.join(c), random.randint(100,1000)))
    random.shuffle(codes)
    return codes

if __name__ == '__main__':
    seed = None
    if len(sys.argv) > 2:
        seed = int(sys.argv[2])
    word_lists = get_words(sys.argv[1])
    codes = generate_codes(word_lists, seed)
    for code in codes:
        print(code)
