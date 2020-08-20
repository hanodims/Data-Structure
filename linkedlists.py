class Node:
    def __init__(self, age, hiL, next_node=None):
        self.age = age
        self.hiL = hiL
        self.next_node = next_node
  
    def get_age(self):
        return self.age

    def get_hiL(self):
        return self.hiL
  
    def get_next_node(self):
        return self.next_node
  
    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, age=None, hiL=None):
        self.head_node = Node(age,hiL)
    
    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_age,new_hiL):
        new_node = Node(new_age,new_hiL) 
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def get_data(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_age() != None:
                string_list += "Age: "+ str(current_node.get_age()) + " HighLight: " + str(current_node.get_hiL())+ "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self,age):
        current_node = self.get_head_node()
        if current_node.get_age() == age:
            self.head_node = current_node.get_next_node()
        else:
         while current_node:
            next_node = current_node.get_next_node()
            if next_node.get_age() == age:
                current_node.set_next_node(next_node.get_next_node())
                current_node = None
            else:
                current_node = next_node
                    
    def find(self,i):
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_age() == i:
                return False
            current_node = current_node.get_next_node()
        return True
    
    def where(self,i):
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_age() == i:
                return current_node
            current_node = current_node.get_next_node()
        return True




print()
a = LinkedList(1,'I was born')
a.insert_beginning(4,'I started Learning')
a.insert_beginning(3,'I started walking')
a.insert_beginning(7,'I turned Seven')
print(a.get_data())
a.find(2)
#a.remove_node(3)
#print(a.where(1).get_hiL())
#print(a.get_data())
ag = input('How old are you now? ')
ag = int(ag)

for i in range(ag):
    counter = ag
    while(counter>0):
        if a.find(counter) == False:
            first = a.where(counter).get_age()
            sec = a.where(counter).get_hiL()
            a.remove_node(counter)
            a.insert_beginning(first,sec)
           
        elif a.find(counter):
            highlight = input("What happend at your %s age? " % str(counter))
            a.insert_beginning(counter,highlight)
        counter -= 1
print()   
print(a.get_data())


#print(a.find(1)+"ss")




  
   
