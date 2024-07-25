## Stack & Queue
## Baekjoon 2257 화학식량
## https://www.acmicpc.net/problem/2257

import sys
input = sys.stdin.readline

cf = input().rstrip()
stack = list()

element_dic = {
    'H' : 1,
    'C' : 12,
    'O' : 16
}

for i in cf:
    if i == '(':
        stack.append(i)
    elif i == ')':
        temp_sum = 0
        while stack:
            c = stack.pop()
            if c == '(':
                break
            temp_sum += c
        stack.append(temp_sum)
    elif i in element_dic:
        stack.append(element_dic[i])
    else:
        stack.append(stack.pop() * int(i))


print(sum(stack))