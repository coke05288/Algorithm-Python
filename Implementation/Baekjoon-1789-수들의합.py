## 구현(Implementation)
## Baekjoon 1789 수들의 합
## https://www.acmicpc.net/problem/1789

S = int(input())

total = 0
count = 0

while True:
    count += 1
    total += count

    if total > S:
        break

print(count-1)