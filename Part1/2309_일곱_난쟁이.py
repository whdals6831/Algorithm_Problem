nine_dwarf = []
answer = []

for _ in range(0, 9):
    nine_dwarf.append(int(input()))

left = 0
right = 1

while True:
    total = 0
    for i in range(0, 9):
        if i == left or i == right:
            continue
        
        total += nine_dwarf[i]
    
    if total == 100:
        for i in range(0, 9):
            if i == left or i == right:
                continue
            
            answer.append(nine_dwarf[i])
        break
    else :
        right += 1
        
        if right == 9:
            left += 1
            right = left + 1
    

sorted_answer = sorted(answer)

for i in sorted_answer:
    print(i)
