
M = int(input())

pos = 1

for i in range(M):
    X, Y = map(int, input().split())
    
    if X == pos:
        pos = Y
        continue

    if Y == pos:
        pos = X
        continue
    
print(pos)    
