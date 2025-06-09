from array import array

class Stack:
    def __init__(self):
        self.stack = array('i')  # integer stack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack: return self.stack.pop()
        return "Stack is empty"

    def display(self):
        print("Stack:", list(reversed(self.stack)))

# Example usage:
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Popped:", s.pop())
s.display()
