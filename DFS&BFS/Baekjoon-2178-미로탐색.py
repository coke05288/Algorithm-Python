## DFS & BFS
## Baekjoon 2178 미로탐색
## https://www.acmicpc.net/problem/2178


N, M = map(int, input().split())
miro = []

for _ in range(N):
    miro.append(list(map(int, input())))

def solution(miro):
    q = []
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    q.append((0, 0))

    while q:
        x, y = q.pop(0)

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if miro[nx][ny] != 0 and miro[nx][ny] == 1:
                    miro[nx][ny] += miro[x][y]
                    q.append((nx, ny))

    return miro[N-1][M-1]

print(solution(miro))