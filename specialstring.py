from collections import Counter

"""Count the number of total special substrings
    in a given string, given special substrings
    are either all the samme letter, or only the
    middle character is different"""

spTrack = {}

def isSpecial(s):
    n = len(s)
    if(n == 1):
        return True
    count = dict(Counter(s))
    if(len(count) == 1):
        return True
    if(not n % 2):
        return False
    if(len(count) > 2):
        return False
    if(1 not in count.values()):
        return False
    if(s[n // 2 + 1] == s[1]):
        return False
    return True

def substrCount1(n, s):
    #brute force
    # substr = [s[x:y] for x, y in combinations(range(n+1), r=2) if isSpecial(s[x:y])]
    # return len(substr)
    
    #slight DP
    count = n
    for run in range(2, n+1):
        for start in range(0, n-run+1):
            substr = s[start:start+run]
            if(substr in spTrack):
                count += 1 if spTrack[substr] else 0
            else:
                special = isSpecial(substr)
                count += 1 if(special) else 0
                spTrack[substr] = special
            #print(run, count, s[start:start+run])
    return count

def substrCount(n, s):
    #squash the input string
    ans = 0
    count = 1
    curLetter = s[0]
    squash = []
    for x in s[1:]:
        if(x == curLetter):
            count += 1
            continue
        squash.append((curLetter, count))
        curLetter = x
        count = 1
    squash.append((curLetter, count))
    
    #parse the squash to add runs
    for each in squash:
        ans += (each[1]) * (each[1]+1) // 2
        #NOT "-1" because of counting
    
    #parse the squash to find sandwiches
    for x in range(len(squash) - 2):
        if(squash[x][0] != squash[x+2][0]):
            continue
        if(squash[x+1][1] != 1):
            continue
        ans += min(squash[x][1], squash[x+2][1])
    
    return ans

def run():
    testSp = ["a", "aba", "aa", "bbb", "aabb", "monop", "nonon", "nonop"]
    testSub = ["aaaa", "bbb", "asasd", "abcbaba", "aaaa"] 
    """longStr = "ccacacabccacabaaaabbcbccbabcbbcaccabaababcbcacabcaba"
              "cbbbccccabcbcabbaaaaabacbcbbbcababaabcbbaaababababba"
              "bcaabcaacacbbaccbbabbcbbcbacbacabaaaaccacbaabccabbac"
              "abaabaaaabbccbaaaabacabcacbbabbacbcbccbbbaaabaaacaab"
              "acccaacbcccaacbbcaabcbbccbccacbbcbcaaabbaababacccbac"
              "acbcbcbbccaacbbacbcbaaaacaccbcaaacbbcbbabaaacbaccacc"
              "bbabbcccbcbcbcbcabbccbacccbacabcaacbcaccabbacbbcccca"
              "abbacccaacbbbacbccbcaaaaaabaacaaabccbbcccaacbacbccaa"
              "acaacaaaacbbaaccacbcbaaaccaabcbccacaaccccacaacbcaccc"
              "bcababcabacaabbcacccbacbbaaaccabbabaaccabbcbbcaabbca"
              "baacabacbcabbaaabccabcacbcbabcbccbabcabbbcbacaaacaab"
              "bbabbaacbbacaccccabbabcbcabababbcbaaacbaacbacacbabbc"
              "acccbccbbbcbcabcabbbcaabbaccccabaabbcbcccabaacccccaa"
              "acbbbcbcacacbabaccccbcbabacaaaabcccaaccacbcbbcccaacc"
              "cbbcaaaccccaabacabcabbccaababbcabccbcaccccbaaabbbcba"
              "baccacaabcabcbacaccbaccbbaabccbbbccaccabccbabbbccbaa"
              "bcaabcabcbbabccbaaccabaacbbaaaabcbcabaacacbcaabbaaab"
              "aaccacbaacababcbacbaacacccacaacbacbbaacbcbbbabccbaba"
              "bcbcccbccbcacccbababbcacaaaaacbabcabcacaccabaabcaaaa"
              "cacbccccaaccbcbccaccacbcaaababaacbccbbbabccbaababcaa"
              "baaabcbaacccaccbcccccbabbbbacbaacbcaaaabbccbbbbbacca"
              "bcabcbcbbcbcbbbabcacbabbabbaabaabbccbbaabbbaacacacac"
              "bcccbcbbccaaaabaaabccaccbbabccabbabccabaaabcabcbabba"
              "bcbccabcbababccbcabaacaaccaacaccacaaccbbbabccbacbaba"
              "bbacbaccbbbcabbcaabcabbcabacbaccaaaaaacaabaaacbbcbcb"
              "abacaaaaaaaacabccacbcbcbbcccbbcbacccaccbbcbccaaccaca"
              "acbacccbcbaccccccbcaccbbbababbbbacaacabbbbcaacacabac"
              "abbcaacbcbbbabbccbcaaabcbbacccaaccbabcbabcbcccccbbaa"
              "bbabccabcacacaccbaaacaaaaabacccbbaacacaaaacbcccbabcb"
              "cbbbccbcbbacabcbcaaabbaaacbcbcaacccabbcbcaaabacaaaab"
              "babbbaaccbccbabccbbabbbbbabbbbaccaaaaacbacccacbcccca"""

    for each in testSub:
        #print(isSpecial(each))
        print(substrCount(len(each), each))
