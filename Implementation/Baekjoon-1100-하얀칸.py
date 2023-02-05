## 구현(Implementation)
## Baekjoon 1100 하얀칸
## https://www.acmicpc.net/problem/1100

chess = [input() for _ in range(8)]

answer = 0

for i in range(len(chess)):
    for j in range(len(chess[i])):
        if i % 2 == 0:
            if j % 2 == 0 and chess[i][j] == 'F':
                answer += 1
        elif i % 2 == 1:
            if j % 2 == 1 and chess[i][j] == 'F':
                answer += 1

print(answer)