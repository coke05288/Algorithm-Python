## 구현(Implementation)
## Baekjoon 5597 과제 안 내신 분...?
## https://www.acmicpc.net/problem/5597

num_list = list(range(1, 31))

for _ in range(28):
    num_list.remove(int(input()))

print(num_list[0])
print(num_list[-1])
