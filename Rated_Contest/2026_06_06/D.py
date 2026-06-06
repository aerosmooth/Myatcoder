import sys
from collections import defaultdict


def solve():
    input_data = sys.stdin.read().split()
    H = int(input_data[0])
    W = int(input_data[1])
    K = int(input_data[2])
    S = []
    for i in range(H):
        S.append(input_data[3 + i])
    sum_S = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
    for i in range(1, 1 + H):
        for j in range(1, 1 + W):
            sum_S[i][j] = sum_S[i][j - 1] + int(S[i - 1][j - 1])
    for j in range(1, 1 + W):
        for i in range(1, 1 + H):
            sum_S[i][j] += sum_S[i - 1][j]
    Answer = 0
    for rup in range(1, H + 1):
        for rdown in range(rup, H + 1):
            count = defaultdict(int)
            count[0] = 1
            for c in range(1, W + 1):
                current_sum = sum_S[rdown][c] - sum_S[rup - 1][c]
                remain = current_sum - K

                if remain in count:
                    Answer += count[remain]

                count[current_sum] += 1

    print(Answer)


if __name__ == "__main__":
    solve()
