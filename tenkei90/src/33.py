import sys


def read_input():
    input_data = sys.stdin.read().split()
    H = int(input_data[0])
    W = int(input_data[1])

    return H, W


def solve():
    H, W = read_input()
    if H == 1 or W == 1:
        print(H * W)
    else:
        print(((H + 1) // 2) * ((W + 1) // 2))


if __name__ == "__main__":
    solve()
