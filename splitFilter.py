# https://www.hackerrank.com/challenges/merge-the-tools/problem
from collections import OrderedDict

def splitFilter(string, k):
    for indx in range(0, len(string), k):
        strDict = OrderedDict.fromkeys(list(string[indx:indx+k]))
        print(' '.join(strDict.keys()))

