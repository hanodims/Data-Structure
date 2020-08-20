import random
class Node:
    def __init__(self, color, num, next_node=None):
        self.color = color
        self.num = num
        self.next_node = next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node
    
    def get_next_node(self):
        return self.next_node
    
    def get_color(self):
        return self.color
    
    def get_num(self):
        return self.num

class Stack:

    def __init__(self, limit=1000):
        self.top_node = None
        self.size = 0
        self.limit = limit

    def is_full(self):
        return self.size == self.limit
    
    def is_empty(self):
        return self.size == 0

  
    def push(self,color,num):
        if not self.is_full():
            item = Node(color,num)
            item.set_next_node(self.top_node)
            self.top_node = item
            self.size += 1
        else:
            print("Nothing to see here, move along.")
    
    def pop(self):
        if not self.is_empty():
            popped = self.top_node
            self.top_node = popped.get_next_node()
            self.size -= 1
            return popped.get_color(),popped.get_num()
        else:
            print("WOW! Easy there buddy, it's a full house.")
  
    def peek(self):
        if not self.is_empty():
	        return self.top_node.get_color() , self.top_node.get_num()
        else:
            print("Nothing to see here, move along.")




deck = Stack(20)
colors = ["Red","Yellow","Blue","Green"]

for i in range(1,21):
    deck.push(colors[random.randint(0,3)],random.randint(1, 20))
    
    

print("-"*15)
print("player 1:")
print("-"*15)

player1 = []
for i in range(1,6):
    player1.append(deck.pop())
    print(f"{i} {player1[i-1][0]}-{player1[i-1][1]}")


print("-"*15)
print("player 2:")
print("-"*15)

player2 = []
for i in range(1,6):
    player2.append(deck.pop())
    print(f"{i} {player2[i-1][0]}-{player2[i-1][1]}")


print("-"*15)
print(f"First card in deck: {deck.peek()}")
print("-"*15)

