import math, os, sys
from collections import Counter
from itertools import combinations
from math import factorial

def func1(arr, r):
    chances = len([x for x in combinations(arr, r) if "a" in x])
    f = factorial
    total = f(len(arr)) / f(r) / f(len(arr)-r)
    return chances / total

def func2()

tests = [[4, "a a b c", 2, 0.833]]#, [int(input()), input().split(" "), int(input()), ""]]
for numElements, array, choicesMade, result in tests:
    f = func1
    print(result, f(array.split(" "), choicesMade))