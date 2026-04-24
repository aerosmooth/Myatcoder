import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    A = [int(x) % 100 for x in input_data[1 : 1 + N]]
    numlist = [0] * 100
    for a in A:
        numlist[a - 1] += 1

    Answer = 0
    for i in range(100):
        for j in range(i, 100):
            if (i + j + 2) % 100 == 0:
                if i == j:
                    Answer += numlist[i] * (numlist[i] - 1) // 2
                else:
                    Answer += numlist[i] * numlist[j]

    print(Answer)


if __name__ == "__main__":
    solve()
