import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    A = []
    B = []
    ox = {}
    for i in range(N):
        A.append(int(input_data[1 + i]))
        ox[A[i]] = i + 1
    for i in range(N):
        B.append(int(input_data[1 + N + i]))
        if ox[i + 1] != B[i]:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    solve()
