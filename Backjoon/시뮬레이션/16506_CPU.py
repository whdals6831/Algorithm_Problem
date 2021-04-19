table = {'ADD':'000000', 'ADDC':'000010', 'SUB':'000100', 'SUBC':'000110', 'MOV':'001000', 'MOVC':'001010', 'AND':'001100', 'ANDC':'001110', 'OR':'010000', 'ORC':'010010', 'NOT':'010100', 'MULT':'011000', 'MULTC':'011010', 'LSFTL':'011100', 'LSFTLC':'011110', 'LSFTR':'100000', 'LSFTRC':'100010', 'ASFTR':'100100', 'ASFTRC':'100110', 'RL':'101000', 'RLC':'101010', 'RR':'101100', 'RRC':'101110'}

n = int(input())
answer = []

def make_bin(num, d):
    num = format(int(num), 'b')
    if len(num) < d:
        num = '0'*(d-len(num)) + num
    return num

for _ in range(n):
    result = ''
    op, rd, ra, rb = input().split()

    # op
    result += table[op]

    # rd
    result += make_bin(rd, 3)

    # ra
    if op == 'MOV' or op == 'MOVC' or op == 'NOT':
        result += '000'
    else:
        result += make_bin(ra, 3)

    # rb
    ex_list = ['ADD', 'SUB', 'MOV', 'AND', 'OR', 'NOT', 'MULT', 'LSFTL', 'LSFTR', 'ASFTR', 'RL', 'RR']

    if op in ex_list:
        result += make_bin(rb, 3) + '0'
    else:
        result += make_bin(rb, 4)

    answer.append(result)

print(*answer, sep='\n')