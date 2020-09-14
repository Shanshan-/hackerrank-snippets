""" Counting Inversions via Merge Sort"""

def merge(arr1, arr2, len1, len2):
    ans = []
    indx1, indx2, swaps = 0, 0, 0
    if(len1 == 0):
        return arr2
    if(len2 == 0):
        return arr1
    while(indx1 < len1 and indx2 < len2):
        if(arr1[indx1] <= arr2[indx2]):
            ans.append(arr1[indx1])
            indx1 += 1
        else:
            ans.append(arr2[indx2])
            indx2 += 1
            swaps += len1-indx1
    if(indx1 < len1):
        for x in range(indx1, len1):
            ans.append(arr1[x])
            #swaps += 1
    elif(indx2 < len2): 
        for x in range(indx2, len2): 
            ans.append(arr2[x]) 
    return swaps, ans
    
def mergeSort(arr, left, right):
    mid = (left+right)//2
    if(right-left <= 1):
        return 0, arr
    swaps1, part1 = mergeSort(arr[left:mid], 0, mid-left)
    swaps2, part2 = mergeSort(arr[mid:right], 0, right-mid)
    swaps, ans = merge(part1, part2, mid-left, right-mid)
    return swaps1 + swaps2 + swaps, ans
    
def run():
    tests = [[1, 1, 1, 2, 2], [2, 1, 3, 1, 2],
             [1, 5, 3, 7], [7, 5, 3, 1]]
             
    for each in tests:
        print(mergeSort(each, 0, len(each)))

