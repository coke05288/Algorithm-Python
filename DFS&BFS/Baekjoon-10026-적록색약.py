## DFS & BFS
## Baekjoon 10026 적록색약
## https://www.acmicpc.net/problem/10026

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = [list(input().rstrip()) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y, color):
    q = deque()
    q.append([x, y])

    while q:
        loot = q.pop()
        x, y = loot[0], loot[1]

        if visited[x][y] == False:
            visited[x][y] = True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx >= 0 and ny >= 0 and nx < n and ny < n:
                    if graph[nx][ny] == color:
                        q.append([nx, ny])
        

visited = [[False] * n for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            temp_color = graph[i][j]
            bfs(i, j, temp_color)
            answer += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False] * n for _ in range(n)]
answer_weakness = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            temp_color = graph[i][j]
            bfs(i, j, temp_color)
            answer_weakness += 1

print(answer, answer_weakness)