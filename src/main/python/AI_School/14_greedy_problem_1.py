import sys

input = sys.stdin.readline

money = 1000 - int(input())

remain_money_count = 0

coin = [500, 100, 50, 10, 5, 1]

for i in coin :
    remain_money_count += money // i
    money = money % i

print(remain_money_count)