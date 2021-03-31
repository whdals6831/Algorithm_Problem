from collections import deque

s = list(input())
p = list(input())

s_begin = 0
p_begin = 0
begin_checkpoint = deque()
end_check = False

while s_begin+len(p)-p_begin <= len(s):
    if s[s_begin] == p[p_begin]:
        # 접두사와 접미사가 동일한 경우를 다 넣어준다.
        if s[s_begin] == p[0] and s[s_begin+len(p)] == p[-1]:
            begin_checkpoint.append(s_begin)

        s_begin += 1
        p_begin += 1

        if p_begin >= len(p):
            end_check = True
            break
    else:
        if begin_checkpoint:
            s_begin = begin_checkpoint.popleft()
        else:
            s_begin += 1
        p_begin = 0

if end_check:
    print(1)
else:
    print(0)