import sys


def solve():
    input_data = sys.stdin.read().split()
    S = input_data[0]
    stack = []
    for i in range(len(S)):
        chr = S[i]
        if chr == "(":
            stack.append(i)
        else:
            index = stack.pop()
            print(index + 1, i + 1)


if __name__ == "__main__":
    solve()
