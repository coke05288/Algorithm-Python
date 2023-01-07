## 구현(Implementation)
## Baekjoon 10103 주사위 게임
## https://www.acmicpc.net/problem/10103

a, b = 100, 100

for _ in range(int(input())):
    a_dice, b_dice = map(int, input().split())

    if a_dice > b_dice:
        b -= a_dice
    elif a_dice < b_dice:
        a -= b_dice 

print(a)
print(b)
