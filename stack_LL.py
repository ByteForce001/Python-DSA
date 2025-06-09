class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        n = Node(item)
        n.next = self.top
        self.top = n

    def pop(self):
        if self.top is None:
            return "Stack Underflow"
        item = self.top.data
        self.top = self.top.next
        return item

    def display(self):
        temp = self.top
        print("Stack:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Example usage:
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Popped:", s.pop())
s.display()
