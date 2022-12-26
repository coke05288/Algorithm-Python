
def solution(skill, skill_trees):
    answer = 0

    for case in skill_trees:
        temp_check = list(skill)
        
        for s in case:
            if temp_check:
                if s == temp_check[0]:
                    del temp_check[0]

        if not temp_check:
            print(case)
            answer += 1
            continue

        check_skill = 0
        
        for c in temp_check:
            if c in case:
                check_skill += 1
        
        if check_skill == 0 : 
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))