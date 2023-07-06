

print('\n----------------------TREE -------------------------'
      '\nA tree is a nonlinear data structure with hierarchical relationship between its elements without a cycle')
print('\nSome properties of trees include:'
      '\n1) Represent hierarchical data (every step down is a more specialized form of the parent'
      '\n2) Each node has 2 components: data and link to its sub category'
      '\n3) There is a base category and sub categories under it. Root node > Sub nodes.'
      '\n\nWe need trees because they allow for quicker, easier access to data as it is a non linear data structure'
      '\nOther data structures like arrays, lists, stack, queue, store data sequentially, so TC will increase w/size')


print('\n----------------------CREATING BASIC TREE -------------------------')
# create Treenode class, initializing it with data and children = []
# create addchild class, with treenode as parameter, and use append to add the treenode to the child list


class Treenode:

    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):  # helps us print out the tree and links more clearly
        ret = ''*level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def addchild(self, treenode):
        self.children.append(treenode)


instrument_tree = Treenode('Instruments', [])
brass = Treenode('Brass', [])
wind = Treenode('Wind', [])
instrument_tree.addchild(brass)
instrument_tree.addchild(wind)
print(instrument_tree)

flute = Treenode('Flute', [])
wind.addchild(flute)
print(instrument_tree)

# Types of Binary Trees :
# Full BT : Tree where each node has either 2 or 0 children
# Perfect BT : Tree where all non-leaf nodes have 2 children, and they are the same depth. All leaf nodes same level
# Complete BT : All levels filled except last one, and in last level nodes are kept left most as possible
# Balanced BT : Each leaf not more than certain distance from root node than any other leaf

print('\n----------------------BINARY TREE REPRESENTATIONS -------------------------')

print('\n\nBT can be represented with a Linked Lists, and python lists (arrays)')
print('\n\nEach have their own usages, advantages and disadvantages')

# Linked list BT nodes look like :  [LEFT CHILD REF              DATA                 RIGHT CHILD REF]

# Array BT can look like: [ x , Instruments , Brass, Wind, Saxophone, Flute] where x is empty first cell for the root

print('\n----------------------CREATE BINARY TREE USING LINKED LIST (LLBT) -------------------------')

# Create object of BT class
# 3 components in each node: Left Child, Data, Right Child


class LLBTNode:

    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def preordertrav(self, rootnode):
        if not rootnode:
            return 'Error no root?'
        print(rootnode.data)
        preordertrav(rootnode.leftchild)
        preordertrav(rootnode.rightchild)



newbt = LLBTNode('Instruments')
Brass = LLBTNode('Brass')
Air = LLBTNode('Air')
Flute = LLBTNode('Flute')
Saxophone = LLBTNode('Saxophone')
newbt.leftchild = Brass
newbt.rightchild = Air
Air.leftchild = Flute
Brass.leftchild = Saxophone



print('\n----------------------LL BINARY TREE TRAVERSAL -------------------------')
# DEPTH FIRST SEARCH TRAVERSALS: PREORDER, INORDER, POSTORDER
# PREORDER: ROOT -> LEFT CHILD -> RIGHT CHILD (last visit is at the right subtrees right leaf)
# INORDER: LEFT CHILD -> ROOT -> RIGHT CHILD
# POSTORDER: LEFT CHILD -> RIGHT CHILD -> ROOT
# BREADTH FIRST SEARCH TRAVERSALS: LEVEL ORDER

# Space complexity of all methods is ON because recursive calls adds values to the stack memory  to come back to after


def preordertrav(rootnode):
    if not rootnode:  # if root is null, no tree
        return 'Error no root?'
    print(rootnode.data)
    preordertrav(rootnode.leftchild)  # recursive, O(N/2)
    preordertrav(rootnode.rightchild)  # recursive, O(N/2) because 2 children


print('\nPREORDER: \n')
preordertrav(newbt)

# INORDER:
# In this traversal you finish smaller subtrees before moving onto bigger ones
# In right tree, you visit the left child first
# Right subtree right leaf always visited last


def inordertrav(rootnode):
    if not rootnode:
        return 'Error no root?'
    inordertrav(rootnode.leftchild)  # O(N/2)
    print(rootnode.data)
    inordertrav(rootnode.rightchild)  # O(N/2)


print('\nINORDER: \n')
inordertrav(newbt)


# POSTORDER:
# In this traversal the rootnode is visited last


def postordertrav(rootnode):
    if not rootnode:
        return 'Error no root?'
    postordertrav(rootnode.leftchild)
    postordertrav(rootnode.rightchild)
    print(rootnode.data)


print('\nPOSTORDER: \n')
postordertrav(newbt)


