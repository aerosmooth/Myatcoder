import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    S = input_data[1 : 1 + N]

    def char2num(chr):
        if chr == "a" or chr == "b" or chr == "c":
            return "2"
        if chr == "d" or chr == "e" or chr == "f":
            return "3"
        if chr == "g" or chr == "h" or chr == "i":
            return "4"
        if chr == "j" or chr == "k" or chr == "l":
            return "5"
        if chr == "m" or chr == "n" or chr == "o":
            return "6"
        if chr == "p" or chr == "q" or chr == "r" or chr == "s":
            return "7"
        if chr == "t" or chr == "u" or chr == "v":
            return "8"
        if chr == "w" or chr == "x" or chr == "y" or chr == "z":
            return "9"

    Answer = []
    for i in range(N):
        ch = S[i]
        Answer.append(char2num(ch[0]))
    print("".join(Answer))


if __name__ == "__main__":
    solve()
