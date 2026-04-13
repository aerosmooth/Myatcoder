from re import M
import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    L = [int(x) for x in input_data[1 : 2 * N + 1 : 2]]
    R = [int(x) for x in input_data[2 : 2 * N + 2 : 2]]
    MOD = 998244353
    large_N = 3 * 10**5
    frac = [1] * (large_N + 1)
    invfrac = [1] * (large_N + 1)
    for i in range(1, large_N + 1):
        frac[i] = frac[i - 1] * i % MOD
    invfrac[large_N] = pow(frac[large_N], MOD - 2, MOD)
    for i in range(large_N, 0, -1):
        invfrac[i - 1] = invfrac[i] * i % MOD

    def nCr(n, r):
        return frac[n] * invfrac[r] % MOD * invfrac[n - r] % MOD

    m = [[0, 0], [0, 0]]
    aok = [0] * N
    bok = [0] * N
    cand = [[] for _ in range(N + 2)]

    for i in range(N):
        cand[L[i]].append(i)
        cand[R[i] + 1].append(i)
        cand[N - L[i] + 1].append(i)
        cand[N - R[i]].append(i)

    m[0][0] = N
    ans = 0
    for i in range(1, N + 1):
        for z in cand[i]:
            m[aok[z]][bok[z]] -= 1
            if L[z] <= i <= R[z]:
                aok[z] = 1
            else:
                aok[z] = 0
            if L[z] <= N - i <= R[z]:
                bok[z] = 1
            else:
                bok[z] = 0
            m[aok[z]][bok[z]] += 1

        if m[0][0] == 0 and m[1][0] <= i and m[0][1] <= (N - i):
            ans += nCr(m[1][1], i - m[1][0])
            ans %= MOD

    print(ans)


if __name__ == "__main__":
    solve()
