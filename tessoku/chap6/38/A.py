import sys


def solve():
    input_data = sys.stdin.read().split()
    D = int(input_data[0])
    N = int(input_data[1])
    L = []
    R = []
    H = []
    for i in range(N):
        L.append(int(input_data[2 + 3 * i]))
        R.append(int(input_data[3 + 3 * i]))
        H.append(int(input_data[4 + 3 * i]))
    Lim_time = [24] * (D + 1)
    for i in range(N):
        for j in range(L[i], R[i] + 1):
            Lim_time[j] = min(Lim_time[j], H[i])

    Answer = 0
    for i in range(D):
        Answer += Lim_time[i + 1]

    print(Answer)


if __name__ == "__main__":
    solve()
