from collections import Counter
from copy import deepcopy

def builtinSort(arr, mux=0):
    mux = 2
    if mux == 0:
        return sorted(arr)
    keys = deepcopy(list(arr))
    if mux == 1: #bubble sort
        swapped = True
        while swapped:
            swapped = False
            for indx in range(1, len(keys)):
                if keys[indx] < keys[indx - 1]:
                    keys[indx], keys[indx-1] = keys[indx-1], keys[indx]
                    swapped = True
        return keys
    if mux == 2: #insertion sort
        for indx in range(1, len(keys)):
            x = indx
            while x > 0:
                if keys[x] < keys[x - 1]:
                    keys[x], keys[x-1] = keys[x-1], keys[x]
                x -= 1
        return keys
    if mux == 3: #selection sort
        return keys


def countPairs(diff, numbers): #makes use of Counter library and built-in sorting
    count = Counter(numbers)
    ans = 0
    for key in count.keys():#builtinSort(count.keys()):
        if key + diff in count:
            ans += min(count[key], count[key+diff])
    return ans

def run():
    # link: https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
    testCases = [["5 2", "1 5 3 4 2", 3], ["7 2", "1 3 5 8 6 4 2", 5], ["5 2", "5 4 3 2 1", 3],
                 ["10 1", "363374326 364147530 61825163 1073065718 1281246024 1399469912 428047635 491595254 879792181 1069262793", 0]]
    for ln1, ln2, sol in testCases[:]:
        nums = [int(x) for x in str.split(ln2, " ")]
        difference = int(str.split(ln1, " ")[1])
        print(difference, ":", nums[:20])
        f = countPairs
        tmp = f(difference, nums)
        print("CORRECT") if sol == tmp else print("WRONG: solution -", sol, "ans -", tmp)

run()
