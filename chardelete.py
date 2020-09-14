from collections import Counter

"""Finding valid strings in Sherlock string question"""

def isValid(s):
    count = dict(Counter(s))
    freq = dict(Counter(count.values()))
    if(len(freq) > 2):
        return "NO"
    if(len(freq) == 1):
        return "YES"
    if(1 in freq.keys() and freq[1] == 1):
        return "YES"
    keys = sorted(freq.keys())
    if(freq[keys[1]] != 1):
        return "NO"
    if(keys[0] + 1 == keys[1]):
        return "YES"
    return "NO"

def run():
    tests = ["aabc", "aaabc", "aabbcd",
         "aabbccddeefghi", "abcdefghhgfedecba"]
    for each in tests:
        print(isValid(each))

run()
