# 위상 정렬
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
student_key_pair = [[] for _ in range(n+1)]
enter_degree = [ 0 for _ in range(n+1)]
edge = deque()
answer = []

# 각 학생 인덱스에 자기 앞에 올 수 있는 학생 번호 저장
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    student_key_pair[b].append(a)
    # 자기 앞에 있는 학생의 차수를 +1
    enter_degree[a] += 1

# 차수가 0 (자신 뒤에 다른 학생이 없음)인 학생을 q에 삽입
for i, v in enumerate(enter_degree[1:]):
    if v == 0:
        edge.append(i+1)

# 학생이 존재하지 않을 때까지 반복
while edge:
    student = edge.popleft()
    answer.append(student)

    # 현재 선택된 학생이 가리키는 학생의 차수를 -1
    for s in student_key_pair[student]:
        enter_degree[s] -= 1

        if enter_degree[s] == 0:
            edge.append(s)

temp = ''

for i in range(len(answer)-1,-1,-1):
    temp += f'{answer[i]} '

print(temp)