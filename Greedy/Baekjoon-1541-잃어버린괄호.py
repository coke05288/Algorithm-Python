## 그리디 알고리즘
## 백준 1541 잃어버린 괄호
## https://www.acmicpc.net/problem/1541

l = input().split("-")

answer = 0

for i in l[0].split("+"):
    answer += int(i)

for i in l[1:]:
    for j in i.split("+"):
        answer -= int(j)

print(answer)