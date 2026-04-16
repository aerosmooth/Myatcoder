import sys


def solve():
    input_data = sys.stdin.read().split()
    W = int(input_data[0])
    Prime = [0] * 300001
    Prime[0] = 1
    Prime[1] = 1
    for i in range(2, 300001):
        if Prime[i] == 0:
            k = 300001 // i
            for j in range(2, k):
                Prime[j * i] = 1

    for i in range(W):
        if Prime[int(input_data[1 + i])] == 0:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    solve()
