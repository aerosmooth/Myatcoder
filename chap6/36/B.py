import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    K = int(input_data[1])
    S = list(map(int, input_data[2]))
    if (sum(S) - K) % 2 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    solve()
