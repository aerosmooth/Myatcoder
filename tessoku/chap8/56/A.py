import sys


def read_input():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    Q = int(input_data[1])
    S = input_data[2]
    a = []
    b = []
    c = []
    d = []
    for i in range(Q):
        start = 3 + 4 * i
        a.append(int(input_data[start]))
        b.append(int(input_data[start + 1]))
        c.append(int(input_data[start + 2]))
        d.append(int(input_data[start + 3]))

    return N, Q, S, a, b, c, d


def solve():
    N, Q, S, a, b, c, d = read_input()
    T = list(map(lambda c: ord(c) - ord("a") + 1, S))

    MOD = 2147483647
    power100 = [None] * (N + 1)
    power100[0] = 1
    for i in range(1, N + 1):
        power100[i] = power100[i - 1] * 100 % MOD

    H = [None] * (N + 1)
    H[0] = 0
    for i in range(N):
        H[i + 1] = (H[i] * 100 + T[i]) % MOD

    def hash_value(l, r):
        return (H[r] - H[l - 1] * power100[r - l + 1]) % MOD

    for i in range(Q):
        A = a[i]
        B = b[i]
        C = c[i]
        D = d[i]

        if hash_value(A, B) == hash_value(C, D):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    solve()
