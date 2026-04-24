import sys


def solve():
    input_data = sys.stdin.read().split()
    H = int(input_data[0])
    W = int(input_data[1])
    MOD = 10**9 + 7
    frac = [1] * (H + W - 1)
    inv_frac = [1] * (H + W - 1)
    for i in range(1, H + W - 1):
        frac[i] = frac[i - 1] * i % MOD
    inv_frac[H + W - 2] = pow(frac[H + W - 2], MOD - 2, MOD)
    for j in range(H + W - 3, -1, -1):
        inv_frac[j] = inv_frac[j + 1] * (j + 1) % MOD

    def nCr(n, r):
        return (frac[n] * inv_frac[r] * inv_frac[n - r]) % MOD

    print(nCr(H + W - 2, H - 1))


if __name__ == "__main__":
    solve()
