import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    MOD = 10**9 + 7
    a = [1] * N
    for i in range(2, N):
        a[i] = (a[i - 1] + a[i - 2]) % MOD
    print(a[N - 1])


if __name__ == "__main__":
    solve()
