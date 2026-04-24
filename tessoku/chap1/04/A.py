N = int(input())
results = [0] * 10
idx = 9
while N != 0:
    results[idx] = N % 2
    idx -= 1
    N = N // 2

for i in results:
    print(i, end="")
print()
