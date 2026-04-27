import sys


def read_input():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    Q = int(input_data[1])
    C = []
    P = []
    for i in range(Q):
        C.append(int(input_data[2 + 2 * i]))
        P.append(int(input_data[3 + 2 * i]))

    return N, Q, C, P


def solve():
    N, Q, C, P = read_input()
    # iの上と下を格納
    up = [-1] * (N + 1)
    down = [-1] * (N + 1)

    for i in range(Q):
        c, p = C[i], P[i]
        if down[c] != -1:
            up[down[c]] = -1
        top_p = p
        while up[top_p] != -1:
            top_p = up[top_p]
        up[top_p] = c
        down[c] = top_p

    ans = []
    for i in range(1, N + 1):
        if down[i] == -1:
            cnt = 0
            curr = i
            while curr != -1:
                cnt += 1
                curr = up[curr]
            ans.append(str(cnt))
        else:
            ans.append("0")

    print(" ".join(ans))


if __name__ == "__main__":
    solve()
