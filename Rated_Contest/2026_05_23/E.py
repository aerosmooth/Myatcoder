import sys
from collections import deque


def solve():
    input_data = sys.stdin.read().split()

    N = int(input_data[0])
    MOD = 998244353

    P = [0, 0] + [int(x) for x in input_data[1:N]]
    C = [0] + [int(x) for x in input_data[N : 2 * N]]
    D = [0] + [int(x) for x in input_data[2 * N : 3 * N]]

    children = [[] for _ in range(N + 1)]
    for i in range(2, N + 1):
        children[P[i]].append(i)

    order = []
    queue = deque([1])
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in children[u]:
            queue.append(v)

    C_cpy = C.copy()
    D_cpy = D.copy()

    def nCk(n, k):
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        k = min(k, n - k)
        num = 1
        den = 1
        for i in range(k):
            num = (num * (n - i)) % MOD
            den = (den * (i + 1)) % MOD
        return (num * pow(den, MOD - 2, MOD)) % MOD

    ans = 1
    for u in reversed(order):
        for v in children[u]:
            C_cpy[u] += C_cpy[v]
            D_cpy[u] += D_cpy[v]

        if C_cpy[u] < D_cpy[u]:
            print(0)
            return

        tmp = nCk(C_cpy[u] - D_cpy[u] + D[u], D[u]) % MOD
        ans = ans * tmp % MOD

    print(ans)


if __name__ == "__main__":
    solve()
