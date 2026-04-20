import sys
from collections import deque


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    M = int(input_data[1])
    A = []
    B = []
    for i in range(M):
        A.append(int(input_data[2 + 2 * i]))
        B.append(int(input_data[3 + 2 * i]))

    can_get = [[] for _ in range(N + 1)]

    for i in range(M):
        can_get[A[i]].append(B[i])

    queue = deque()
    d = [False] * N
    queue.append(0)
    d[0] = True
    while queue:
        x = queue.popleft()
        for i in can_get[x + 1]:
            if d[i - 1]:
                continue
            queue.append(i - 1)
            d[i - 1] = True
    print(d.count(True))


if __name__ == "__main__":
    solve()
