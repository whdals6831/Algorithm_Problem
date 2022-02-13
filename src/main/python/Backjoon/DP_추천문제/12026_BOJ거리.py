import math

n = int(input())
boj = ['B','O','J']
boj_list = list(input())
energy = [float('inf')] * n
energy[0] = 0

for i in range(n):
    for j in range(i):
        # 현재 지점 전단계를 모두 탐색하여
        # 전단계의 에너지 값과 현재 지점까지 소비되는 에너지의 값의 최소값을 삽입
        if boj_list[j] == boj[(boj.index(boj_list[i])+2)%3]:
            energy[i] = min(energy[i], energy[j]+(i-j)*(i-j))

if not math.isinf(energy[n-1]):
    print(energy[n-1])
else:
    print(-1)