var = input().split()
var_name = [0]

for i in range(1,len(var)):
    var_name_idx = len(var[i])
    for k, j in enumerate(var[i]):
        if not j.isalpha():
            var_name_idx = k
            break
    var_name.append(var[i][:var_name_idx])
    var[i] = var[i][var_name_idx:-1][::-1] # 문자열 reverse = s[::-1]
    s = ""
    for j in var[i]:
        if j == "[":
            j = "]"
        elif j == "]":
            j = "["
        s += j
    var[i] = s

idx = 1

for _ in range(len(var_name)-1):
    print(var[0] + var[idx] + ' ' + var_name[idx] + ";")
    idx += 1