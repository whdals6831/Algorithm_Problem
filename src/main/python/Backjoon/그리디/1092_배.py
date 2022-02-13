from sys import stdin

n = int(input())
crane = list(map(int, stdin.readline().split()))
m = int(input())
box = list(map(int, stdin.readline().split()))

crane.sort(reverse=True)
box.sort(reverse=True)
time = 0

while len(box) > 0:
    now_crane = 0
    del_idx = []

    for i, w in enumerate(box):
        if crane[now_crane] >= w:
            del_idx.append(i)
            now_crane += 1

            if now_crane == n:
                break

    if len(del_idx) == 0: # 모든 박스를 배로 옮길 수 없는 경우
        time = -1
        break
    else:
        time += 1
        # del 함수를 쓰면 배열이 밀리기 때문에 이런 방식으로 제거
        for i in del_idx: 
            box[i] = -1
        for i in range(len(del_idx)):
            box.remove(-1)

print(time)