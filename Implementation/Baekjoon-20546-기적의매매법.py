## 구현(Implementation)
## Baekjoon 20546 기적의 매매법
## https://www.acmicpc.net/problem/20546

seed_money = int(input())

JH = seed_money
SM = seed_money

MachineDuck = [int(i) for i in input().split()]

def check_BNP(JH):    
    
    num_of_stock = 0

    for i in MachineDuck:
        if i <= JH:
            num_of_stock += JH // i
            JH = JH % i
    
    return JH + MachineDuck[-1] * num_of_stock
    
def check_33(SM):
    
    num_of_stock = 0
    stack_price_check = []

    prev_price = MachineDuck[0]
    state = ""

    for i in MachineDuck:
        if (i - prev_price) < 0 :
            state = "DOWN"
        elif (i - prev_price) > 0:
            state = "UP"
        else :
            continue

        if stack_price_check:
            if stack_price_check[0] == state:
                stack_price_check.append(state)
            else:
                stack_price_check.clear()
                stack_price_check.append(state)
        else:
            stack_price_check.append(state)

        if len(stack_price_check) >= 3:
            if stack_price_check[-1] == "UP":
                if num_of_stock > 0 :
                    SM += num_of_stock * i 
                    num_of_stock = 0

            if stack_price_check[-1] == "DOWN":
                if SM >= i:
                    num_of_stock += SM // i
                    SM = SM % i
                
        prev_price = i
    
    return SM + MachineDuck[-1] * num_of_stock

JH = check_BNP(JH)
SM = check_33(SM)

if JH < SM:
    print("TIMING")
elif JH > SM : 
    print("BNP")
else:
    print("SAMESAME")