import sys


def read_input():
    input_data = sys.stdin.read().split()

    return input_data[0]


def solve():
    S = read_input()
    MOD = 998244353
    n = len(S)

    Answer = 1
    current = 1
    for i in range(1, n):
        if S[i] != S[i - 1]:
            current += 1
        else:
            current = 1
        current %= MOD
        Answer = (Answer + current) % MOD
    print(Answer)


if __name__ == "__main__":
    solve()
