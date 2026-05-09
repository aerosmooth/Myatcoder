import sys
from collections import deque


def solve():
    Q = int(input())
    queries = [input().split() for _ in range(Q)]

    T = deque()
    for q in queries:
        if q[0] == "1":
            T.append(q[1])
        elif q[0] == "2":
            print(T[0])
        elif q[0] == "3":
            T.popleft()


if __name__ == "__main__":
    solve()
