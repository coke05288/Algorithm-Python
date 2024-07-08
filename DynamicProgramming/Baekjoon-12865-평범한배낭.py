## 동적계획법(Dynamic Programming)
## Baekjoon 12865 평범한 배낭
## https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

w_list = [0]
v_list = [0]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    W, V = map(int, input().split())
    w_list.append(W)
    v_list.append(V)
    
for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j < w_list[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w_list[i]] + v_list[i])

print(dp[N][K])

