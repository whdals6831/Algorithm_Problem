a, b = map(int, input().split())
isAnswer = False
min_cnt = float('inf')

def dfs(a, b, cnt):
    if a > b:
        return
    elif a == b:
        global isAnswer
        global min_cnt
        isAnswer = True
        min_cnt = min(min_cnt, cnt)
        return
    else:
        dfs(a*2, b, cnt+1)
        dfs(a*10+1,b, cnt+1)

dfs(a, b, 1)

if isAnswer:
    print(min_cnt)
else:
    print(-1)