n, k = map(int, input().split())
electrical_appliance = list(map(int, input().split()))
multi_tap = [0 for _ in range(n)]
priority = [[0,0] for _ in range(n)]
pop_count = 0

for i, v in enumerate(electrical_appliance):
    # 멀티탭에 빈공간이 있을 경우
    if 0 in multi_tap and v not in multi_tap:
        multi_tap[multi_tap.index(0)] = v
    # 멀티탭에 빈공간이 없을 경우
    else:
        # 다음 사용할 전기용품이 멀티탭에 꽂혀있을 경우 
        if v in multi_tap:
            continue
        # 다음 사용할 전기용품이 멀티탭에 꽂혀있지 않을 경우 
        else:
            for j, m in enumerate(multi_tap):
                # 뽑힐 전기용품의 우선순위를 정하기 위해 
                try:
                    priority[j][0] = electrical_appliance[i+1:k].index(m)
                    priority[j][1] = m
                except:
                    priority[j][0] = 101
                    priority[j][1] = m
            
            temp = [-1, 0]
            
            # 우선순위가 높으면 교환
            for p in priority:
                if p[0] > temp[0]:
                    temp = p
            
            multi_tap[multi_tap.index(temp[1])] = v 
            pop_count += 1

print(pop_count)