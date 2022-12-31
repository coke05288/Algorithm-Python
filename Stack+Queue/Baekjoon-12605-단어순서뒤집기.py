## Stack & Queue
## Baekjoon 12605 단어순서 뒤집기
## https://www.acmicpc.net/problem/12605

n = int(input())

for i in range(n):
    temp = input().split()

    print(f"Case #{i+1}: ", end = "")
    
    while temp:
        print(temp.pop() + " ", end ="")
    
    print()