## 구현(Implementation)
## Baekjoon 20436 ZOAC 3
## https://www.acmicpc.net/problem/20436

zaum = [
    ['q', 'w', 'e', 'r', 't'],
    ['a', 's', 'd', 'f', 'g'],
    ['z', 'x', 'c', 'v']
]

moem = [
    [' ', 'y', 'u', 'i', 'o', 'p'],
    [' ', 'h', 'j', 'k', 'l'],
    ['b', 'n', 'm']
]

sL, sR = input().split()
target = input()

answer = 0
now_Lx, now_Ly = 0, 0
now_Rx, now_Ry = 0, 0

for alphabet in target:
    state = ""
    
    target_x, target_y = 0, 0

    for i in range(3):
        if alphabet in zaum[i]:
            target_x, target_y = (i, zaum[i].index(alphabet))
            state = "zaum"
            break
        elif alphabet in moem[i]:
            target_x, target_y = (i, moem[i].index(alphabet))
            state = "moem"
            break
    
    if state == "zaum":
        for i in range(3):
            if sL in zaum[i]:
                now_Lx, now_Ly = (i, zaum[i].index(sL))

                if now_Lx == target_x and now_Ly == target_y:
                    break
                else:    
                    answer += abs(now_Lx - target_x) + abs(now_Ly - target_y)
                    sL = zaum[target_x][target_y]

                break
    elif state == "moem":
        for i in range(3):
            if sR in moem[i]:
                now_Rx, now_Ry = (i, moem[i].index(sR))
                
                if now_Rx == target_x and now_Ry == target_y:
                    break
                else:
                    answer += abs(now_Rx - target_x) + abs(now_Ry - target_y)
                    sR = moem[target_x][target_y]
                
                break
    
    answer += 1
    
print(answer)
