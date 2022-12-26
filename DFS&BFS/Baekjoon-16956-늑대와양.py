import sys
input = sys.stdin.readline

R, C = map(int, input().split())

State = []

for _ in range(R):
    State.append(list(input().rstrip()))

sign = False

for i in range(R):
    for j in range(C):
        if State[i][j] == 'W':
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]

            for k in range(4):
                tx = i + dx[k]
                ty = j + dy[k]

                if (0 <= tx and tx < R) and (0 <= ty and ty < C) and State[tx][ty] == 'S':
                    sign = True
                    break
        
        elif State[i][j] == 'S':
            continue

        elif State[i][j] == '.':
            State[i][j] = 'D'


if sign:
    print(0)
else:
    print(1)
    for i in range(R):
        print(''.join(State[i]))
    
