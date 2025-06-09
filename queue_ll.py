class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def insert(self, item):
        n = Node(item)
        if self.rear is None:
            self.front = self.rear = n
        else:
            self.rear.next = n
            self.rear = n

    def delete(self):
        if self.front is None:
            return "Queue Underflow"
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return item

    def display(self):
        temp = self.front
        print("Queue:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Example usage:
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
q.display()
print("Deleted:", q.delete())
q.display()
