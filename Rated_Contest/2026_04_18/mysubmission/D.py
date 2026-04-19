import sys


def reduce(s):
    stack = []
    for c in s:
        stack.append(c)
        if len(stack) >= 4 and stack[-4:] == ["(", "x", "x", ")"]:
            del stack[-4:]
            stack.extend(["x", "x"])
    return "".join(stack)


def solve():
    input_data = sys.stdin.read().split()
    T = int(input_data[0])
    for i in range(T):
        A = input_data[1 + 2 * i]
        B = input_data[2 + 2 * i]
        if reduce(A) == reduce(B):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    solve()
