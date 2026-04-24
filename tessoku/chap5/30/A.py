import sys


def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    r = int(input_data[1])
    MOD = 1000000007
    frac = [1] * (n + 1)
    inv_frac = [1] * (n + 1)
    # 階乗を計算
    for i in range(n):
        frac[i + 1] = frac[i] * (i + 1) % MOD
    # 階乗の逆数を計算
    inv_frac[n] = pow(frac[n], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        inv_frac[i] = (inv_frac[i + 1] * (i + 1)) % MOD

    Numerator = frac[n]
    Denominator = inv_frac[r] * inv_frac[n - r] % MOD
    print(Numerator * Denominator % MOD)


if __name__ == "__main__":
    solve()
