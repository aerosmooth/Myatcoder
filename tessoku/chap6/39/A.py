import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    A = []
    for i in range(N):
        A.append([int(input_data[1 + 2 * i]), int(input_data[2 + 2 * i])])

    A.sort()
    Answer = 0
    tmp_time = 0
    for i in range(N):
        if A[i][1] >= tmp_time:
            tmp_time = A[i][0]
            Answer += 1
    print(Answer)


if __name__ == "__main__":
    solve()
