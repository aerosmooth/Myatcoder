import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    A = []
    for i in range(N):
        A.append(int(input_data[1 + i]))

    cnt = [0] * 100
    for i in range(N):
        cnt[A[i] - 1] += 1
    Answer = 0
    for i in range(100):
        count = cnt[i]
        if count >= 3:
            Answer += count * (count - 1) * (count - 2) / 6

    print(int(Answer))


if __name__ == "__main__":
    solve()
