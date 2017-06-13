"""Write a function that takes a head node and an integer value n and
then returns the nth to last node in the linked list."""

class Node(object):

    def __init__(self,k):
        self.value = k
        self.nextnode = None

#Testing Client
class TestNthToLast(object):

    def TestClient(self,sol):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        e = Node(5)
        a.nextnode = b
        b.nextnode = c
        c.nextnode = d
        d.nextnode = e
        assert(sol(2,a)==4)
        assert(sol(3,a)==3)
        assert(sol(4,a)==2)
        assert(sol(5,a)==1)
        print("All Test Cases Correct")

#Solution:1
def nth_to_last_node(n,head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.nextnode

    nodeIndex = length - n

    current = head
    while(nodeIndex != 0 and current.nextnode != None):
            current = current.nextnode
            nodeIndex-=1

    return current.value

#Tests
t = TestNthToLast()
t.TestClient(nth_to_last_node)


#Most efficient Solution:
def nth_to_last_node_2(n,head):
    left_pointer = head
    right_pointer = head

    for i in range(n-1):
        if not right_pointer.nextnode:
            raise Error('n is bigger than the length of the linked list')
        right_pointer = right_pointer.nextnode

    while right_pointer.nextnode:
        right_pointer = right_pointer.nextnode
        left_pointer = left_pointer.nextnode

    return left_pointer.value

#Tests
a = TestNthToLast()
a.TestClient(nth_to_last_node_2)
