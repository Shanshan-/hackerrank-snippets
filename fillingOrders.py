def filledOrders(order, k):
    #Greedy Algorithms FTW!!!
    order = sorted(order)
    ans = 0
    count = 0
    for each in order:
        if k - ans < each:
            continue
        ans += each
        count += 1
    return count


test1 = [[10, 30], 40]
test2 = [[5, 4, 6], 3]
test3 = [[21, 24], 831178701]
print(filledOrders(*test1))
print(filledOrders(*test2))
print(filledOrders(*test3))
