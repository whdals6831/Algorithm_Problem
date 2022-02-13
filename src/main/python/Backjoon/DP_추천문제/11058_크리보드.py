n = int(input())
view = [0] * 101
jump_idx = 4
clipboard = 0

for i in range(1,7):
    view[i] = i

for i in range(7, 101):
    for j in range(1, i-2):
        # 예를 들어 i가 9일 때 
        # i = 4 에서 복붙 시작 -> 16
        # i가 5에서나 6에서 붙혀넣기 한 값보다 크다.
        view[i] = max(view[i], view[i-1]+1, view[i-(j+2)]*(j+1))

print(view[n])