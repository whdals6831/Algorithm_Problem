# 시뮬레이션 기본
h, w = map(int, input().split())
block = list(map(int, input().split()))
space = [[0]*w for _ in range(h)]
total = 0

for i, x in enumerate(space):
    for j, _ in enumerate(x):
        if block[j] > 0:
            space[i][j] = 1
            block[j] -= 1

for x in space:
    rain = 0
    flag = False

    for y in x:
        if y == 1 and not flag:
            flag = True
        elif y == 1 and flag :
            total += rain
            rain = 0

        if y == 0 and flag:
            rain += 1
        
print(total)