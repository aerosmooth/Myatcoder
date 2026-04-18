import sys


def solve():
    input_data = sys.stdin.read().split()
    A = int(input_data[0])
    B = int(input_data[1])

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    print(gcd(A, B))


if __name__ == "__main__":
    solve()
