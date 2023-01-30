## 구현(Implementation)
## Baekjoon 3190 뱀
## https://www.acmicpc.net/problem/3190

from collections import deque


### CHECK INPUT ###
N = int(input())

graph = [[0 for _ in range(N+2)] for _ in range(N+2)]
graph[0] = [1 for _ in range(N+2)]
graph[N+1] = [1 for _ in range(N+2)]

for i in range(len(graph)):
    graph[i][0] = 1
    graph[i][N+1] = 1

K = int(input())

for _ in range(K):
    ax, ay = map(int, input().split())
    graph[ax][ay] = 8   

L = int(input())

action = deque()
snake = deque()

for _ in range(L):
    sec, dir = map(str, input().split())
    action.append([int(sec), dir])
###################


### CHECK INPUT ###
# for i in range(len(graph)):
#     print(graph[i])

# print(action)
###################


#### SET VALUE ####
x, y = 1, 1
snake.append([x, y])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direction = 0
length = 1
timer = 0
###################


#### ALGORITHM ####
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

def turn_right():
    global direction
    direction += 1
    if direction == 4:
        direction = 0

while True:
    ## print("< timer : {} >".format(timer)) ## TEMP PRINT ##

    if action:
        if action[0][0] == timer:
            ## print("< action : {} >".format(action[0][0])) ## TEMP PRINT ##
            if action[0][1] == 'D':
                turn_right()
            elif action[0][1] == 'L':
                turn_left()
            action.popleft()

    nx, ny = x + dx[direction], y + dy[direction]

    if nx > 0 and nx < N+1 and ny > 0 and ny < N+1:
        if graph[nx][ny] != 1 and graph[nx][ny] != 2:
            
            if [nx, ny] in snake: break

            snake.append([nx, ny])
            
            if graph[nx][ny] == 8:
                length += 1
                graph[nx][ny] = 0

            if len(snake) > length:
                snake.popleft()

            x, y = nx, ny

            ## print("#length : {} \n#snake : {}".format(length, snake)) ## TEMP PRINT ##
        else:
            break
    else:
        break

    timer += 1
###################


### PRINT ANSWER ##
print(timer+1)
###################