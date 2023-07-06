import queue

print('\n----------------------AVL TREE -------------------------\n')

print('\nAVL trees are self-balancing Binary search trees where the difference between the heights of left and right'
      '\nsubtrees cannot be more than one for all nodes\n')

print('AVL trees MUST be balanced and use height balancing automatically')

print('\nWhy do we need AVL Trees?\n'
      '- If we rotate elements through height balancing, the tree will perform better\n'
      '- Generally, the less height on a tree, the better its performance\n'
      '\nThe auto-balancing property of AVL tree allows it to perform faster in insertions, deletions, and searching\n'
      '\nEvery time there is a loss of balance, AVL tree performs some rotations to balance the tree once again')


print('\n----------------------CREATING AVL TREE -------------------------')
# Initialize root node w/value of none.
# Set left and right child to none


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1  # To tell whether tree is balanced or not, we need this property


newAVL = AVLNode(None)

print('\n----------------------TRAVERSE AVL TREE -------------------------')

# PREORDER: ROOT -> LEFT CHILD -> RIGHT CHILD (last visit is at the right subtrees right leaf)
# INORDER: LEFT CHILD -> ROOT -> RIGHT CHILD
# POSTORDER: LEFT CHILD -> RIGHT CHILD -> ROOT
# LEVELORDER:  BY LEVELS

print('\nWe see that traversal syntax for an AVL Tree is similar to a regular Binary Search Tree')

print('\nPREORDER: \n')  # PRE: ROOT FIRST


def preordertrav(rootnode):
    if not rootnode:
        return 'Root error!'
    else:
        print(rootnode.data)
        preordertrav(rootnode.leftchild)
        preordertrav(rootnode.rightchild)


print('\nINORDER: \n')  # IN: ROOT 2ND


def inordertrav(rootnode):
    if not rootnode:
        return 'Root error!'
    else:
        inordertrav(rootnode.leftchild)
        print(rootnode.data)
        inordertrav(rootnode.rightchild)


print('\nPOSTORDER: \n')  # POST:  ROOT LAST

def postordertrav(rootnode):
    if not rootnode:
        return 'Root error!'
    else:
        postordertrav(rootnode.leftchild)
        postordertrav(rootnode.rightchild)
        print(rootnode.data)


print('\nLEVELORDER: \n')  # FOR LEVEL WE CAN INCORPORATE QUEUE, DEQUEUEING AND PRINTING NODE VALUE AS WE CHECK LC RC


def levelordertrav(rootnode):
    if not rootnode:
        return 'Root error!'
    else:
        customq = queue.Queue()
        customq.put(rootnode)
        while not customq.empty():
            root = customq.get()
            print(root.data)
            if root.leftchild is not None:
                customq.get(root.leftchild)
            if root.rightchild is not None:
                customq.get(root.rightchild)
    return 'Finished traverse!'


print('\n----------------------SEARCH NODE IN AVL TREE -------------------------')
# Idea is generally the same; check if root == searched value
# If less than root, compare L child, else recursive call for L child
# Else, check if R child == searched value if not, recursive call for the R child


def searchAVL(rootnode, target):
    if rootnode.data == target:
        return 'Target found at root!'
    else:
        if target < rootnode.data:
            if rootnode.leftchild.data == target:
                return 'Target found as a left child!'
            else:
                searchAVL(rootnode.leftchild, target)
        else:
            if rootnode.rightchild.data == target:
                return 'Target found as a right child!'
            else:
                searchAVL(rootnode.rightchild, target)


print('\n----------------------INSERT NODE IN AVL TREE -------------------------')
# Case 1: Rotation required (unbalanced tree)
# 4 sub conditions: LL, LR, RR, RL rotations
# To find the right condition;
# 1) Find the unbalanced node (the node with disparity in the height =>2)
# 2) Find the grandchild of this unbalanced node. The path from the parent to the grandchild will show the condition
# LL condition: RIGHT rotation
# LR condition: Rotate grandchild LEFT,  then unbalancednode RIGHT
# RL condition: Rotate grandchild RIGHT, then unbalancednode LEFT
# RR condition: LEFT rotation

# Case 2: No rotation required
# In this case insertion is similar to BST. Compare newnode to root, left and right child to find appropriate site


