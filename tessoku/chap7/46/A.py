import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    X = []
    Y = []
    for i in range(N):
        X.append(int(input_data[1 + 2 * i]))
        Y.append(int(input_data[2 + 2 * i]))

    # 都市iと都市jの距離を計算する
    def calculate_distance(i: int, j: int):
        unrooted_dist = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
        return unrooted_dist**0.5

    reached = [False] * N
    reached[0] = True

    Answer = [0]
    for _ in range(N - 1):
        current_city = Answer[-1]
        min_dist = float("inf")
        min_j = None
        for j in range(N):
            if not reached[j]:
                ij_dist = calculate_distance(current_city, j)
                if min_dist > ij_dist:
                    min_j = j
                    min_dist = ij_dist

        Answer.append(min_j)
        reached[min_j] = True
    for city in Answer:
        print(city + 1)
    print(1)


if __name__ == "__main__":
    solve()
