## 구현(Implementation)
## Baekjoon 1924 2007년
## https://www.acmicpc.net/problem/1924

x, y = map(int, input().split())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

dif = 0

for i in range(x - 1):
    dif += month[i]

print(week[(dif + y) % 7])