import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    X = input_data[1]
    S = []
    for i in range(N):
        S.append(input_data[2 + i])

    if X == "A":
        index = 0
    elif X == "B":
        index = 1
    elif X == "C":
        index = 2
    elif X == "D":
        index = 3
    elif X == "E":
        index = 4

    for i in range(N):
        if S[i][index] == "o":
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    solve()