# LEVELORDER:
# In the case of level order traversals, we can use a linked list queue to traverse the tree how we want (by levels)
# The root will always be visited first in level order traversals because it is the first level of any tree
# We always start level order traversals from the left


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):  # Makes the LL iterable, yielding the values of nodes in one list
        currnode = self.head
        while currnode:
            yield currnode
            currnode = currnode.next


class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):  # Makes our Queue printable
        values = [str(x) for x in self.linkedlist]
        return ''.join(values)

    def enqueue(self, value):  # 2 conditions to consider: if no node, if nodes already exist
        new = Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head = new
            self.linkedlist.tail = new
        else:
            self.linkedlist.tail.next = new
            self.linkedlist.tail = new
        return 'Value added!'

    def isempty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False

    def dequeue(self):  # Same 2 conditions to consider: if no node, if node already exists
        if self.linkedlist.head is None:
            return 'Error, linkedlist is empty!'
        else:
            dequeuednode = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return dequeuednode.value

    def peek(self):
        if self.linkedlist.head is None:
            return 'Error, linkedlist is empty!'
        else:
            return self.linkedlist.head

    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None
        return 'Successfully deleted entire Queue LL!'


def levelordertrav(rootnode):
    if not rootnode:
        return 'Error no root!'
    else:
        customq = Queue()
        customq.enqueue(rootnode)  # Queue the current root (root of the tree, level 1)
        while not customq.isempty():  # while the custom q is not empty:
            root = customq.dequeue()  # dequeue the root according to FIFO and print its value
            print(root.data)
            if root.leftchild is not None:  # if current root has a left child, queue that
                customq.enqueue(root.leftchild)
            if root.rightchild is not None:  # if current root has a right child, queue it and run again
                customq.enqueue(root.rightchild)


print('\nLEVELORDER: \n')
levelordertrav(newbt)


print('\n----------------------LL BINARY TREE SEARCH -------------------------')
# Level order Traverse through BT using Queue , comparing target value every step in traversal
# Level order trav uses queue, while other traversal methods use stack
# IN THIS CASE QUEUE ALWAYS PERFORMS BETTER THAN STACK


def searchLLBT(rootnode, targetvalue):
    if not rootnode:
        return 'Error no root!'
    else:
        customq = Queue()
        customq.enqueue(rootnode)
        while not customq.isempty():
            root = customq.dequeue()  # dequeues according to FIFO
            if root.data == targetvalue:  # compare current root that was just dequeued to target
                return root.data  # if matches, return its data
            if root.leftchild is not None:
                customq.enqueue(root.leftchild)
            if root.rightchild is not None:
                customq.enqueue(root.rightchild)
        return 'Value not found'


print(searchLLBT(newbt, 'Flute'))
print(searchLLBT(newbt, 'Guitar'))

print('\n----------------------LL BINARY TREE INSERT A NODE -------------------------')

# Case 1: Root node is blank (in this case, if root DNE, we just create a root and assign a value to it)
# Case 2: Tree already exists, and we are looking to insert at a vacant spot

# For Case 2, we would have to level order traverse, scanning if every root has 2 children in each step
# The first root that does not have 2 children in our LOT will be the site of insertion for the new node
# The new node is inserted as the left (priority) child or right child

def insertLLBT(rootnode, newnode):
    if not rootnode:
        rootnode = newnode
    else:
        customq = Queue()
        customq.enqueue(rootnode)
        while not customq.isempty():
            root = customq.dequeue()
            if root.leftchild is not None:
                customq.enqueue(root.leftchild)
            elif root.leftchild is None:
                root.leftchild = newnode
                return 'Node inserted'
            if root.rightchild is not None:
                customq.enqueue(root.rightchild)
            elif root.rightchild is None:
                root.rightchild = newnode
                return 'Node inserted'


new = LLBTNode('Trombone')
insertLLBT(newbt, new)
levelordertrav(newbt)  # should display trombone after sax, since sax is left child of brass and right child is vacant

print('\n----------------------LL BINARY TREE DELETE A NODE -------------------------')
# Case 1: Value DNE in BT
# Case 2: Value exists in BT

# Case 2: 3 separate methods for removing a node that exists in a BT
# Method 1: Get the deepest node in the tree (last value using LOT)
# Method 2: Delete the deepest node
# Method 3: Delete the node from the BT (switch values of node to be deleted, and deepest node)


