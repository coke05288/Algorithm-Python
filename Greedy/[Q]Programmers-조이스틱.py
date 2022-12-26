## 그리디 알고리즘
## 프로그래머스 조이스틱
## https://school.programmers.co.kr/learn/courses/30/lessons/42860

def greedy_case(char_list):
    greedy_case_answer = 0
    idx = 0

    while True:
        greedy_case_answer += char_list[idx]
        char_list[idx] = 0

        if sum(char_list) == 0:
            break

        left, right = 1, 1

        print(char_list)

        while char_list[idx - left] == 0:
            left += 1
        
        while char_list[idx + right] == 0:
            right += 1

        temp_left_right_value = 0

        if left < right :
            temp_left_right_value = left
            idx -= left
        else:
            temp_left_right_value = right
            idx += right

        greedy_case_answer += temp_left_right_value

    print(greedy_case_answer)
    print("----")

    return greedy_case_answer

def left_to_right_to_back(char_list):
    left_to_right_to_back_case_answer = 0
    idx = 0

    for index, value in enumerate(char_list):
        if value > 0:
            idx = index
            left_to_right_to_back_case_answer += idx
            break


    while True:
        left_to_right_to_back_case_answer += char_list[idx]
        char_list[idx] = 0

        if sum(char_list) == 0:
            break

        print(char_list)

        left, right = 1, 1

        while char_list[idx - left] == 0:
            left += 1
        
        while char_list[idx + right] == 0:
            right += 1

        temp_left_right_value = 0

        if left < right :
            temp_left_right_value = left
            idx -= left
        else:
            temp_left_right_value = right
            idx += right

        left_to_right_to_back_case_answer += temp_left_right_value

    print(left_to_right_to_back_case_answer)
    return left_to_right_to_back_case_answer

def solution(name):   
    
    char_list_1 = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    char_list_2 = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    
    return min(greedy_case(char_list_1), left_to_right_to_back(char_list_2))


print(solution("AAAABA"))