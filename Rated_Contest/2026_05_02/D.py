import sys
from collections import defaultdict


def read_input():
    input_data = sys.stdin.read().split()

    return input_data[0]


def solve():
    S = read_input()
    MOD = 998244353
    ch_dict = defaultdict(int)
    n = len(S)
    Answer = 0
    for i in range(n):
        ch = S[i]
        curr_ans = (Answer + 1 - ch_dict[ch]) % MOD
        ch_dict[ch] += curr_ans
        Answer = (Answer + curr_ans) % MOD

    print(Answer)


if __name__ == "__main__":
    solve()
