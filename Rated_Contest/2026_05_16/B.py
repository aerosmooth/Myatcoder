import sys


def solve():
    input_data = sys.stdin.read().split()
    H = int(input_data[0])
    W = int(input_data[1])
    if H == 1 and W == 1:
        print(0)
        return
    elif H == 1:
        for j in range(W):
            count = 1
            if not (j == 0 or j == W - 1):
                count += 1
            print(count, end=" ")
        print()
    elif W == 1:
        for i in range(H):
            count = 1
            if not (i == 0 or i == H - 1):
                count += 1
            print(count, end=" ")
        print()
    else:
        for i in range(H):
            for j in range(W):
                count = 2
                if not (i == 0 or i == H - 1):
                    count += 1
                if not (j == 0 or j == W - 1):
                    count += 1

                print(count, end=" ")
            print()


if __name__ == "__main__":
    solve()
