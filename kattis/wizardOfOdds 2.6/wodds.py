'''
https://open.kattis.com/problems/wizardofodds
'''

import math
import sys


def solve(x):
    if(math.log(x[0], 2) <= x[1]):
        return('Your wish is granted!')
    else:
        return('You will become a flying monkey!')


def test():
    assert(solve([8, 3]) == 'Your wish is granted!')
    assert(solve([44, 6]) == 'Your wish is granted!')
    assert(solve([1234567890, 3]) == 'You will become a flying monkey!')
    print('All tests passed...')


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        x = [float(i) for i in input().split()]
        print(solve(x))
