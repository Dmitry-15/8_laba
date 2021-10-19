#!/usr/bin/env python3
# -*- coding: utf-8 -*-

words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four'
}
dict_items = words.items()
new_words = dict(zip(words.values(), words.keys()))
print(new_words)







