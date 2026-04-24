import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    isPrime = [True] * (N + 1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(N + 1):
        if isPrime[i]:
            k = N // i
            for j in range(2, k + 1):
                isPrime[j * i] = False
    for i in range(N + 1):
        if isPrime[i]:
            print(i)


if __name__ == "__main__":
    solve()
