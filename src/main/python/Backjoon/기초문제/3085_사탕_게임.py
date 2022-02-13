import sys

n = int(input())

candy_list = []
x = [1,0,-1,0]
y = [0,1,0,-1]

visit = [[False]*n for _ in range(n)]

for _ in range(n):
    candy_list.append(list(sys.stdin.readline().rstrip()))

def find_max_candy(candy_list, start_i, start_j, next_i, next_j):
    max_candy = 1

    for i in range(start_i,next_i+1):
        before = ''
        temp = 0
        for j in range(len(candy_list)):
            if candy_list[i][j] == before:
                temp += 1
            else:
                temp = 1
            max_candy = max(max_candy, temp)
            before = candy_list[i][j] 

    for i in range(start_j,next_j+1):
        before = ''
        temp = 0
        for j in range(len(candy_list)):
            if candy_list[j][i] == before:
                temp += 1
            else:
                temp = 1
            max_candy = max(max_candy, temp)
            before = candy_list[j][i]        

    return(max_candy)

answer = 1

for i in range(len(candy_list)):
    for j in range(len(candy_list)):
        visit[i][j] = True

        for k in range(4):
            if x[k]+i < 0 or x[k]+i > len(candy_list)-1 or y[k]+j < 0 or y[k]+j > len(candy_list)-1 or visit[i+x[k]][j+y[k]]:
                continue
            else:
                # 사탕 교환
                candy_list[i][j], candy_list[i+x[k]][j+y[k]] = candy_list[i+x[k]][j+y[k]], candy_list[i][j]
                answer = max(answer, find_max_candy(candy_list, i, j, i+x[k], j+y[k]))
                # 원래 대로
                candy_list[i][j], candy_list[i+x[k]][j+y[k]] = candy_list[i+x[k]][j+y[k]], candy_list[i][j]

print(answer)
