## 동적계획법(Dynamic Programming)
## Baekjoon 9251 LCS
## https://www.acmicpc.net/problem/9251

import sys
input = sys.stdin.readline

sequence = []

for _ in range(2):
    sequence.append(list(input().rstrip()))

dp = [[0 for _ in range(len(sequence[0]) + 1)] for _ in range(len(sequence[1]) + 1)]

for i in range(1, len(sequence[1]) + 1):
    for j in range(1, len(sequence[0]) + 1):
        if sequence[1][i - 1] != sequence[0][j - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)

print(dp[-1][-1])
