import sys


def read_input():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    S = []
    for i in range(N):
        S.append(input_data[1 + i])

    return N, S


def solve():
    N, S = read_input()
    user_name = set()
    for i in range(1, N + 1):
        s = S[i - 1]
        if s not in user_name:
            user_name.add(s)
            print(i)


if __name__ == "__main__":
    solve()
