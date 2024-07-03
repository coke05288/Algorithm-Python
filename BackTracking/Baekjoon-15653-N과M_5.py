## Backtracking
## Baekjoon 15653 N과 M(5)
## https://www.acmicpc.net/problem/15653

N, M = map(int, input().split())
sequence = list(map(int, input().split()))
result = list()

def func():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for i in sorted(sequence):
        if i not in result:
            result.append(i)
            func()
            result.pop()

func()