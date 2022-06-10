# Baekjoon 16917 양념반후라이드반
# BruteForce

def solution():
    
    answer = 0

    a = input_list[0]
    b = input_list[1]
    c = input_list[2]
    x = input_list[3]
    y = input_list[4]

    if a + b < 2 * c:
        answer = a * x + b * y
    else:
        answer = 2 * c * min(x, y) + min(a, 2 * c) * max(0, x - y) + min(b, 2 * c) * max(0, y - x)
        
    return answer

input_list = list(map(int, input().split(" ")))

print(solution())