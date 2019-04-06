class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self,d):
        if self.value == d:              # Eru þessi gögn þegar fyrir
            return False
        elif self.value > d:             # Förum vinstra megin
            if self.left:                   # Er til leftChild
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True
        else:                               # Förum hægra megin
            if self.right:                  # Er til rightChild
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return True

    def preOrderPrint(self):
        if self == None:
            return
        else:
            print(self.value, end=" ")
            Node.preOrderPrint(self.left)
            Node.preOrderPrint(self.right)

    def postOrderPrint(self):
        if self == None:
            return
        else:
            Node.postOrderPrint(self.left)
            Node.postOrderPrint(self.right)
            print(self.value, end=" ")

    def minValueNode(self): 
        current = self 
      
        # loop down to find the leftmost leaf 
        while(current.left is not None): 
            current = current.left  
      
        return current  

    def delete(self, d):
        if d < self.value:
            self.left = Node.delete(self.left, d)
        elif d > self.value:
            self.right = Node.delete(self.right, d)
        else:
            if self.left == None:
                temp = self.right
                root = temp
                return temp
            elif self.right == None:
                temp = self.left
                self = None
                return temp

            temp = Node.minValueNode(self.right)

            self.d = temp.d

            self.right = Node.delete(self.right, temp.d)

        return self
            
class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self,d):
        if self.root:                       # Er til rót?
            return self.root.insert(d)      
        else:
            self.root = Node(d)
            return True

    def preOrderPrint(self):
        # Þinn kóði hér. Endurkvæmt fall sem fer yfir í Node klasa
        if self.root:
            self.root.preOrderPrint()
        else:
            return self.root

    def postOrderPrint(self):
        # Þinn kóði hér. Endurkvæmt fall sem fer yfir í Node klasa
        if self.root:
            self.root.postOrderPrint()
        else:
            return self.root
        
    def delete(self, d):
        # Þinn kóði hér. Endurkvæmt fall sem fer yfir í Node klasa
        if self.root is None:
            return -1
        elif self.root.value == d:
            self.root = self.root.right
            self.root.left.right = None
            self.root.right = None
            return True
        else:
            return self.root.delete(d)
        
            
    def deleteTree(self):
        # Þinn kóði hér
        self.root = None

t = Tree()
t.insert(10)
t.insert(5)
t.insert(3)
t.insert(4)
t.insert(8)
t.insert(6)
t.insert(9)
t.insert(20)
t.insert(15)


print("Pre-order:")
t.preOrderPrint()

print()
print()

print("Post-order:")
t.postOrderPrint()

t.delete(6)

print()
print()

t.preOrderPrint()
print()
t.postOrderPrint()



