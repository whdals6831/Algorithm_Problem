# 재귀 탐색의 기본
from copy import deepcopy

op = ["+", "-", "*", "/"]

min = float("inf")
max = float("-inf")

def calc(a, op, b):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        if a < 0:
            a = -a
            return -(a//b)
        else:
            return a//b

def DFS(n, num_list, idx, operators, sum):
    global max, min

    if n == idx:
        if max < sum:
            max = sum
        if min > sum:
            min = sum
        return
    
    for i in range(4):
        # operators의 감소한 배열 값을 재귀에 넘겨줘야 되기 때문에 deepcopy사용
        copied_operators = deepcopy(operators)

        if copied_operators[i] > 0:
            copied_operators[i] -= 1
            DFS(n, num_list, idx+1, copied_operators, calc(sum, op[i], num_list[idx]))

def solve():
    n = int(input())
    num_list = list(map(int, input().split()))
    operators = list(map(int, input().split()))

    DFS(n, num_list, 1, operators, num_list[0])

    print(max)
    print(min)

if __name__ == "__main__":
    solve()