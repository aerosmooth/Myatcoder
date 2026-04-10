import sys


def Enumerate(A: list):
    SumList = []
    for i in range(2 ** len(A)):
        sum = 0
        for j in range(len(A)):
            wari = 2**j
            if (i // wari) % 2 == 1:
                sum += A[j]
        SumList.append(sum)
    return SumList


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        exit()
    N = int(input_data[0])
    K = int(input_data[1])
    A = [int(x) for x in input_data[2 : N + 2]]

    A_initial = A[: N // 2]
    A_last = A[N // 2 :]

    Sum_A = Enumerate(A_initial)
    Sum_B = Enumerate(A_last)
    Sum_A.sort()
    Sum_B.sort()

    for a in Sum_A:
        num = K - a
        left = 0
        right = len(Sum_B)
        while left < right:
            mid = (left + right) // 2
            if Sum_B[mid] < num:
                left = mid + 1
            elif Sum_B[mid] > num:
                right = mid
            else:
                print("Yes")
                return
    print("No")
    return


if __name__ == "__main__":
    solve()
