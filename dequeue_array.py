from array import array

class Deque:
    def __init__(self, size):
        self.q = array('i', [0]*size)
        self.size = size
        self.front = -1
        self.rear = -1

    def insert_front(self, item):
        if (self.front - 1) % self.size == self.rear:
            print("Overflow")
            return
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.size) % self.size
        self.q[self.front] = item

    def insert_rear(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Overflow")
            return
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = item

    def delete_front(self):
        if self.front == -1:
            return "Underflow"
        item = self.q[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item

    def delete_rear(self):
        if self.front == -1:
            return "Underflow"
        item = self.q[self.rear]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.size) % self.size
        return item

    def display(self):
        if self.front == -1:
            print("Deque is empty")
            return
        i = self.front
        print("Deque:", end=" ")
        while True:
            print(self.q[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

# Example usage:
d = Deque(5)
d.insert_rear(10)
d.insert_front(5)
d.insert_rear(15)
d.display()
print("Deleted front:", d.delete_front())
print("Deleted rear:", d.delete_rear())
d.display()
