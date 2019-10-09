'''
https://open.kattis.com/problems/putovanje
'''
import sys

def solve(stomach_size, food_found):
    b = 0
    for i in range(len(food_found)):
        m, t = [0, 0]
        for j in range(len(food_found)-i):
            if(t + food_found[j+i] <= stomach_size):
                t += food_found[j+i]
                m += 1
        b = max(b, m)
    return b


def test():
    a1 = 5
    v1 = [3, 1, 2, 1, 1]
    a2 = 5
    v2 = [1, 5, 4, 3, 2, 1, 1]
    a3 = 10
    v3 = [3, 2, 5, 4, 3]

    assert(solve(a1, v1) == 4)
    assert(solve(a2, v2) == 3)
    assert(solve(a3, v3) == 3)
    print("Tested. All passed...")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        num_of_food, stomach_size = [int(x) for x in input().split()]
        food_found = [int(x) for x in input().split()]
        print(solve(stomach_size, food_found))
