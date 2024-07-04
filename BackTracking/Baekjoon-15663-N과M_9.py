## Backtracking
## Baekjoon 15663 N과 M(9)
## https://www.acmicpc.net/problem/15663

N, M = map(int, input().split())
sequence = sorted(list(map(int, input().split())))
visited = [False] * N
result = list()

def func():
    check = 0

    if len(result) == M:
        print(*result)
        return
    for i in range(N):
        if not visited[i] and sequence[i] != check:
            result.append(sequence[i])
            visited[i] = True
            check = sequence[i]        
            func()
            result.pop()
            visited[i] = False

func()