N = int(input())
res = 0
for i in range(1, N // 2 + 1):
    res += i * (N // i)  # 우선순위를 주의해야할거같음
for i in range(N // 2 + 1, N + 1):
    res += i
print(f"{res}")
