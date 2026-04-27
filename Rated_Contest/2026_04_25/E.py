import sys
from collections import defaultdict


def read_input():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    S = input_data[1]

    return N, S


def solve():
    N, S = read_input()
    """
    dpだとN^2くらいになるから無理
    累積和系でいけそうな雰囲気ある
    逆に条件を満たす（出現回数が同じ）が少ないからそれを数えた方が早いのでは？
    sum_A[i]はS[0:i-1]に現れるAの個数とかと定義する
    部分文字列[l,r]でA=Bになるのは
    sum_A[r+1] - sum_A[l]
    =
    sum_B[r+1] - sum_B[l]
    この条件を満たすのをA,Bとか全部で探して重複消せば良い
    でもl,rでやったら増えるな。
    Nがでかいから一回見るくらいで終わらせたい
    sum_A[r+1] - sum_B[r+1]
    =
    sum_A[l] - sum_B[l]
    を満たせば良い。だから、ある時点でのA,B,Cの差分を計算していってそれらを良い感じに足していけば良い
    """
    count_ab = defaultdict(int)
    count_bc = defaultdict(int)
    count_ca = defaultdict(int)
    count_all = defaultdict(int)

    a = 0
    b = 0
    c = 0

    count_ab[0] = 1
    count_bc[0] = 1
    count_ca[0] = 1
    count_all[(0, 0)] = 1

    Answer_ab = 0
    Answer_bc = 0
    Answer_ca = 0
    Answer_all = 0

    for ch in S:
        if ch == "A":
            a += 1
        elif ch == "B":
            b += 1
        elif ch == "C":
            c += 1

        diff_ab = a - b
        diff_bc = b - c
        diff_ca = c - a
        diff_all = (diff_ab, diff_bc)

        Answer_ab += count_ab[diff_ab]
        Answer_bc += count_bc[diff_bc]
        Answer_ca += count_ca[diff_ca]
        Answer_all += count_all[diff_all]

        count_ab[diff_ab] += 1
        count_bc[diff_bc] += 1
        count_ca[diff_ca] += 1
        count_all[diff_all] += 1

    print(N * (N + 1) // 2 - Answer_ab - Answer_bc - Answer_ca + 2 * Answer_all)


if __name__ == "__main__":
    solve()
