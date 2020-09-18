import sys

def getSize(node, parents, files_size):
    subTree = {node}
    ans = files_size[node]
    for indx, each in enumerate(parents):
        if each in subTree:
            subTree.add(indx)
            ans += files_size[indx]
    return ans


def buildSizeTree(parents, files_sizes, sizesTree):
    tree = {}
    for indx, each in enumerate(parents):
        if each not in tree:
            tree[each] = []
        tree[each] += [indx]
    for each in range(len(files_sizes)-1, -1, -1):
        sizesTree[each] = files_sizes[each]
        if each in tree:
            sizesTree[each] += sum([sizesTree[x] for x in tree[each]])

def mostBalancedPartition(parent, files_size):
    minDiff = sys.maxsize
    sizeTree = [0] * len(parent)
    buildSizeTree(parent, files_size, sizeTree)
    maxSize = sizeTree[0]
    #TODO: this can almost certiainly be improved via DP
    for indx in range(len(parent) - 1):
        tmp = parent[indx+1]
        parent[indx+1] = -1
        y = sizeTree[indx+1]
        minDiff = abs(maxSize-2*y) if abs(maxSize-2*y) < minDiff else minDiff
        if minDiff == 0:
            return 0
        parent[indx+1] = tmp
    return minDiff

def mostBalancedPartitionv2(parent, files_size):
    minDiff = sys.maxsize
    maxSize = getSize(0, parent, files_size)
    #TODO: this can almost certiainly be improved via DP
    for indx in range(len(parent) - 1):
        tmp = parent[indx+1]
        parent[indx+1] = -1
        y = getSize(indx+1, parent, files_size)
        minDiff = abs(maxSize-2*y) if abs(maxSize-2*y) < minDiff else minDiff
        if minDiff == 0:
            return 0
        parent[indx+1] = tmp
    return minDiff


def mostBalancedPartitionv1(parent, files_size):
    minDiff = sys.maxsize
    print(getSize(0, parent, files_size))
    #TODO: this can almost certiainly be improved via DP
    for indx in range(len(parent) - 1):
        tmp = parent[indx+1]
        parent[indx+1] = -1
        x = getSize(0, parent, files_size)
        y = getSize(indx+1, parent, files_size)
        minDiff = abs(x-y) if abs(x-y) < minDiff else minDiff
        if minDiff == 0:
            return 0
        parent[indx+1] = tmp
    return minDiff


test1 = [[-1, 0, 1, 2], [1, 4, 3, 4]]
print(mostBalancedPartition(*test1))
test2 = [[-1, 0, 0, 1, 1, 2], [1, 2, 2, 1, 1, 1]]
print(mostBalancedPartition(*test2))
