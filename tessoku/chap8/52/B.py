import sys
from collections import deque


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    X = int(input_data[1])
    A = list(input_data[2])

    queue = deque()

    queue.append(X)
    A[X - 1] = "@"

    while queue:
        q = queue.popleft()
        if q > 1 and A[q - 2] == ".":
            A[q - 2] = "@"
            queue.append(q - 1)
        if q < N and A[q] == ".":
            A[q] = "@"
            queue.append(q + 1)

    print("".join(A))


if __name__ == "__main__":
    solve()
