class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def insert(root,node):
	if root is None:
		root = node
	else:
		if root.data < node.data:
			if root.right is None:
				root.right = node
			else:
				insert(root.right,node)
		else:
			if root.left is None:
				root.left = node
			else:
				insert(root.left,node)

def inorder(root):
	if root is not None:
		#print ("1")
		#print(root.data)
		#print ("2")
		inorder(root.left)
		#print ("3")
		print(root.data)
		#print("4")
		inorder(root.right)
		#print ("5")
		#print (root.data)

r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
#print(r.data)
inorder(r)
		