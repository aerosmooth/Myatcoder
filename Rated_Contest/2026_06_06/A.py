import sys


def solve():
    input_data = sys.stdin.read().split()
    A = int(input_data[0])
    D = int(input_data[1])
    if A <= D:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    solve()
