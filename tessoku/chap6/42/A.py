import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    K = int(input_data[1])
    A = []
    B = []
    for i in range(N):
        A.append(int(input_data[2 + 2 * i]))
        B.append(int(input_data[3 + 2 * i]))

    Answer = 0
    for a in range(1, 101):
        for b in range(1, 101):
            # aからa+K以下に何人いるか　かつ　bからb+K以下に何人いるか
            cnt = 0
            for i in range(N):
                if a <= A[i] <= a + K and b <= B[i] <= b + K:
                    cnt += 1
            Answer = max(Answer, cnt)

    print(Answer)


if __name__ == "__main__":
    solve()
