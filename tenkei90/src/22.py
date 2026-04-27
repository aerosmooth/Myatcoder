import math
import sys


def solve():
    a, b, c = map(int, sys.stdin.read().split())

    common_edge = math.gcd(a, math.gcd(b, c))
    answer = a // common_edge + b // common_edge + c // common_edge - 3

    print(answer)


if __name__ == "__main__":
    solve()
