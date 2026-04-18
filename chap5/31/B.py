import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    print(N // 3 + N // 5 + N // 7 - N // 15 - N // 35 - N // 21 + N // 105)


if __name__ == "__main__":
    solve()
