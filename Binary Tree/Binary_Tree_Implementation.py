class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

firstnode = Node(2)
secondnode = Node(3)
thirdnode = Node(4)
fourthnode = Node(5)

firstnode.left = secondnode
firstnode.right = thirdnode
secondnode.left = fourthnode 