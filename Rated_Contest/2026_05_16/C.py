import sys


def solve():
    input_data = sys.stdin.read().split()
    S = input_data[0]
    n = len(S)
    Answer = 0

    for i in range(n):
        char = S[i]
        if char == "C":
            left = i
            right = n - i - 1
            margin = min(left, right)
            Answer += margin + 1
    print(Answer)


if __name__ == "__main__":
    solve()