def rotateright(unbalancednode):
    newroot = unbalancednode.leftchild
    unbalancednode.leftchild = unbalancednode.leftchild.rightchild
    newroot.rightchild = unbalancednode
    unbalancednode.height = 1 + max(getheight(unbalancednode.leftchild), getheight(unbalancednode.rightchild))
    newroot.height = 1 + max(getheight(unbalancednode.leftchild), getheight(unbalancednode.rightchild))
    # in the line above. we add 1 b/c getheight returns L+R child height, but here we are setting the unbalanced
    # nodes height. We need to add the parent node as well, which is the unbalanced node, so we add 1
    return newroot


def rotateleft(unbalancednode):
    newroot = unbalancednode.rightchild
    unbalancednode.rightchild = unbalancednode.rightchild.leftchild
    newroot.leftchild = unbalancednode
    unbalancednode.height = 1 + max(getheight(unbalancednode.leftchild), getheight(unbalancednode.rightchild))
    newroot.height = 1 + max(getheight(unbalancednode.leftchild), getheight(unbalancednode.rightchild))
    return newroot


# LL CONDITION: rotateright(unbalancednode)

# LR CONDITION: rotateleft(unbalancednode.leftchild), rotateright(unbalancednode) ; Rotate lower half left, upper right

# RR CONDITION: rotateleft(unbalancednode)

# RL CONDITION: rotateright(unbalancednode.rightchild), rotateleft(unbalancednode) ; Rotate lower half right, upper left

# To implement logic of AVL trees, we need various helper functions

def getheight(rootnode):
    if not rootnode:
        return 'Error, invalid root'
    else:
        return rootnode.height

# Whenever we insert to an AVL tree, we need to check if it's balanced after EVERY insertion


def getbalance(rootnode):  # helps us identify the condition
    if not rootnode:
        return 'Error, invalid root'
    else:
        return getheight(rootnode.leftchild) - getheight(rootnode.rightchild)

# Actual insert node method where all cases are addressed


def insertnode(rootnode, nodevalue):
    if not rootnode:
        return AVLNode(nodevalue)
    elif nodevalue < rootnode.data:
        rootnode.leftchild = insertnode(rootnode.leftchild, nodevalue)  # if newvalue smaller than root, and if
        # we recursively call the method again and there is no leftchild (satisfying the if not rootnode cond) then it
        # returns an AVL instance of the nodevalue and sets it as the leftchild
    else:
        rootnode.rightchild = insertnode(rootnode.rightchild, nodevalue)  # same thing but for the right child
    rootnode.height = 1 + max(getheight(rootnode.leftchild), getheight(rootnode.rightchild))  # We have to update...
    # the ancestor's height b/c we are adding a new node and the height is changing
    balance = getbalance(rootnode)  # this value gives us our condition
    if balance > 1 and nodevalue < rootnode.leftchild.data:  # LL CONDITION
        return rotateright(rootnode)
    if balance > 1 and nodevalue > rootnode.leftchild.data:  # LR CONDITION
        rootnode.leftchild = rotateleft(rootnode.leftchild)  # rotating the left child LEFT <- makes the cond LL now
        return rotateright(rootnode)
    if balance < -1 and nodevalue > rootnode.rightchild.data:  # RR CONDITION
        return rotateleft(rootnode)
    if balance < -1 and nodevalue < rootnode.rightchild.data:  # RL CONDITION
        rootnode.rightchild = rotateright(rootnode.rightchild)  # rotating the right child RIGHT -> makes the cond RR
        return rotateleft(rootnode)
    return rootnode


testAVL = AVLNode(30)
insertnode(testAVL, 5)
insertnode(testAVL, 10)
insertnode(testAVL, 15)
insertnode(testAVL, 20)
insertnode(testAVL, 25)
levelordertrav(testAVL)


print('\n----------------------DELETE NODE IN AVL TREE -------------------------')
# Case 1: Rotation required (unbalanced tree)
# 4 sub conditions: LL, LR, RR, RL rotations

# Whenever we delete a node we have to check if the parent of deleted node becomes unbalanced or not
# If node becomes unbalanced, we can identify the condition through the path from unbalanced node to grandchild


# Case 2: Rotation not required
# 3 sub conditions: 1) Node to be deleted is leaf  2) Node TBD has 1 child  3) Node TBD has 2 children

