import sys

n = int(input())
num_list = []

# 내장함수의 정렬은 nlogn으로 구성되어 있기 때문에 충분히 성능은 좋음
# 이 문제는 구현보다 입력이 많아서 sys를 사용해 입력을 받아야 통과가 가능했다.

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

for i in sorted(num_list):
    sys.stdout.write(str(i) + '\n')