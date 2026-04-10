import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        exit()
    N = int(input_data[0])
    M = int(input_data[1])
    A = [int(x) for x in input_data[2 : N + 2]]
    B = [int(x) for x in input_data[N + 2 :]]
    DEVISOR = 998244353
    # i mod j = i - j [i/j]
    ruiseki_A = [0] * (N + 1)
    for i in range(N):
        ruiseki_A[i + 1] = (ruiseki_A[i] + A[i]) % DEVISOR
    sum_A_i = 0
    for i in range(1, N + 1):
        sum_A_i = (sum_A_i + (A[i - 1] % DEVISOR) * i) % DEVISOR
    sum_B = 0
    for j in range(1, M + 1):
        sum_B = (sum_B + B[j - 1]) % DEVISOR
    ans_1 = (sum_A_i * sum_B) % DEVISOR

    ans_2 = 0
    limit = min(N, M)
    for j in range(1, limit + 1):
        term = 0
        for k in range(1, N // j + 1):
            L = k * j
            R = (k + 1) * j - 1
            if R > N:
                R = N
            sum_A = ruiseki_A[R] - ruiseki_A[L - 1]
            term += k * sum_A
        ans_2 = (ans_2 + term * (B[j - 1] % DEVISOR) * (j % DEVISOR)) % DEVISOR
    ans = (ans_1 - ans_2) % DEVISOR
    ans = (ans + DEVISOR) % DEVISOR
    print(ans)


if __name__ == "__main__":
    solve()
