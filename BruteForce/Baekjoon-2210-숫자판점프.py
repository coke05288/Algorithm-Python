l = 0

board = []
result = set()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, num, length):
    
    global l

    if length == 6:
        result.add(num)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < 5 and ny >= 0 and ny < 5:
            l = l + 1
            dfs(nx, ny, num * 10 + board[nx][ny], length + 1)

# 보드 입력
for i in range(5):
    board.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j], 1)

print(l)
print(len(result))