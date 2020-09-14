def oneCycle(m, w, p, n):
    cycles = 0
    inv = 0
    while inv < n:
        inv += m*w
        # determine how many machines and workers to buy

    return cycles

def run():
    # link: https://www.hackerrank.com/challenges/making-candies/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
    testCases = [["3 1 2 12", 3]]
    for ln1, sol in testCases[:]:
        numMach, numWork, cost, goal = [int(x) for x in str.split(ln1, " ")]
        print("goal", ":", goal)
        f = oneCycle
        tmp = f(numMach, numWork, cost, goal)
        print("CORRECT") if sol == tmp else print("WRONG: solution -", sol, "ans -", tmp)

run()