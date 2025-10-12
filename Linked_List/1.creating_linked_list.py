#creating a node in linked list 


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
        
        
#creating object  [ node ] of that Node class 
node1 = Node(5)
node2 = Node(10)
node3 = Node(57)
node4 = Node(117)

# lining up the nodes 

node1.next = node2
node2.next= node3
node3.next=node4
