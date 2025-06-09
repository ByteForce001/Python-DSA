class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
        else:
            t = self.head
            while t.next: t = t.next
            t.next, n.prev = n, t

    def insert_front(self, data):
        n = Node(data)
        if self.head:
            self.head.prev = n
            n.next = self.head
        self.head = n

    def delete(self, key):
        t = self.head
        while t and t.data != key: t = t.next
        if not t: return
        if t.prev: t.prev.next = t.next
        else: self.head = t.next
        if t.next: t.next.prev = t.prev

    def display(self):
        t = self.head
        while t:
            print(t.data, end=' ')
            t = t.next
        print()

    def count(self):
        c, t = 0, self.head
        while t: c, t = c + 1, t.next
        return c

    def search(self, key):
        t, i = self.head, 0
        while t:
            if t.data == key: return i
            t, i = t.next, i + 1
        return -1

# Example usage:
dll = DoublyLinkedList()
dll.insert_end(10)
dll.insert_front(5)
dll.insert_end(20)
dll.display()
print("Count:", dll.count())
print("Search 5 at:", dll.search(5))
print("Search 100 at:", dll.search(100))
dll.delete(10)
dll.display()
