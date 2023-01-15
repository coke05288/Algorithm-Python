## Stack & Queue
## Baekjoon 2161 카드1
## https://www.acmicpc.net/problem/2161
from collections import deque

Card = deque([i+1 for i in range(int(input()))])
Left = []

while Card:
    print(Card.popleft(), end = " ")
    if(Card):
        Card.append(Card.popleft())