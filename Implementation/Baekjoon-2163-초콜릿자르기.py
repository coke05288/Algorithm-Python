## 구현(Implementation)
## Baekjoon 2163 초콜릿자르기
## https://www.acmicpc.net/problem/2163

N, M = map(int, input().split())

answer = (N - 1) + N * (M - 1)

print(answer)