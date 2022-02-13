from collections import deque

n = int(input())
signal = list(input())
sort_signal = []
idx = 0
jump = n//5
visit = [[0]*(jump+2) for _ in range(7)]
answer = ''
pattern_table = [['-1']*100 for _ in range(100)]

# pattern table
pattern_table[5][14] = '1'
pattern_table[11][65] = '2'
pattern_table[11][57] = '3'
pattern_table[9][40] = '4'
pattern_table[11][49] = '5'
pattern_table[12][47] = '6'
pattern_table[7][27] = '7'
pattern_table[13][51] = '8'
pattern_table[12][53] = '9'


# signal 2차원 배열로 만들어주기
sort_signal.append(['.']*(jump+2))
for _ in range(5):
    sort_signal.append(list('.' + ''.join(signal[idx:idx+jump]) + '.'))
    idx += jump
sort_signal.append(['.']*(jump+2))

# signal pattern 찾기
def bfs(x, y):
    global sort_signal
    global visit
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    block_cnt = 0
    sum_num = 0
    zero_check = True

    while q:
        nx, ny = q.popleft()
        block_cnt += 1

        # 0 가운데 index는 비었기 때문에 이걸 이용해서 0과 6 구별
        if nx == x+2 and ny == y+1:
            zero_check = False 

        for i in range(4):
            if visit[nx+dx[i]][ny+dy[i]] == 0 and sort_signal[nx+dx[i]][ny+dy[i]] == '#':
                q.append([nx+dx[i], ny+dy[i]])
                visit[nx+dx[i]][ny+dy[i]] = visit[nx][ny] + 1
                sum_num += visit[nx+dx[i]][ny+dy[i]]

    return block_cnt, sum_num, zero_check

for i in range(jump+2):
    if sort_signal[1][i] == "#" and visit[1][i] == 0:
        block_cnt, sum_num, zero_check = bfs(1, i)
        # 0하고 6하고 block_cnt, sum_num이 동일해 따로 check
        if block_cnt == 12 and sum_num == 47 and zero_check:
            answer += '0'
        else:
            answer += pattern_table[block_cnt][sum_num]

print(answer)


## 다른 사람 풀이법

# N = int(input()) // 5
# sig = input()
# numbers = dict()
# # 한 columns씩 가져와 pattern 생성
# numbers["######...######"] = "0"
# numbers["#####"] = "1"
# numbers["#.####.#.####.#"] = "2"
# numbers["#.#.##.#.######"] = "3"
# numbers["###....#..#####"] = "4"
# numbers["###.##.#.##.###"] = "5"
# numbers["######.#.##.###"] = "6"
# numbers["#....#....#####"] = "7"
# numbers["######.#.######"] = "8"
# numbers["###.##.#.######"] = "9"
# answer = ""
# cur = ""
# for c in range(N):
#     temp = ""
# # 한 줄씩 temp에 저장하면서 cur에 추가로 저장, "....."이 temp에 저장되면 번호 한개가 끝났으므로 정답 저장
#     for r in range(5):
#         temp += sig[c + r * N]
#     if temp == ".....":
#         if cur:
#             answer += numbers[cur]
#             cur = ""
#     else:
#         cur += temp
# if cur:
#     answer += numbers[cur]
# print(answer)