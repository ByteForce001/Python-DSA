class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if not root:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')

    def find_min(self, root):
        if not root:
            return None
        while root.left:
            root = root.left
        return root.data

    def find_max(self, root):
        if not root:
            return None
        while root.right:
            root = root.right
        return root.data

    def search(self, root, key):
        if not root:
            return False
        if root.data == key:
            return True
        elif key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

# Example usage:
tree = BST()
root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = tree.insert(root, val)

print("Inorder: ", end=''); tree.inorder(root); print()
print("Preorder:", end=' '); tree.preorder(root); print()
print("Postorder:", end=' '); tree.postorder(root); print()
print("Min:", tree.find_min(root))
print("Max:", tree.find_max(root))
print("Search 60:", tree.search(root, 60))
print("Search 25:", tree.search(root, 25))
