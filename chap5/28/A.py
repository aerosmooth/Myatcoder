import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    blackboard_num = 0
    for i in range(N):
        T_i = input_data[1 + 2 * i]
        A_i = int(input_data[2 + 2 * i])
        if T_i == "+":
            blackboard_num = (A_i + blackboard_num + 10000) % 10000
        elif T_i == "-":
            blackboard_num = (blackboard_num - A_i + 10000) % 10000
        elif T_i == "*":
            blackboard_num = (A_i * blackboard_num + 10000) % 10000
        blackboard_num = (blackboard_num + 10000) % 10000
        print(blackboard_num)


if __name__ == "__main__":
    solve()
