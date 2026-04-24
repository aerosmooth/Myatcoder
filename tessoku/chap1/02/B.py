A, B = map(int, input().split())
for num in range(A, B + 1):
    if 100 % num == 0:
        print("Yes")
        exit(0)
print("No")
