# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

def DFS(v, adj_arr, visit, n):
    print(v, end=" ")
    visit[v] = True

    for i in range(1, n+1):
        if adj_arr[v][i] == 1 and not visit[i]:
            DFS(i, adj_arr, visit, n)


def BFS(v, adj_arr, visit_q, n):
    queue = [0] * (n+1)
    f_idx = 0
    r_idx = 1
    queue[f_idx] = v
    visit_q[v] = True

    while f_idx < r_idx:
        now_node = queue[f_idx]
        f_idx += 1
        print(now_node, end=" ")

        for i in range(1, n+1):
            if adj_arr[now_node][i] == 1 and not visit_q[i]:
                queue[r_idx] = i
                r_idx += 1
                visit_q[i] = True

# deque를 적극 활용해도됨

n, m, v = map(int, input().split())
adj_arr = [[0] * (n+1) for _ in range(n+1)]
visit = [False] * (n+1)
visit_q = [False] * (n+1)


for _ in range(m):
    v1, v2 = map(int, input().split())
    adj_arr[v1][v2] = 1
    adj_arr[v2][v1] = 1


DFS(v, adj_arr, visit, n)
print()
BFS(v, adj_arr, visit_q, n)