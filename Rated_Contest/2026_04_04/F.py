import sys


class BIT:
    def __init__(self, N):
        self.N = N
        self.bits = [0] * (self.N + 1)

    def update(self, i, x):
        while i <= self.N:
            self.bits[i] += x
            i += i & -i

    def total(self, i):
        res = 0

        while i > 0:
            res += self.bits[i]
            i -= i & -i

        return res


N = int(input())
A = list(map(int, input().split()))
bits = BIT(N)

count = 0

for i in range(N - 1, -1, -1):
    count += bits.total(A[i] - 1)
    bits.update(A[i], 1)

print(count)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        exit()
    N = int(input_data[0])
    K = int(input_data[1])
    P = [int(x) for x in input_data[2 : N + 2]]


if __name__ == "__main__":
    solve()
