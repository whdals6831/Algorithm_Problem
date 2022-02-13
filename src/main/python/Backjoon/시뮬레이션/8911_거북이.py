from sys import stdin

t = int(input())
commands = [stdin.readline().rstrip() for _ in range(t)]
answer = []

for command in commands:
    visit_x = [False]*1001
    visit_y = [False]*1001
    x = 500
    y = 500
    w = 0
    h = 0
    visit_x[x] = True
    visit_y[y] = True
    four_direction = {
        'up':True,
        'down':False,
        'left':False,
        'right':False
    }

    for d in command:
        if four_direction['up']:
            if d == 'F':
                y += 1
                if not visit_y[y]:
                    visit_x[x] = True
                    visit_y[y] = True
                    h += 1
            if d == 'B':
                y -= 1
                if not visit_y[y]:
                    visit_x[x] = True
                    visit_y[y] = True
                    h += 1
            if d == 'L':
                four_direction['up'] = False
                four_direction['left'] = True
            if d == 'R':
                four_direction['up'] = False
                four_direction['right'] = True
        elif four_direction['down']:
            if d == 'F':
                y -= 1
                if not visit_y[y]:
                    visit_x[x] = True
                    visit_y[y] = True
                    h += 1
            if d == 'B':
                y += 1
                if not visit_y[y]:
                    visit_x[x] = True
                    visit_y[y] = True
                    h += 1
            if d == 'L':
                four_direction['down'] = False
                four_direction['right'] = True
            if d == 'R':
                four_direction['down'] = False
                four_direction['left'] = True
        elif four_direction['left']:
            if d == 'F':
                x -= 1
                if not visit_x[x]:
                    visit_x[x] = True
                    visit_y[y] = True
                    w += 1
            if d == 'B':
                x += 1
                if not visit_x[x]:
                    visit_x[x] = True
                    visit_y[y] = True
                    w += 1
            if d == 'L':
                four_direction['left'] = False
                four_direction['down'] = True
            if d == 'R':
                four_direction['left'] = False
                four_direction['up'] = True
        elif four_direction['right']:
            if d == 'F':
                x += 1
                if not visit_x[x]:
                    visit_x[x] = True
                    visit_y[y] = True
                    w += 1
            if d == 'B':
                x -= 1
                if not visit_x[x]:
                    visit_x[x] = True
                    visit_y[y] = True
                    w += 1
            if d == 'L':
                four_direction['right'] = False
                four_direction['up'] = True
            if d == 'R':
                four_direction['right'] = False
                four_direction['down'] = True

    answer.append(w*h)

print(*answer, sep='\n')