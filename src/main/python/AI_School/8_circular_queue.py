# import sys
# input = sys.stdin.readline

class Queue:
    def __init__(self, length):
        self.length = length+1
        self.array_list = [0 for _ in range(length+1)]
        self.f_idx = 0
        self.b_idx = 0

    def is_full(self) :
        return (self.b_idx + 1) % self.length == self.f_idx
    
    def push(self, value):

        if self.is_full() :
            return -1
        
        self.b_idx = (self.b_idx + 1) % self.length
        self.array_list[self.b_idx] = value

        print(self.array_list)

        
    
    def pop(self):
        if self.size() == 0:
            return -1
        
        self.f_idx = (self.f_idx + 1) % self.length
        pop_val = self.array_list[self.f_idx]
        self.array_list[self.f_idx] = 0
        
        print(self.array_list)
        return pop_val
    
    def size(self):
        return (self.b_idx - self.f_idx + self.length) % self.length
    
    def empty(self):
        # return int(self.size() <= 0)
        if self.size() == 0:
            return 1
        
        return 0
    
    def front(self):
        if self.size() == 0:
            return -1
            
        return self.array_list[self.f_idx+1]


    def back(self):
        if self.size() == 0:
            return -1
        
        return self.array_list[self.b_idx]

def process_queue(queue_list, command):
    cmd = command[0]
    if cmd == "push":
        if queue_list.push(command[1]) is not None :
            print("full list!")
    elif cmd == "pop":
        print(queue_list.pop())
    elif cmd == "size":
        print(queue_list.size())
    elif cmd == "empty":
        print(queue_list.empty())
    elif cmd == "front":
        print(queue_list.front())
    elif cmd == "back":
        print(queue_list.back())
 
n = int(input())
queue_list = Queue(length=4)

for _ in range(n):
    command = input().split()
    process_queue(queue_list, command)