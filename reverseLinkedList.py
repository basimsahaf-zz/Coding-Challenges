"""Write a function to reverse a Linked List in place.
The function will take in the head of the list as input and return the new head of the list."""

#Node Class:
class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None

#Testing Client
class TestReverse(object):

    def TestClient(self,sol):
        # Create a list of 4 nodes
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        # Set up order a,b,c,d with values 1,2,3,4
        a.nextnode = b
        b.nextnode = c
        c.nextnode = d
        sol(a)
        assert(a.nextnode==None)
        assert(b.nextnode.value==1)
        assert(c.nextnode.value==2)
        assert(d.nextnode.value==3)
        print("All Test Cases are Correct")

#Solution:

def reverse(nodeObj):
    if nodeObj.nextnode == None:
        return nodeObj
    prevNode = None
    currNode = nodeObj
    nextNode = None
    while currNode:
        try:
            nextNode = currNode.nextnode
        except AttributeError:
            currNode.nextnode = prevNode
            return currNode

        currNode.nextnode = prevNode
        prevNode = currNode
        currNode = nextNode


#Testing the function:
t = TestReverse()
t.TestClient(reverse)
