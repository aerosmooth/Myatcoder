import sys


def read_input():
    input_data = sys.stdin.read().split()
    Q = int(input_data[0])
    t = []
    x = []
    for i in range(Q):
        t.append(int(input_data[1 + 2 * i]))
        x.append(int(input_data[2 + 2 * i]))

    return Q, t, x


def solve():
    Q, t, x = read_input()
    front = []
    back = []
    answer = []

    for i in range(Q):
        if t[i] == 1:
            front.append(x[i])
        elif t[i] == 2:
            back.append(x[i])
        else:
            index = x[i]
            if index <= len(front):
                answer.append(str(front[-index]))
            else:
                answer.append(str(back[index - len(front) - 1]))

    print("\n".join(answer))


if __name__ == "__main__":
    solve()
