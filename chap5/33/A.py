import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    A = list(map(int, input_data[1 : N + 1]))

    A_or_sum = A[0]
    for i in range(1, N):
        A_or_sum = A_or_sum ^ A[i]
    if A_or_sum:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    solve()
