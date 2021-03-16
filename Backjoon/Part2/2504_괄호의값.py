# 스택의 응용
bracket = list(input())

def isBracket(bracket):
    temp = []

    for i in bracket:
        if i == '[' or i == '(':
            temp.append(i)
        else :
            if temp :
                if i == ']' and temp.pop() == '[':
                    continue
                elif i == ')' and temp.pop() == '(':
                    continue  
                else:
                    return False  
            else :
                return False
    
    if temp:
        return False
    else:
        return True

def value_of_bracket(bracket):
    stack = []

    for s in bracket:
        # print(stack)
        if s == '[' or s == '(':
            stack.append(s)
        elif s == ')':
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                tmp = 0

                for i in range(len(stack)-1, -1, -1):
                    if stack[i] == '(':
                        stack[-1] = tmp * 2
                        break
                    else:
                        tmp += stack[i]
                        stack = stack[:-1]
        elif s == ']':
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                tmp = 0

                for i in range(len(stack)-1, -1, -1):
                    if stack[i] == '[':
                        stack[-1] = tmp * 3
                        break
                    else:
                        tmp += stack[i]
                        stack = stack[:-1]
    
    return sum(stack)
                        
if isBracket(bracket):
    print(value_of_bracket(bracket))
else :
    print(0)