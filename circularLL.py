"""Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle".

A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.

You've been given the Linked List Node class code:
"""

from nose.tools import assert_equal

class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


#############
class TestCycleCheck(object):

    def test(self,sol):
        assert_equal(sol(a),True)
        assert_equal(sol(x),False)

        print "ALL TEST CASES PASSED"

# Run Tests

t = TestCycleCheck()
t.test(cycle_check)



#Attempt 1:
def cycle_check(nodeObj):
    initialPoint = id(nodeObj) #gets the address of the node

    if nodeObj.nextnode == None:
        return False

    nodeObj = nodeObj.nextnode

    while(nodeObj):
        if(id(nodeObj) == initialPoint):
            return True
        try:
            nodeObj = nodeObj.nextnode
        except AttributeError:
            return False

#Popular Solution:

def cycle_check2(node):

    # Begin both markers at the first node
    marker1 = node
    marker2 = node

    # Go until end of list
    while marker2 != None and marker2.nextnode != None:

        # Note
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        # Check if the markers have matched
        if marker2 == marker1:
            return True

    # Case where marker ahead reaches the end of the list
    return False


"""difference between my solution and the second one is that my function traverses till
end of the linked list, going through each and every node. But the second solution skips one node
and jumps two nodes ahead, therby making runtime < O(n)."""
