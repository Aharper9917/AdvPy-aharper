'''
https://open.kattis.com/problems/icpcteamselection
'''
import sys

def test():
    assert(solve([9, 8, 10, 9, 6, 8], 2) == 17)
    assert(solve([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == 18)
    assert(solve([1, 100, 51], 1) == 51)
    assert(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3], 4) == 21)
    print("All Tests Passed...")

def solve(scores, numOfTeams):
    scores.sort(reverse=True)
    total = 0
    for i in range(numOfTeams):
        total += scores[i*2+1]
        # # wrong solution...
        # team = []
        # for member in range(3):
        #     score = scores.pop(0)
        #     team.append(score)
        # team.sort()
        # total += team[1]
    return(total)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        for i in range(int(input())):
            numOfTeams = int(input())
            scores = [int(num) for num in input().split()]
            print(solve(scores, numOfTeams))


'''
for i in range(int(input())):
    numOfTeams = int(input())
    scores = [int(num) for num in input().split()]
    scores.sort(reverse = True)
    # print(scores)

    total = 0
    for i in range(numOfTeams):
        total += scores[i*2+1]
        # team = []
        # for member in range(3):
        #     score = scores.pop(0)
        #     team.append(score)
        # team.sort()
        # total += team[1]


    print(total)
'''
