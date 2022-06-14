## Backtracking
## Baekjoon 15649 N과 M(1)
## https://www.acmicpc.net/problem/15649

N, M = map(int, input().split())
result = list()

def func():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            func()
            result.pop()

func()