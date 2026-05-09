import sys


def read_input():
    input_data = sys.stdin.read().split()
    A = []
    for i in range(3):
        B = [int(x) for x in input_data[6 * i : 6 * i + 6]]
        A.append(B)

    return A


def solve():
    A = read_input()
    prob_1 = [0] * 6
    prob_2 = [0] * 6
    prob_3 = [0] * 6
    for i in range(6):
        prob_1[A[0][i] - 1] += 1 / 6
    for i in range(6):
        prob_2[A[1][i] - 1] += 1 / 6
    for i in range(6):
        prob_3[A[2][i] - 1] += 1 / 6

    Answer = (
        prob_1[3] * prob_2[4] * prob_3[5]
        + prob_1[3] * prob_2[5] * prob_3[4]
        + prob_1[4] * prob_2[3] * prob_3[5]
        + prob_1[4] * prob_2[5] * prob_3[3]
        + prob_1[5] * prob_2[3] * prob_3[4]
        + prob_1[5] * prob_2[4] * prob_3[3]
    )
    print(Answer)


if __name__ == "__main__":
    solve()
