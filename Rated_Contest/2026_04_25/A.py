import sys


def read_input():
    input_data = sys.stdin.read().split()
    A = int(input_data[0])
    B = int(input_data[1])
    C = int(input_data[2])

    return A, B, C


def solve():
    A, B, C = read_input()
    if (A != B) and (B == C):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    solve()
