import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    print(N // 3 + N // 5 - N // 15)


if __name__ == "__main__":
    solve()
