import sys
from typing_extensions import dataclass_transform


class segtree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.dat = [0] * (self.size * 2)

    def update(self, pos, x):
        pos += self.size
        self.dat[pos] = x
        while pos >= 2:
            pos //= 2
            self.dat[pos] = max(self.dat[pos * 2-, self.dat[pos * 2 + 1]])

    def query(self, l, r, a, b, u):
        if r<= a or b <= l:
            return -10000000000000
        if l <= a and b <= r:
            return self.dat[u]
        m = (a + b) // 2
        answerl = self.query(l, r, a, m, u * 2)
        answerr = self.query(l, r, m, b, u * 2 + 1)
        return max(answerl, answerr)


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    Q = int(input_data[1])
    index = 2
    Z = segtree(N)
    for i in range(Q):
        query = int(input_data[index])
        index += 1
        if query == 1:
            pos = int(input_data[index])
            index += 1
            x = int(input_data[index])
            index += 1
            Z.update(pos - 1, x)
        else:
            l = int(input_data[index])
            index += 1
            r = int(input_data[index])
            index += 1
            print(Z.query(l - 1, r - 1, 0, Z.size, 1))


if __name__ == "__main__":
    solve()
