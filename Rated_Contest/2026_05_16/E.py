import sys


def solve():
    input_data = sys.stdin.read().split()
    X1 = int(input_data[0])
    X2 = int(input_data[1])
    X3 = int(input_data[2])

    MOD = 998244353

    def build_factorials(n):
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        return fact, inv_fact

    def comb(n, r, fact, inv_fact):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

    gaps = X2 + 1

    A = min(X1, X3)
    B = max(X1, X3)

    max_n = X2 + B + 1
    fact, inv_fact = build_factorials(max_n)

    answer = 0

    for k in range(1, min(A, gaps) + 1):
        a_gaps = comb(gaps, k, fact, inv_fact)

        split_a = comb(A - 1, k - 1, fact, inv_fact)

        place_b = comb(gaps - k + B - 1, B, fact, inv_fact)

        answer += a_gaps * split_a % MOD * place_b
        answer %= MOD

    print(answer)


if __name__ == "__main__":
    solve()
