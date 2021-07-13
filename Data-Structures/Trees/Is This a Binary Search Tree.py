""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
list1 = []
def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        list1.append(root)
        inOrderTraversal(root.right)
        
def check_binary_search_tree_(root):
    inOrderTraversal(root)
    if len(list1) < 2 :
        return True
    for i in range(len(list1)-1):
        if list1[i].data >= list1[i+1].data:
            return False
    return True
            
    