import sys
from collections import deque


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i] = int(input_data[1 + 2 * i])
        R[i] = int(input_data[2 + 2 * i])
    DIVISOR = 998244353
    # 循環的な問題だから、k固定したらいける？
    # 線分で考えればいけそうかも
    # Aチームにk人、BチームにN-k人入ると仮定する
    # ある選手iに関して、L[i] <= k <= R[i]ならAに所属できる。N - R[i] <= k <= N - L[i]ならAに所属できる
    # or_people[k]はAまたはBに所属できる
    # A_people[k]はAに所属できる
    # ans_people[k]は両方に所属できる
    # もしor_people[k] != Nならそのkにおいては0
    # もしor_people[k] == Nなら二こう係数でnCk、nはans_people[k]でkはk - (A_people[k] - ans_people[k])になる
    # こいつらを足せば良い
    fact = [1] * (N + 1)
    inv = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = (fact[i - 1] * i) % DIVISOR
    inv[N] = pow(fact[N], DIVISOR - 2, DIVISOR)
    for i in range(N - 1, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % DIVISOR

    def nCr(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv[r] % DIVISOR * inv[n - r] % DIVISOR

    # 差分の箇所だけ記録して、あとで加算する
    diff_or = [0] * (N + 2)
    diff_A = [0] * (N + 2)
    diff_ans = [0] * (N + 2)

    for i in range(1, N + 1):
        a_start, a_end = L[i - 1], R[i - 1]
        b_start, b_end = N - R[i - 1], N - L[i - 1]

        diff_A[a_start] += 1
        diff_A[a_end + 1] -= 1

        # これで共通する部分をとってこれる
        start = max(a_start, b_start)
        end = min(a_end, b_end)

        if start <= end:
            diff_ans[start] += 1
            diff_ans[end + 1] -= 1

            # これでまたはの部分する部分をとってこれる
            or_start = min(a_start, b_start)
            or_end = max(a_end, b_end)

            diff_or[or_start] += 1
            diff_or[or_end + 1] -= 1
        else:
            diff_or[a_start] += 1
            diff_or[a_end + 1] -= 1
            diff_or[b_start] += 1
            diff_or[b_end + 1] -= 1

    ans = 0
    or_count = 0
    A_count = 0
    ans_count = 0

    for k in range(1, N):
        or_count += diff_or[k]
        A_count += diff_A[k]
        ans_count += diff_ans[k]

        if or_count == N:
            ans = (ans + nCr(ans_count, k - A_count + ans_count)) % DIVISOR
    print(ans)


if __name__ == "__main__":
    solve()
