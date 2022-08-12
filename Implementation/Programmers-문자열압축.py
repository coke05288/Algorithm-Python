## 구현(Implementation)
## Programmers 문자열 압축
## https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    
    answer = len(s)

    if answer == 1: return 1

    for u in range(1, len(s) // 2 + 1):
        split_list = [ s[i:(i+u)]  for i in range(0, len(s), u)]
        
        tmp_count = 1
        tmp_list = []

        print(split_list)

        for r in range(len(split_list) - 1):
            if split_list[r] == split_list[r+1]:
                tmp_count += 1

                if r == len(split_list) -2:
                    tmp_list.append(f"{tmp_count}{split_list[r]}")
            
            else:
                if tmp_count != 1:
                    tmp_list.append(f"{tmp_count}{split_list[r]}")
                    tmp_count = 1
                else:
                    tmp_list.append(split_list[r])

                if r == len(split_list) - 2:
                    tmp_list.append(split_list[r+1])

        print(tmp_list)

        join_list = "".join(tmp_list)
        
        if len(join_list) < answer:
            answer = len(join_list)

    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))