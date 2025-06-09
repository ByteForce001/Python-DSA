class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
        else:
            temp = self.head
            while temp.next: temp = temp.next
            temp.next = n

    def insert_front(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev, temp = temp, temp.next
        if temp: prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def count(self):
        c, temp = 0, self.head
        while temp: c, temp = c + 1, temp.next
        return c

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key: return True
            temp = temp.next
        return False

# Example usage:
ll = LinkedList()
ll.insert_end(10)
ll.insert_front(5)
ll.insert_end(20)
ll.display()
print("Count:", ll.count())
print("Search 20:", ll.search(20))
ll.delete(10)
ll.display()
