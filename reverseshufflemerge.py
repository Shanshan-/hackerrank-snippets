"""
NOTES:
- length of the minStr will always be 1/2 length of orig string
- minStr will be some permutation of all the letters in the orig string / 2
- potential bruteforce/greedy: get permutations of minStr in order, then 
    check if present in rev(string)
    If present, then that will be solution
    - NOPE: string generation includes a merge step
- merge(reverse(A), shuffle(A))
    - modify the "in" check
"""
from collections import Counter
from itertools import permutations

def inStr(substr, string):
    for letter in substr:
        indx = string.find(letter)
        if(indx == -1):
            return False
        string = string[indx+1:]
    return True

def rsm(string):
    fullCt = dict(Counter(string))
    halfStr = ""#[]
    halfCt = dict()
    for key, val in fullCt.items():
        halfStr += key * (val // 2)
        #halfStr += [key] * (val // 2)
        halfCt[key] = val // 2
    halfStr = ''.join(sorted(halfStr))
    #halfStr.sort()
    ans = ""
    bound = halfStr[0]
    while(fullCt[bound] == halfCt[bound]):
        indx = halfStr.rfind(letter)
        if(indx == len(halfStr)-1 or indx == -1):
            bound = "~"
            break
        if(fullCt[halfStr[indx+1]] == halfCt[halfStr[indx+1]]):
            bound = halfStr[indx+1]
        else:
            break
    for letter in string[::-1]:
        a = letter <= bound and letter in halfStr
        b = fullCt[letter] == halfCt[letter]
        if(a or b):
            indx = halfStr.find(letter)
            halfStr = halfStr[:indx] + halfStr[indx+1:]
            #halfStr.remove(letter)
            halfCt[letter] -= 1
            ans += letter
        fullCt[letter] -= 1
        if(not halfStr):
            break
        if(letter == bound):
            bound = halfStr[0]
            while(fullCt[bound] == halfCt[bound]):
                indx = halfStr.rfind(bound)
                if(indx == len(halfStr)-1 or indx == -1):
                    bound = "~"
                    break
                if(fullCt[halfStr[indx+1]] == halfCt[halfStr[indx+1]]):
                    bound = halfStr[indx+1]
                else:
                    break
    return ans

def rsm1(string):
    string = string[::-1]
    #generate the string to permute
    # # Using Counter
    # tmp = dict(Counter(string))
    # halfStr = ""
    # for key, val in tmp.items():
    #     halfStr += key * (val // 2)
    # # Using set
    # tmp = set()
    # halfStr = ""
    # for letter in string:
    #     if letter in tmp:
    #         tmp.remove(letter)
    #         halfStr += letter
    #     else:
    #         tmp.add(letter)
    # Using sorting
    halfStr = sorted(string)[::2]
    
    #Permuting using library
    permutes = list(set(permutations(halfStr)))
    for each in sorted(permutes):
        if(inStr(each, string)):
            return ''.join(each)
    return ""

def rsm2(string):
    string = string[::-1]
    length = len(string) // 2
    start = min(string)
    minInd = string.index(start)
    minStr = string[minInd:minInd+length][::-1]
    lastInd = minInd
    while(True):
        try:
            nextInd = lastInd + string[lastInd+1:].index(start) + 1
        except:
            break
        nextStr = string[nextInd:nextInd+length][::-1]
        if len(nextStr) < length:
            break
        if nextStr < minStr:
            minInd = nextInd
            minStr = nextStr
        lastInd = nextInd
    return minStr[::-1]

def run():
    tests = ["eggegg", "abcdefgabcdefg", "aeiouuoiea", "adbcdbca", "acbdcbda", "acbcdbda",
             "bdabaceadaedaaaeaecdeadababdbeaeeacacaba", "aabcggbbcbaa",
             "djjcddjggbiigjhfghehhbgdigjicafgjcehhfgifadihiajgciagicdahcbajjbhifjiaajigdgdfhdiijjgaiejgegbbiigida"]
    ans = ["egg", "agfedcb", "aeiou", "abcd", "abcd", "abdc", "aaaaaabaaceededecbdb",
           "aabcbg", "aaaaabccigicgjihidfiejfijgidgbhhehgfhjgiibggjddjjd"]
             
    for query, ans in zip(tests, ans):
        result = rsm(query)
        if(result == ans):
            print("True:\t", result)
        else:
            print("False:\t", result, "\n\t", ans)