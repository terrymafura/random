#!/usr/bin/python

import random

def generate_random_nums():
    numbers = list(range(1, 11))
    random.shuffle(numbers)
    for num in numbers:
        print(num)

if __name__ == '__main__':
    generate_random_nums()