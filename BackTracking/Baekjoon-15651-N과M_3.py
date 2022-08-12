## Backtracking
## Baekjoon 15651 N과 M(3)
## https://www.acmicpc.net/problem/15651

N, M = map(int, input().split(" "))

result = list()

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(1, N + 1):
        result.append(i)
        dfs()
        result.pop()

dfs()