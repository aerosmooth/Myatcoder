import sys


def read_input():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    C = []
    P = []
    for i in range(N):
        start = 1
        C.append(int(input_data[start + 2 * i]))
        P.append(int(input_data[start + 2 * i + 1]))
    Q = int(input_data[1 + 2 * N])
    L = []
    R = []
    for i in range(Q):
        start = 2 + 2 * N
        L.append(int(input_data[start + 2 * i]))
        R.append(int(input_data[start + 2 * i + 1]))

    return N, C, P, Q, L, R


def set_dict(
    N: int, C: list[int], P: list[int]
) -> tuple[dict[int, int], dict[int, int]]:
    score_1 = {}
    score_2 = {}
    for i in range(N):
        if C[i] == 1:
            score_1[i + 1] = P[i]
        elif C[i] == 2:
            score_2[i + 1] = P[i]
    return score_1, score_2


def calculate_accumlate_sum(score_dict: dict[int, int], N: int) -> list[int]:
    acc_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        acc_sum[i] += acc_sum[i - 1] + score_dict.get(i, 0)
    return acc_sum


def answer_query(acc_sum: list[int], L: int, R: int) -> int:
    Answer = acc_sum[R] - acc_sum[L - 1]
    return Answer


def solve():
    N, C, P, Q, L, R = read_input()
    score_1, score_2 = set_dict(N, C, P)
    acc_sum1 = calculate_accumlate_sum(score_1, N)
    acc_sum2 = calculate_accumlate_sum(score_2, N)

    for i in range(Q):
        A = answer_query(acc_sum1, L[i], R[i])
        B = answer_query(acc_sum2, L[i], R[i])
        print(A, B)


if __name__ == "__main__":
    solve()
