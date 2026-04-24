from re import A
import sys


def solve():
    input_data = sys.stdin.read().split()
    X = int(input_data[0])
    Y = int(input_data[1])
    Answer = []
    while X >= 2 or Y >= 2:
        Answer.append((X, Y))
        if X > Y:
            X -= Y
        else:
            Y -= X

    Answer.reverse()
    print(len(Answer))
    for x, y in Answer:
        print(x, y)


if __name__ == "__main__":
    solve()
