import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    Q = int(input_data[1])
    grid = [[0 for _ in range(N)] for _ in range(N)]
    Answer = 0
    for i in range(Q):
        query_id = int(input_data[2 + 2 * i])
        query_num = int(input_data[3 + 2 * i])
        if query_id == 1:
            for j in range(N):
                grid[query_num - 1][j] = 1
        elif query_id == 2:
            for i in range(N):
                grid[i][query_num - 1] = 0

        print(Answer)


if __name__ == "__main__":
    solve()
