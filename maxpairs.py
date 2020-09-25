from collections import Counter
import bisect

# Count the numbers of pairs in a list with a minimum difference

ARRAY = False

def maxPairsLeast(arr, minDiff):
    count = Counter(arr)
    ans = [] if ARRAY else 0
    keys = sorted(count.keys())
    for each in keys:
        val = each + minDiff
        if minDiff == 0:
            if not ARRAY:
                ans += int(count[each] * (count[each]-1) / 2)
            else:
                ans += [[(each, each), int(count[each] * (count[each]-1) / 2)]]
            continue
        indx = bisect.bisect_left(keys, val)
        #tmp = keys[indx]
        while count[each] > 0 and indx < len(keys):
            tmp = min(count[each], count[keys[indx]])
            ans += [[(each, each + minDiff), tmp]] if ARRAY else tmp
            count[each] -= tmp
            count[keys[indx]] -= tmp
            indx += 1
    return ans

def maxPairsGreedy(arr, minDiff):
    count = Counter(arr)
    ans = [] if ARRAY else 0
    for each in sorted(count.keys()):
        val = each + minDiff
        if count[each] == 0 or not each + minDiff in count:
            continue
        if minDiff == 0:
            if not ARRAY:
                ans += int(count[each] * (count[each]-1) / 2)
            else:
                ans += [[(each, each), int(count[each] * (count[each]-1) / 2)]]
            continue
        tmp = min(count[each], count[each + minDiff])
        ans += [[(each, each + minDiff), tmp]] if ARRAY else tmp
        count[each] -= tmp
        count[each + minDiff] -= tmp
    return ans

tests = [[[1, 2, 3, 4, 5, 6], 4, 2], [[1, 1, 1, 1], 1, 0], [[3, 4, 5, 2, 1, 1], 3, 2], [[1, 1, 3, 5, 5], 2, 2]]
tests += [[[1, 1, 3, 3, 3, 3, 3, 5, 5, 5, 5], 2, 5], [[1, 1, 1], 0, 3], [[1, 1, 1, 1], 0, 6]]
tests += [[[1, 2, 3, 4, 5], 7, 0], [[1, 3, 5, 3, 1, 5, 3], 2, 3]]
tests += [[[690726610, 893005429, 771998092, 23203911, 732048773, 609897342, 605163057, 492930001, 830083522, 952945114], 763949691, 1]]
tests += [[[709552565, 473251358, 803612259, 579542802, 183012194, 689345248, 151290765, 123232501, 994391793, 25107191, 862726097], 440987423, -1]]
for each in tests:
    result = maxPairsLeast(*each[:-1])
    if ARRAY:
        x = list(zip(*result))
        x = sum(x[1]) if x else 0
        print(each[-1], x, result)
    else:
        print(each[-1], result)
