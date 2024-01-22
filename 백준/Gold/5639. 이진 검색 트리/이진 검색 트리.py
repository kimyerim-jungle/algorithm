import sys
sys.setrecursionlimit(10010)
    
class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

class BinaryTree:
    
    def __init__(self):
        self.root = None
                   
    def add(self, key):
        
        def add_node(node, key):
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, None, None)
                else:
                    add_node(node.left, key)
                    
            else:
                if node.right is None:
                    node.right = Node(key, None, None)
                else:
                    add_node(node.right, key)
            return True
        
        if self.root is None:
            self.root = Node(key, None, None)
            return True
        else:
            return add_node(self.root, key)
        
    def result(self):
        start = self.root
        
        def postorder(node):
            if node != None:
                postorder(node.left)
                postorder(node.right)
                print(node.key)
            
        postorder(start)
 
tree = BinaryTree()
       
while True:
    try:
        node = sys.stdin.readline().strip()
        if node == '':
            break
        tree.add(int(node))
    except EOFError:
        break
    
tree.result()