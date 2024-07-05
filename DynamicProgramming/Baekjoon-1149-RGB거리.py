## Dynamic Programming
## Baekjoon 1149 RGB거리
## https://www.acmicpc.net/problem/1149

N = int(input())
dp = []

for _ in range(N):
    dp.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(3):
        temp_value = []
        for k in range(3):
            if j != k:
                temp_value.append(dp[i][j] + dp[i-1][k])
        dp[i][j] = min(temp_value)

print(min(dp[N-1]))