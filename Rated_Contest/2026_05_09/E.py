import sys
import bisect


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    M = int(input_data[1])
    L = []
    R = []
    for i in range(M):
        L.append(int(input_data[2 + 2 * i]))
        R.append(int(input_data[3 + 2 * i]))
    Q = int(input_data[2 + 2 * M])
    S = []
    T = []
    base = 2 + 2 * M + 1
    for i in range(Q):
        S.append(int(input_data[base + 2 * i]))
        T.append(int(input_data[base + 1 + 2 * i]))

    max_R = [[] for _ in range(N + 1)]
    min_L = [[] for _ in range(N + 1)]
    starts_at = [[] for _ in range(N + 1)]
    for i in range(M):
        max_R[L[i]].append((R[i], i))
        min_L[R[i]].append((L[i], i))
        starts_at[L[i]].append(R[i])

    for i in range(N + 1):
        max_R[i].sort()
        min_L[i].sort()

    min_R1 = [float("inf")] * (N + 2)
    min_R2 = [float("inf")] * (N + 2)
    for i in range(N, 0, -1):
        r1 = min_R1[i + 1]
        r2 = min_R2[i + 1]
        for r in starts_at[i]:
            if r < r1:
                r2 = r1
                r1 = r
            elif r < r2:
                r2 = r
        min_R1[i] = r1
        min_R2[i] = r2

    for i in range(Q):
        s = S[i]
        t = T[i]

        index_r = bisect.bisect_right(max_R[s], (t, float("inf")))
        candisates_A = max_R[s][max(0, index_r - 2) : index_r]
        index_l = bisect.bisect_left(min_L[t], (s, -1))
        candisates_B = min_L[t][index_l : min(len(min_L[t]), index_l + 2)]
        Answer = False

        for r_a, id_a in candisates_A:
            for l_b, id_b in candisates_B:
                if id_a != id_b and l_b <= r_a + 1:
                    Answer = True
        if not Answer:
            exact_match = False
            idx = bisect.bisect_left(max_R[s], (t, -1))
            if idx < len(max_R[s]) and max_R[s][idx][0] == t:
                exact_match = True
            if exact_match and min_R2[s] <= t:
                Answer = True
        if Answer:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    solve()
