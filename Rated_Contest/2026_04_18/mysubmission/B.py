import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    M = int(input_data[1])
    F = []
    for i in range(N):
        F.append(int(input_data[2 + i]))

    set_F = set(F)
    if len(set_F) == len(F):
        print("Yes")
    else:
        print("No")

    if len(set_F) == M:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    solve()
