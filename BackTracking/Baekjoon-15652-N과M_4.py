## Backtracking
## Baekjoon 15652 N과 M(4)
## https://www.acmicpc.net/problem/15652

N, M = map(int, input().split())
result = list()

def func(k):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for i in range(k, N+1):
        result.append(i)
        func(i)
        result.pop()

func(1)