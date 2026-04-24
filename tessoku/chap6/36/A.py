import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    K = int(input_data[1])
    if K >= 2 * (N - 1):
        if K % 2 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")


if __name__ == "__main__":
    solve()
