import sys


def solve():
    input_data = sys.stdin.read().split()
    X = int(input_data[0])
    Y = int(input_data[1])

    if X / Y == 16 / 9:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    solve()
