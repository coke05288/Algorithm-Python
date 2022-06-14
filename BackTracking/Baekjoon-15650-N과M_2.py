## Backtracking
## Baekjoon 15649 N과 M(2)
## https://www.acmicpc.net/problem/15650

N, M = map(int, input().split(" "))
arr = []

def func(_k):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(_k, N + 1):
        if i not in arr:
            arr.append(i)
            func(i+1)
            arr.pop()

func(1)