import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    L = int(input_data[1])
    A = []
    B = []
    for i in range(N):
        A.append(int(input_data[2 + 2 * i]))
        B.append(input_data[3 + 2 * i])

    Answer = 0
    for i in range(N):
        tmp = 0
        if B[i] == "E":
            tmp = L - A[i]
        else:
            tmp = A[i]
        Answer = max(Answer, tmp)

    print(Answer)


if __name__ == "__main__":
    solve()
