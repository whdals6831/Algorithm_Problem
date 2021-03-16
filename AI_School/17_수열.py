# 1 = 132
# 2 = 211
# 3 = 232

start_num = input()
second = int(input())
left = int(input())
right = int(input())

num = ['1', '2', '3']
change_num = ['132', '211', '232']

changed_num = start_num

for _ in range(second) :
    temp = ''
    for n in changed_num :
        change_idx = num.index(n)
        temp += change_num[change_idx]
    changed_num = temp
    print(changed_num)
