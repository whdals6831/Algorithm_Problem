import sys

input = sys.stdin.readline

n = int(input())

meeting_time_list = []

for _ in range(n) :
    start_meeting_time, end_meeting_time = map(int, input().split())
    meeting_time_list.append([start_meeting_time, end_meeting_time])

# 끝나는 시간을 기준으로 정렬, 그 후 시작시간으로 정렬(시작시간과 끝나는 시간이 같은 case 때문에)
meeting_time_list = sorted(meeting_time_list, key=lambda meeting_time: (meeting_time[1], meeting_time[0]))

last_time = 0
max_meeting_cnt = 0

for meeting_time in meeting_time_list :
    if meeting_time[0] >= last_time :
        last_time = meeting_time[1]
        max_meeting_cnt += 1

print(max_meeting_cnt)