## DFS & BFS
## Baekjoon 11724 연결 요소의 개수 구하기
## https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

Graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def initGraph():
    for _ in range(M):
        start, end = map(int, input().split())
  
        Graph[start].append(end)
        Graph[end].append(start)

def dfs(v):
    
    visited[v] = True

    for i in Graph[v]:
        if not visited[i]:
            dfs(i)

def solution():
    answer = 0

    for i in range(1, N+1):
        if not visited[i]:
            answer += 1
            dfs(i)

    return answer

initGraph()
print(solution())