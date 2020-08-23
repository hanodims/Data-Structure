class Node:
    def __init__(self, group, num, next_node=None):
        self.group = group
        self.num = num
        self.next_node = next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node
    
    def get_next_node(self):
        return self.next_node
    
    def get_group(self):
        return self.group

    def get_num(self):
        return self.num
    
    


class Queue:
    def __init__(self, limit=None):
        self.front_node = None
        self.back_node = None
        self.length = 0
        self.limit = limit
    
    def is_full(self):
        return self.length == self.limit if self.limit else False

    def is_empty(self):
        return self.length == 0
    
    def get_length(self):
        return self.length
    

    def peek(self):
        if self.is_empty():
            print("Nothing to see here, move along.")
        else:
            return self.front_node.get_group() , self.front_node.get_num()

    def enqueue(self, group,num):
        if not self.is_full():
            new_node = Node(group,num)
            if self.is_empty():
                self.front_node = new_node
                self.back_node = new_node
            else:
                self.back_node.set_next_node(new_node)
                self.back_node = new_node
            self.length += 1
        else:
            print("Eww go away, there's no more room!")

    def dequeue(self):
        if not self.is_empty():
            removed_node = self.front_node
            if self.get_length() == 1:
                self.front_node = None
                self.back_node = None
            if self.get_length() > 1:
                 self.front_node = removed_node.get_next_node()
            self.length -= 1
            return removed_node.get_group(),removed_node.get_num()
        else:
            print("Ya basic! Nothing here nerd!")

    #To print q elemnts
    def display(self):
        m = self.get_length()
        current = self.front_node
        for i in range(1,self.get_length()+1):
            if m > 0:
                print(f"Group: {current.get_group()}, Members#: {current.get_num()}")
                current = current.get_next_node()
                m -= 1
            else : break
    
        
#------------------------

waiting_time = 0
groups = [[1,41]]
q = Queue(4)
for i in range(0,len(groups)):
    group = groups[i][1]
    count = groups[i][1]

    if group <=12 and count > 0:
        q.enqueue(groups[i][0],groups[i][1])
        waiting_time += 30
    else:
        while count > 0:
            if count > 12:
                if not q.front_node == None:
                    q.enqueue(q.back_node.get_group()+1,12)   
                else: q.enqueue(groups[i][0],12)   
                waiting_time += 30
            else:
                q.enqueue(q.back_node.get_group()+1,count)
                waiting_time += 30
            count -= 12

#-----------------------------------------------            
print(f"Waiting times= {waiting_time/60} mins")
q.display()
print(f"Size: {q.get_length()}")
q.dequeue()
waiting_time -= 30
print(f"Waiting times= {waiting_time/60} mins")
q.display()
print(f"Size: {q.get_length()}")




        
            










