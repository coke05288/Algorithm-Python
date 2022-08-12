## 구현(Implementation)
## Programmers 오픈채팅방
## https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    
    user_db = dict()
    split_data = []
    message_list = []

    for re in record:
        split_data = list(map(str, re.split()))

        if split_data[0] == "Enter" or split_data[0] == "Change":
            user_db[f"{split_data[1]}"] = split_data[2]
        
        message_list.append(split_data)
    
    for message in message_list:
        if message[0] == "Enter":
            answer.append(f"{user_db[message[1]]}님이 들어왔습니다.")
        elif message[0] == "Leave":
            answer.append(f"{user_db[message[1]]}님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))