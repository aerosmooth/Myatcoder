import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    C = input_data[1]
    A = input_data[2]
    number = 0
    for i in range(N):
        if A[i] == "R":
            number = (number + 2) % 3
        elif A[i] == "B":
            number = (number + 1) % 3

    number = number % 3
    ans_number = 0
    if C == "R":
        ans_number = 2
    elif C == "B":
        ans_number = 1

    if number == ans_number:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    solve()
