## 구현(Implementation), 재귀(Reucursion)
## Baekjoon 1914 하노이탑
## https://www.acmicpc.net/problem/1914

n = int(input())

def hanoi(n, start_pos, aux_pos, target_pos):
    if n == 0:
        return
    
    hanoi(n-1, start_pos, target_pos, aux_pos)
    print(start_pos, target_pos)
    hanoi(n-1, aux_pos, start_pos, target_pos)

print(2**n - 1)

if n <= 20:
    hanoi(n, 1, 2, 3)