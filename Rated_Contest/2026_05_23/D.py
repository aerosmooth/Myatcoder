import sys
from collections import Counter


def solve():
    input_data = sys.stdin.read().split()
    T = int(input_data[0])
    for i in range(T):
        S = input_data[1 + i]
        counter = Counter(S)
        S_len = len(S)
        max_count = counter.most_common(1)[0][1]
        if max_count > (S_len + 1) // 2:
            print("No")
        else:
            print("Yes")
            sorted_chars = []
            for char, count in counter.most_common():
                sorted_chars.extend([char] * count)

            res = [""] * S_len
            index = 0
            for char in sorted_chars:
                res[index] = char
                index += 2
                if index >= S_len:
                    index = 1

            print("".join(res))


if __name__ == "__main__":
    solve()
