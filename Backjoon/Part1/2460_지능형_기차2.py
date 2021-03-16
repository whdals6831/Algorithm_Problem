max = 0
remain_person = 0

for _ in range(0, 10):
    get_out, get_in = map(int, input().split())
    remain_person -= get_out
    remain_person += get_in

    if max < remain_person:
        max = remain_person

print(max)