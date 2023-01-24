## 구현(Implementation)
## Baekjoon 1546 평균
## https://www.acmicpc.net/problem/1546

N = int(input())

scores = list(map(int, input().split()))
M = max(scores)

scores = [i / M * 100 for i in scores]

print(sum(scores)/len(scores))
