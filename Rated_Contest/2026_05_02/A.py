import sys


def read_input():
    input_data = sys.stdin.read().split()

    return int(input_data[0])


def solve():
    X = read_input()
    if 3 <= X <= 18:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    solve()
