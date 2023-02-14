## Stack & Queue
## Baekjoon 2493 탑
## https://www.acmicpc.net/problem/2493

N = int(input())
top_list = list(map(int, input().split()))

answer = [0] * N
stack = []

for i in range(len(top_list)):
    while stack:
        if top_list[i] > stack[-1][1]:
            stack.pop()
        else:
            answer[i] = stack[-1][0] + 1
            break

    stack.append((i, top_list[i]))


for i in answer:
    print(i, end =" ")