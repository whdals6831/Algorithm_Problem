n, k = map(int, input().split())
item_info = []
max_value_list = [[0] * (k+1) for _ in range(n+1)]


for _ in range(n):
    item_info.append(list(map(int, input().split())))

idx = 0
for (weight, value) in item_info:
    idx += 1
    for i in range(1, k+1):
        max_value_list[idx][i] = max_value_list[idx-1][i]
        if i >= weight and max_value_list[idx][i] < value + max_value_list[idx-1][i-weight]:
            max_value_list[idx][i] = value + max_value_list[idx-1][i-weight]

print(max_value_list[n][k])