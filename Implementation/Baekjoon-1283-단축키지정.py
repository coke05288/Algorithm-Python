## 구현(Implementation)
## Baekjoon 1283 단축키지정
## https://www.acmicpc.net/problem/1283

def find_shortcut(word_list):
    
    for idx, word in enumerate(word_list):
        if word[0] not in short_cut:
            short_cut.add(str(word[0]).upper())
            temp_word = list(word)
            temp_word.pop(0)
            text = "[" + word[0] + "]" + "".join(temp_word)
            word_list[idx] = text
            return " ".join(word_list)

    temp = " ".join(word_list)

    for idx, t in enumerate(temp):
        if t != " ":
            if (t.upper() not in short_cut):
                short_cut.add(t.upper())
                return temp[0:idx] + "[" + t + "]" + temp[idx+1:]
    
    return "".join(word_list)

def solution(_option):
    return find_shortcut(list(_option.split()))

short_cut = set()

for _ in range(int(input())):
    option = input()
    print(solution(option))