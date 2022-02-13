import sys

input = sys.stdin.readline

class Stack :

    def __init__(self) :
        self.list = []
        self.last_index = -1



    def process_stack(self, command):
        if command[0] == 'push' :
            self.stack_push(command[1])
        elif command[0] == 'top' :
            self.stack_top()
        elif command[0] == 'pop' :
            self.stack_pop()
        elif command[0] == 'size' :
            self.stack_size()
        elif command[0] == 'empty' :
            self.stack_empty()



    def stack_push(self, value) :
        zero_list = [0 for i in range(self.last_index+2)]
        index = 0

        for i in self.list :
            zero_list[index] = i
            index += 1
        
        zero_list[self.last_index+1] = value

        self.last_index += 1
        self.list = zero_list
        



    def stack_top(self) :
        if self.get_length(self.list) == 0 :
            return print(-1)
        return print(self.list[self.last_index])



    def stack_pop(self) :
        if self.get_length(self.list) == 0 :
            return print(-1)
            
        pop_value = self.list[self.last_index]

        if self.last_index == 0 :
            self.list = []
            self.last_index -= 1
            return print(pop_value)
        else :
            zero_list = [0 for i in range(self.last_index+1)]

            for i in range(self.last_index+1) :
                zero_list[i] = self.list[i]

            self.last_index -= 1
            self.list = zero_list
            return print(pop_value)


    def stack_size(self) :
        return print(self.last_index + 1)



    def stack_empty(self) :
        if self.get_length(self.list) == 0 :
            return print(1)
        return print(0)



    def get_length(self, list) :
        n = 0
        for _ in self.list :
            n += 1
        return n
    


def main() :
    stack = Stack() 

    n = int(input())
    
    for _ in range(n):
        command = input().split()
        stack.process_stack(command)

main()