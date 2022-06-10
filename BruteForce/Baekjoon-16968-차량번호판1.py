# Baekjoon 16968 차량번호판1
# BruteForce

# 1. Recursive
def recur_solution(_s, _index, _last):
    
    # Base-Case
    if len(_s) == _index:
        return 1

    start = ord('a') if _s[_index] == 'c' else ord('0')
    end = ord('z') if _s[_index] == 'c' else ord('9')

    answer = 0

    for i in range(start, end+1):
        if i != _last:
            answer += recur_solution(_s, _index + 1, i)

    return answer

# function 001 | 2. Combine
def comb_solution(_s):
    answer = 1

    for i in range(0, len(_s)):
        cnt = 26 if _s[i] == 'c' else 10

        if i > 0 and _s[i] == _s[i - 1]:
            cnt -= 1

        answer = answer * cnt

    return answer


s = input()
    
print(recur_solution(s, 0, ' '))
print(comb_solution(s))
