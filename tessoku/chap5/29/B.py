import sys


def solve():
    input_data = sys.stdin.read().split()
    a = int(input_data[0])
    b = int(input_data[1])
    MOD = 10**9 + 7
    Answer = 1
    p = a
    for i in range(60):
        wari = 2**i
        if (b // wari) % 2 == 1:
            Answer = Answer * p % MOD
        p = (p * p) % MOD
    print(Answer)


if __name__ == "__main__":
    solve()
