N = input()
result = 0
len_N = len(N)
idx = 1
for n in N:
    n = int(n)
    result += n * 2 ** (len_N - idx)
    idx += 1

print(result)
