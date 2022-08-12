## Backtracking
## Baekjoon 9663 N-Queen
## https://www.acmicpc.net/problem/9663

result = 0
N = int(input())
row = [0 for _ in range(N)]

def purning(_current):
    for i in range(_current):
        if row[_current] == row[i] or abs(row[i] - row[_current]) == abs(_current - i):
            return False
    return True

def dfs(_current):
    global result

    if _current == N:
        result += 1
        return
    
    for i in range(N):
        row[_current] = i
        if purning(_current):
            #print(_current , " " , i)
            dfs(_current + 1)

dfs(0)  
print(result)
