'''
https://open.kattis.com/problems/tutorial
'''
import sys
import math


def test():
    assert(solve(999999999, 12, 1)     == 'TLE')
    assert(solve(100000000, 909090, 2) == 'TLE')
    assert(solve(0, 121212, 3)         == 'TLE')
    assert(solve(987654321, 121212, 4) == 'TLE')
    assert(solve(123456789, 121212, 5) == 'TLE')
    assert(solve(1000000, 121212, 6)   == 'TLE')
    assert(solve(100, 121212, 7)       == 'TLE')

    assert(solve(999999999, 10, 1)     == 'AC')
    assert(solve(100000000, 12, 2)     == 'AC')
    assert(solve(12344321, 1, 3)       == 'AC')
    assert(solve(987654321, 10, 4)     == 'AC')
    assert(solve(123456789, 100, 5)    == 'AC')
    assert(solve(1000000, 1000, 6)     == 'AC')
    assert(solve(100, 1, 7)            == 'AC')
    print('Tests passed...')

def solve(m,n,t):
    if(t == 1):
        return 'AC' if(n < 12 and math.factorial(n) <= m) else 'TLE'
    elif(t == 2):
        return 'AC' if(2**n <= m) else 'TLE'
    elif(t == 3):
        return 'AC' if(n**4 <= m) else 'TLE'
    elif(t == 4):
        return 'AC' if(n**3 <= m) else 'TLE'
    elif(t == 5):
        return 'AC' if(n**2 <= m) else 'TLE'
    elif(t == 6):
        return 'AC' if(math.log2(n)*n <= m) else 'TLE'
    elif(t == 7):
        return 'AC' if(n <= m) else 'TLE'

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        m,n,t = [int(x) for x in input().split()]
        print(solve(m,n,t))


