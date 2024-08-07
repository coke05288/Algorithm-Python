## Backtracking
## Baekjoon 15649 N과 M(2)
## https://www.acmicpc.net/problem/15650

N, M = map(int, input().split())
result = list()

def func(_k):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(_k, N + 1):
        if i not in result:
            result.append(i)
            func(i+1)
            result.pop()

func(1)