# 1) Leaf - Must traverse to the node TBD, and we can straight up delete because it's a leaf node
# 2) Node TBD has 1 child - Search value, delete the node and assign deleted node's child to deleted node's parent
# 3) Node TBD has 2 children - Search value, find successor node (min node in right subtree), switch successor and
# node TBD, assign new children

# To delete we need minsuccessor helper function in the case that the node has 2 children
# The successor will be the minimum value found in the left subtree

def getminvalue(rootnode):
    if rootnode is None or rootnode.leftchild is None:
        return rootnode
    return getminvalue(rootnode.leftchild)  # Recursive call to find min value in the left subtree


def deleteNode(rootnode, nodevalue):
    if not rootnode:
        return 'Rootnode error!'
    elif nodevalue < rootnode.data:
        rootnode.leftchild = deleteNode(rootnode.leftchild, nodevalue)  # recursive call down left subtree
    elif nodevalue > rootnode.data:
        rootnode.rightchild = deleteNode(rootnode.rightchild,  nodevalue)  # recursive call down right subtree
    else:
        if rootnode.leftchild is None:  # returns either right or left child. If we want to delete node in which we have
            temp = rootnode.rightchild  # a right child, based on the return, in this case it will set it to left child
            rootnode = None  # because it becomes the left child of the parent node of the deleted node
            return temp
        elif rootnode.rightchild is None:
            temp = rootnode.leftchild
            rootnode = None
            return temp
        temp = getminvalue(rootnode.rightchild)  # Assigns successor to a variable
        rootnode.data = temp.data  # Switch values of successor w/ the previous rootnode
        rootnode.rightchild = deleteNode(rootnode.rightchild, temp.data)  # up until here, this is method for BST delete
    rootnode.height = 1 + max(getheight(rootnode.leftchild), getheight(rootnode.rightchild))
    balance = getbalance(rootnode)
    if balance > 1 and getbalance(rootnode.leftchild) >= 0:  # LL CONDITION
        return rotateright(rootnode)
    if balance < -1 and getbalance(rootnode.rightchild) <= 0:  # RR CONDITION
        return rotateleft(rootnode)
    if balance < 1 and getbalance(rootnode.leftchild) < 0:  # LR COND, rotate LC left and ROOT right
        rootnode.leftchild = rotateleft(rootnode.leftchild)
        return rotateright(rootnode)
    if balance < -1 and getbalance(rootnode.rightchild) > 0:  # RL COND, rotate RC right and ROOT left
        rootnode.rightchild = rotateright(rootnode.rightchild)
        return rotateleft(rootnode)
    return rootnode


print('\n----------------------DELETE ENTIRE AVL TREE -------------------------')
# If you set up an AVL tree with a linked list, you just need to delete the root node and links to its children

def deleteEntireAVL(rootnode):
    if not rootnode:
        return 'Nothing to delete!'
    else:
        rootnode.leftchild = None
        rootnode.rightchild = None
        rootnode = None
    return 'Successfully deleted entire AVL!'


print('\n----------------------AVL TREE TC SC QUIZ -------------------------')


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


class AVL_set:

    tc_set = {'Creation of AVL': 'O1', 'Insertion to AVL': 'OLOGN', 'Traversing AVL': 'ON', 'Searching AVL': 'OLOGN',
              'Deleting node in AVL': 'OLOGN', 'Deleting entire AVL': 'O1'}

    sc_set = {'Creation of AVL': 'O1', 'Insertion to AVL': 'OLOGN', 'Traversing AVL': 'ON', 'Searching AVL': 'OLOGN',
              'Deleting node in AVL': 'OLOGN', 'Deleting entire AVL': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning!')
                AVL_set.assess_tc(AVL_set.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        AVL_set.assess_sc(AVL_set.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                AVL_set.assess_sc(AVL_set.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')


AVL_set.assess_tc(AVL_set.tc_set)

print('\nHere we see that AVL trees have improved performance compared to unbalanced BST in terms of insertion,'
      '\nsearching, and node deletion because of its enhanced properties. Even in the worst case, due to AVL tree'
      '\nconstantly rebalancing to maintain order, it will perform at OLOGN speed compared to ON speed in unbal BST')

