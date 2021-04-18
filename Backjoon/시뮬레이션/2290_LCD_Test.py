def row_blank(num):
    return ' '*(num+2)

def row(num):
    return ' '+'-'*num+' '

def column(num):
    return '|'+' '*num+'|'

def column_r(num):
    return ' '*(num+1)+'|'

def column_l(num):
    return '|'+' '*(num+1)


n, num = map(int, input().split())
num = str(num)
one = [row_blank(n), column_r(n), row_blank(n), column_r(n), row_blank(n) ]
two = [row(n), column_r(n), row(n), column_l(n), row(n)]
three = [row(n), column_r(n), row(n), column_r(n), row(n)]
four = [row_blank(n), column(n), row(n), column_r(n), row_blank(n)]
five = [row(n), column_l(n), row(n), column_r(n), row(n)]
six = [row(n), column_l(n), row(n), column(n), row(n)]
seven = [row(n), column_r(n), row_blank(n), column_r(n), row_blank(n)]
eight = [row(n), column(n), row(n), column(n), row(n)]
nine = [row(n), column(n), row(n), column_r(n), row(n)]
zero = [row(n), column(n), row_blank(n), column(n), row(n)]

table = {'1':one, '2':two, '3':three, '4':four, '5':five, '6':six, '7':seven, '8':eight, '9':nine, '0':zero}

idx = 0

while idx < 5:
    if idx == 0 or idx == 2 or idx == 4:
        s = ''
        for i in num:
            s += table[i][idx] + ' '
        
        print(s)
        idx += 1
    else:
        for _ in range(n):
            s = ''
            for i in num:
                s += table[i][idx] + ' '
            print(s)
        idx += 1
