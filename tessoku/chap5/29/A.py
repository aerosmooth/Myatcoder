import sys


def solve():
    input_data = sys.stdin.read().split()
    a = int(input_data[0])
    b = int(input_data[1])
    MOD = 10**9 + 7
    ans = 1
    p = a
    for i in range(30):
        wari = 2**i
        if (b // wari) % 2 == 1:
            ans = (ans * p) % MOD
        p = (p * p) % MOD
    print(ans)


if __name__ == "__main__":
    solve()
