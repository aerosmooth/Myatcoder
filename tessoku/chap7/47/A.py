import sys
import random


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    X = []
    Y = []
    for i in range(N):
        X.append(int(input_data[1 + 2 * i]))
        Y.append(int(input_data[2 + 2 * i]))
    NUM_LOOPS = 40000
    P = [i % N for i in range(N + 1)]

    def calculate_distance(i: int, j: int):
        unrooted_dist = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
        return unrooted_dist**0.5

    def get_score(P: list):
        Answer_score = 0
        for i in range(N):
            Answer_score += calculate_distance(P[i] % N, P[i + 1] % N)
        return Answer_score

    current_score = get_score(P)
    for i in range(NUM_LOOPS):
        l = random.randint(1, N - 1)
        r = random.randint(1, N - 1)
        if l > r:
            l, r = r, l
        P[l : r + 1] = reversed(P[l : r + 1])
        new_score = get_score(P)
        if new_score <= current_score:
            current_score = new_score
        else:
            P[l : r + 1] = reversed(P[l : r + 1])

    for i in P:
        print(i + 1)


if __name__ == "__main__":
    solve()
