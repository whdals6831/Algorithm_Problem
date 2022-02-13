import sys

n = int(input())
nn = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
nn_cnt = [[0]*n for _ in range(n)]

nn_cnt[0][0] = 1

for i in range(n):
    for j in range(n):
        if nn_cnt[i][j] > 0:
            if i == n-1 and j == n-1:
                break

            if nn[i][j]+i < n:
                # 해당 지점에 다른 경로에서의 방문이 이미 존재할 때, 현재 지점의 방문수를 더함
                if nn_cnt[nn[i][j]+i][j] > 0:
                    nn_cnt[nn[i][j]+i][j] += nn_cnt[i][j]
                else:
                    nn_cnt[nn[i][j]+i][j] = nn_cnt[i][j]

            if nn[i][j]+j < n:
                if nn_cnt[i][nn[i][j]+j] > 0:
                    nn_cnt[i][nn[i][j]+j] += nn_cnt[i][j]
                else:
                    nn_cnt[i][nn[i][j]+j] = nn_cnt[i][j]

print(nn_cnt[n-1][n-1])