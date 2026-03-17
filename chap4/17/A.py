N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = [0] * N
for i in range(1, N):
    tmp_i_1 = ans[i - 1] + A[i - 1]
    if i >= 2:
        tmp_i_2 = ans[i - 2] + B[i - 2]
        ans[i] = min(tmp_i_1, tmp_i_2)
    else:
        ans[i] = tmp_i_1
ANSWER = []
Place = N
while True:
    ANSWER.append(Place)
    if Place == 1:
        break
    if ans[Place - 1] == ans[Place - 2] + A[Place - 2]:
        Place -= 1
    else:
        Place -= 2
ANSWER.reverse()
print(len(ANSWER))
for i in ANSWER:
    print(i, end=" ")
print()
