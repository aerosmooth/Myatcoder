import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    S = input_data[1]
    Answer = False
    for i in range(N - 2):
        if S[i] == S[i + 1] == S[i + 2]:
            Answer = True

    if Answer:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    solve()
