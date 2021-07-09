class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

def lca(root, v1, v2):
    ansNode = None
    val1List = [root]
    val2List = [root]
    temp = root
    while temp!=None and temp.info!=v1:
        if temp.info < v1:
            temp = temp.right
        else:
            temp = temp.left
        val1List.append(temp)
    
    temp = root
    while temp!=None and temp.info!=v2:
        if temp.info < v2:
            temp = temp.right
        else:
            temp = temp.left
        val2List.append(temp)
    for i in val1List[::-1]:
        if i in val2List:
            return i
    return None


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
