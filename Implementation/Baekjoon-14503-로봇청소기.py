## 구현(Implementation)
## Baekjoon 14503 로봇청소기
## https://www.acmicpc.net/problem/14503

N, M = map(int, input().split())

r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

graph[r][c] = '@'
answer = 1

turning = 0

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

while True:
    turn_left()
    nx, ny = r + dx[d], c + dy[d]

    if graph[nx][ny] == 0:
        graph[nx][ny] = '@'
        r, c = nx, ny
        answer += 1
        turning = 0
        continue
    else:
        turning += 1

    if turning == 4:
        nx, ny = r - dx[d], c - dy[d]

        if graph[nx][ny] != 1:
            r,c = nx, ny
        else:
            break

        turning = 0

print(answer)