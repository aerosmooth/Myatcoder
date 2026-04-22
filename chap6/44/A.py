import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    Q = int(input_data[1])
    A = [i + 1 for i in range(N)]
    index = 2
    reverse = False
    for i in range(Q):
        q = int(input_data[index])
        index += 1
        if q == 1:
            x = int(input_data[index])
            index += 1
            y = int(input_data[index])
            index += 1
            if reverse:
                A[N - x] = y
            else:
                A[x - 1] = y
        elif q == 2:
            if reverse:
                reverse = False
            else:
                reverse = True
        elif q == 3:
            x = int(input_data[index])
            index += 1
            if reverse:
                print(A[N - x])
            else:
                print(A[x - 1])


if __name__ == "__main__":
    solve()
