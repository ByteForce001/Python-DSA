from array import array

class CircularQueue:
    def __init__(self, size):
        self.q = array('i', [0]*size)
        self.size = size
        self.front = -1
        self.rear = -1

    def insert(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow")
            return
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = item

    def delete(self):
        if self.front == -1:
            return "Queue Underflow"
        item = self.q[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return
        i = self.front
        print("Queue:", end=" ")
        while True:
            print(self.q[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

# Example usage:
cq = CircularQueue(5)
cq.insert(10)
cq.insert(20)
cq.insert(30)
cq.display()
print("Deleted:", cq.delete())
cq.display()
