import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    K = int(input_data[1])
    A = []
    for i in range(N):
        A.append(int(input_data[2 + i]))

    # 1 累積和を計算する
    sum_A = [0] * (N + 1)
    for i in range(1, N + 1):
        sum_A[i] = sum_A[i - 1] + A[i - 1]

    # A[l]からA[r]までの和を計算する
    def sum_l_r(l, r, S):
        return S[r + 1] - S[l]

    # 2 左端iで、右端をどこまで許容できるかを計算する
    R = [0] * N
    for i in range(N):
        if i == 0:
            R[i] = -1
        else:
            R[i] = R[i - 1]
        while R[i] < N - 1 and sum_l_r(i, R[i] + 1, sum_A) <= K:
            R[i] += 1
    Answer = 0
    for i in range(N):
        Answer += R[i] - i + 1
    print(Answer)


if __name__ == "__main__":
    solve()
