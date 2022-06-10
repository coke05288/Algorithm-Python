# Baekjoon 15686 치킨배달
# BruteForce

from itertools import combinations

n, m = map(int, input().split())

boards = []

for i in range(n):
    boards.append(list(map(int, input().split())))

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if boards[i][j] == 1:
            house.append((i, j))
        elif boards[i][j] == 2:
            chicken.append((i, j))

pick_chicken = list(combinations(chicken, m))
result = [0] * len(pick_chicken)

for i in house:
    for j in range(len(pick_chicken)):
        A = 101
        for k in pick_chicken[j]:
            temp = abs(i[0] - k[0]) + abs(i[1] - k[1])
            A = min(A, temp)
        
        result[j] += A

print(min(result))