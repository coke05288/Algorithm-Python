## DFS & BFS
## Baekjoon 1012 유기농배추
## https://www.acmicpc.net/problem/1012


T = int(input())

def bfs(field, start):
    q = []
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    field[start[0]][start[1]] = -1

    q.append((start[0], start[1]))

    while q:
        x, y = q.pop(0)

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if field[nx][ny] != 0 and field[nx][ny] == 1:
                    field[nx][ny] = -1
                    q.append((nx, ny))
     

def solution(field):
    answer = 0

    for i in range(N):
        for j in range(M):
            if field[i][j] != -1 and field[i][j] != 0:
                bfs(field, (i, j))
                answer += 1

    return answer


for _ in range(T):
    M, N, K = map(int, input().split())

    field = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    print(solution(field))
