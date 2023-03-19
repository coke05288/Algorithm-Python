## 구현(Implementation)
## Baekjoon 2851 슈퍼마리오
## https://www.acmicpc.net/problem/2851

mushroom = [int(input()) for _ in range(10)]

answer = 0
sum_score = 0
diff = 100

for i in mushroom:
    sum_score += i
    temp_gap = abs(sum_score - 100)

    if diff >= temp_gap:
        diff = temp_gap
        answer = sum_score

print(answer)