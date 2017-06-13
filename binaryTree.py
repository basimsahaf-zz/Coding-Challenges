"""Given a Binary tree find total number of clusters in a binary tree.

Cluster Definition: Assume there are two colors of node RED and BLUE. A start of cluster is when root, left and right have same color Node.

"""


class binaryTree(object):

    def __init__(self,bnode):
        self.head = bnode

class bnode(object):

    def __init__(self,color):
        self.value = color
        self.left = None
        self.right = None

class TestBTree(object):
    """docstring for TestBTree."""
    def TestClient(self,sol):
        a = bnode("Red")
        treeOne = binaryTree(a)
        b = bnode("Red")
        c = bnode("Red")
        a.left = b
        a.right = c
        d = bnode("Red")
        e = bnode("Red")
        b.left = d
        b.right = e
        assert(sol(treeOne)==2)
        print("All cases Correct")


def findNodes(bnode, blen):
    try:
        if bnode.value==bnode.left.value and bnode.value==bnode.right.value:
            blen += 1
    except AttributeError:
        pass
    if bnode.left:
        blen = findNodes(bnode.left,blen)
    if bnode.right:
        blen = findNodes(bnode.right,blen)
    return blen


def findClusters(btree):
    length = 0
    length = findNodes(btree.head, length)
    return length


t = TestBTree()
t.TestClient(findClusters)
