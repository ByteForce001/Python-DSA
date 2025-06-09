from array import array

class Queue:
    def __init__(self, size):
        self.q = array('i', [0]*size)
        self.front = 0
        self.rear = 0
        self.size = size

    def insert(self, item):
        if self.rear >= self.size:
            print("Queue Overflow")
            return
        self.q[self.rear] = item
        self.rear += 1

    def delete(self):
        if self.front == self.rear:
            return "Queue Underflow"
        item = self.q[self.front]
        for i in range(self.rear - 1):
            self.q[i] = self.q[i + 1]
        self.rear -= 1
        return item

    def display(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            print("Queue:", [self.q[i] for i in range(self.front, self.rear)])

# Example usage:
q = Queue(size=5)
q.insert(10)
q.insert(20)
q.insert(30)
q.display()
print("Deleted:", q.delete())
q.display()