def getdeepestLLBT(rootnode):   # Method 1 returns value of the deepest node in the tree
    if not rootnode:
        return 'Error, no root!'
    else:
        customq = Queue()
        customq.enqueue(rootnode)
        while not customq.isempty():
            root = customq.dequeue()
            if root.leftchild is not None:
                customq.enqueue(root.leftchild)
            if root.rightchild is not None:
                customq.enqueue(root.rightchild)
        deepestnode = root.data
        return deepestnode


levelordertrav(newbt)
print('\nDeepest node:', getdeepestLLBT(newbt))


def deldeepestLLBT(rootnode, dnode):  # Method 2 deletes the deepest node in the tree and makes its value None
    if not rootnode:
        return 'Error. no root!'
    else:
        customq = Queue()
        customq.enqueue(rootnode)
        while not customq.isempty():
            root = customq.dequeue()
            if root.data == dnode:
                root.data = None
                return 'Successfully deleted root'
            if root.leftchild:  # if left child exists, compare it to target, if not target it is queued
                if root.leftchild.data == dnode:
                    root.leftchild.data = None
                    return 'Successfully deleted deepest node'
                else:
                    customq.enqueue(root.leftchild)
            if root.rightchild:  # if right child exists, compare to target, if not target it is queued
                if root.rightchild.data == dnode:
                    root.rightchild.data = None
                    return 'Successfully deleted deepest node!'
                else:
                    customq.enqueue(root.rightchild)


target = getdeepestLLBT(newbt)
print(deldeepestLLBT(newbt, target))
levelordertrav(newbt)  # Flute should be deleted, so Air no longer has children

# Noticed that when using print(levelorder..) the nodes with value "None" were also printed, AVOID


def deletenodeBT(rootnode, target):
    if not rootnode:
        return 'Error root DNE!'
    else:
        customq = Queue()
        customq.enqueue(rootnode)
        while not customq.isempty():
            root = customq.dequeue()
            if root.data == target:
                deepest = getdeepestLLBT(rootnode)
                deldeepestLLBT(rootnode, deepest)
                root.data = deepest  # Switching the order of this line and the line above messes with output
                return 'Node deleted!'
            if root.leftchild is not None:
                customq.enqueue(root.leftchild)
            if root.rightchild is not None:
                customq.enqueue(root.rightchild)
        return 'Failed to delete'


Recorder = LLBTNode('Recorder')
Whistle = LLBTNode('Whistle')
Air.leftchild = Recorder
Air.rightchild = Whistle
print('\nSame tree but with new values added: \n')
levelordertrav(newbt)

print('\nDeleting Trombone and replacing with the deepest node (Whistle)...\n')

print(deletenodeBT(newbt, 'Trombone'))  # this call should replace Trombone with Whistle, & delete the value of Trombone

levelordertrav(newbt)


print('\n----------------------LL BINARY TREE DELETE ENTIRE -------------------------')

# Just set rootnode to None, and its children to none

def delallLLBT(rootnode):

    rootnode.leftchild = None
    rootnode.rightchild = None
    rootnode = None
    return 'Deleted entire LL BT!'


print(delallLLBT(newbt))
levelordertrav(newbt)

print('\n----------------------LL BINARY TREE Entire TC SC QUIZ -------------------------')

class Question:

    def ask_tc():
        ans= (input('What is the TC of this operation? Remove parenthesis and spaces from your answer')).upper()
        if ans[0] != 'O':
            print ('Please provide an answer in big O notation. Try again')
            Question.ask_tc()
        return ans

    def ask_sc():
        ans = (input('What is the SC of this operation? Remove parenthesis and spaces from your answer')).upper()
        if ans[0]  != 'O':
            print('Please provide an answer in big O notation. Try again')
            Question.ask_sc()
        return ans

    def ask_shoulduse():
        answers = ['Y', 'N']
        ans = str((input('Should we use arrays in this situation? Input y for yes and n for no (remove spaces)')).upper())
        if ans not in answers:
            print ('Please provide a valid input.')
            Question.ask_shoulduse()
        return ans


class LLBT_set:

    tc_set = {'Creation of LLBT': 'O1', 'Insertion to LLBT': 'ON', 'Traversing LLBT': 'ON', 'Searching LLBT': 'ON',
              'Deleting node in LLBT': 'ON', 'Deleting entire LLBT': 'O1'}

    sc_set = {'Creation of LLBT': 'O1', 'Insertion to LLBT': 'ON', 'Traversing LLBT': 'ON', 'Searching LLBT': 'ON',
              'Deleting node in LLBT': 'ON', 'Deleting entire LLBT': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning!')
                LLBT_set.assess_tc(LLBT_set.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        LLBT_set.assess_sc(LLBT_set.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                LLBT_set.assess_sc(LLBT_set.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')


LLBT_set.assess_tc(LLBT_set.tc_set)



