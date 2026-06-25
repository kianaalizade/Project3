class Node:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.key=key
def Add(root,data):
    if root==None:
        
        return Node(data)
    if data<root.key:
        root.left=Add(root.left,data)
       
    else :
        root.right=Add(root.right,data)
    return root
        
def Search(root,value):
    if root==None or (root.key)==value:
        return root
    if value>root.key:
        return Search(root.right,value)
    if value<root.key:
        return Search(root.left,value)
def Min_node(root):
    c=root
    
   
        
    while (c.left!= None):
                 c=c.left
    return c.key
def max_node(root):
    c=root
    
   
        
    while (c.right != None):
                 c=c.right
    return c.key
def preorder(root):
     if root:
          print(root.key," ")
          preorder(root.left)
          preorder(root.right)
          
  

r=Node(13)
r.left=Node(1)
r.right=Node(21)
Add(r,23)
preorder(r)
