import sys

input = sys.stdin.readline

class Queue :

    def __init__(self) :
        self.list = []
        self.last_index = -1



    def process_queue(self, command):
        if command[0] == 'push' :
            self.queue_push(command[1])
        elif command[0] == 'front' :
            self.queue_front()
        elif command[0] == 'pop' :
            self.queue_pop()
        elif command[0] == 'size' :
            self.queue_size()
        elif command[0] == 'empty' :
            self.queue_empty()
        elif command[0] == 'back' :
            self.queue_back()



    def queue_push(self, value) :
        zero_list = [0 for i in range(self.last_index + 2)]

        index = 0

        for i in self.list :
            zero_list[index] = i
            index += 1
        
        self.last_index += 1
        zero_list[self.last_index] = value
        self.list = zero_list



    def queue_front(self) :
        if self.get_length(self.list) == 0 :
            return print(-1)

        return print(self.list[0])



    def queue_pop(self) :
        if self.get_length(self.list) == 0 :
            return print(-1)
        
        pop_value = self.list[0]

        if self.last_index == 0 :
            self.list = []
            self.last_index -= 1
            return print(pop_value)
        else :
            zero_list = [0 for i in range(self.last_index+1)]

            for i in range(self.last_index) :
                zero_list[i] = self.list[i+1]

            self.last_index -= 1
        
        self.list = zero_list
        return print(pop_value)



    def queue_size(self) :
        return print(self.last_index+1)



    def queue_empty(self) :
        if self.get_length(self.list) == 0 :
            return print(1)
        return print(0)



    def queue_back(self) :
        if self.get_length(self.list) == 0 :
            return print(-1)
        
        return print(self.list[self.last_index])



    def get_length(self, list) :
        n = 0
        for _ in self.list :
            n += 1
        return n
    


def main() :
    queue = Queue() 

    n = int(input())
    
    for _ in range(n):
        command = input().split()
        queue.process_queue(command)

main()