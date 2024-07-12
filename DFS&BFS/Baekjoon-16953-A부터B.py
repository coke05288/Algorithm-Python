## DFS & BFS
## Baekjoon 16953 A -> B
## https://www.acmicpc.net/problem/16953

import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

A, B = map(int, input().split())

def dfs(num, answer):

    # print(f"@ Depth : {answer} / Num : {num}")
    if num == A:
        return answer
    elif num < A:
        return -1

    if num % 2 == 0:
        answer = dfs(num//2, answer + 1)
    elif int(str(num)[-1]) == 1:
        answer = dfs(int(str(num)[:-1]), answer + 1)
    else:
        answer = -1

    return answer

print(dfs(B, 1))