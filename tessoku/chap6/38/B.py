import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    S = input_data[1]
    permissible_length_left = [1] * N
    permissible_length_right = [1] * N
    for i in range(N - 1):
        if S[i] == "A":
            permissible_length_left[i + 1] = permissible_length_left[i] + 1
    for i in range(N - 2, -1, -1):
        if S[i] == "B":
            permissible_length_right[i] = permissible_length_right[i + 1] + 1
    Answer = 0
    for i in range(N):
        Answer += max(permissible_length_right[i], permissible_length_left[i])
    print(Answer)


if __name__ == "__main__":
    solve()
