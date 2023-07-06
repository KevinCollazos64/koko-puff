import queue

print('\n----------------------BINARY SEARCH TREE -------------------------')

print('\nBST are essentially the same as Binary Trees, only with a few additional properties;'
      '\nProperty 1) In left subtree the value of nodes are less than or equal to its parent nodes value'
      '\nProperty 2) In right subtree the value of nodes are greater than its parent nodes value')

# BST does not store index of its data elements, instead relies on its implicit structure to keep record of elements
# Unique structure allows for quick deletion and insertion of nodes
# Instead of traversing sequentially, for BST we only have to traverse half the tree (the lower or greater half)
# Then we continue to half of that half, and half of that half and so on

print('\n----------------------CREATING BINARY SEARCH TREE -------------------------')
# Create object of BST class
# Inside BST class, we set root, left and right child to none


class BST:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


newBST = BST(None)  # When we create an object of BST class we are essentially creating its root


print('\n----------------------INSERTING TO BINARY SEARCH TREE -------------------------')
# Case 1: Insert into blank tree with no elements in it
# Case 2: BST already has some nodes in it

# For case 1, we simply create a blank node and toss it a value, and let the root point to this new node
# For case 2, we traverse only right or left side of tree (based on relative value of node we want to insert)

# If newnode < rootnode, go left
# If newnode > rootnode, go right
# Continue the comparisons until you find a vacant spot


def insertnode(rootnode, nodevalue):  # TC: OLOGN     SC: OLOGN (bc of recursive nature, we push logN elements to stack)
    if rootnode.data is None:  # Case 1
        rootnode.data = nodevalue
    elif nodevalue <= rootnode.data:  # Case 2 comparisons
        if rootnode.leftchild is None:
            rootnode.leftchild = BST(nodevalue)
        else:
            insertnode(rootnode.leftchild, nodevalue)  # recursive call if left child exists to continue comparisons
    else:
        if rootnode.rightchild is None:
            rootnode.rightchild = BST(nodevalue)  # recursive call if right child exists to continue comparisons
        else:
            insertnode(rootnode.rightchild, nodevalue)
    return 'Node successfully inserted'


print(insertnode(newBST, 50))
print(insertnode(newBST, 40))
print(insertnode(newBST, 45))
print(insertnode(newBST, 60))
print(insertnode(newBST, 55))
print(insertnode(newBST, 30))
print(insertnode(newBST, 70))


print('\n----------------------TRAVERSE BINARY SEARCH TREE -------------------------')

# PREORDER: ROOT -> LEFT CHILD -> RIGHT CHILD (last visit is at the right subtrees right leaf)
# INORDER: LEFT CHILD -> ROOT -> RIGHT CHILD
# POSTORDER: LEFT CHILD -> RIGHT CHILD -> ROOT
# LEVELORDER:  BY LEVELS

print('\nPREORDER: \n')  # PRE: ROOT FIRST

def preordertrav(rootnode):
    if not rootnode:
        return 'Error, root is None!'
    else:
        print(rootnode.data)
        preordertrav(rootnode.leftchild)
        preordertrav(rootnode.rightchild)


preordertrav(newBST)

print('\nINORDER: \n')  # IN: ROOT 2ND

def inordertrav(rootnode):
    if not rootnode:
        return 'Error, root is None!'
    else:
        preordertrav(rootnode.leftchild)
        print(rootnode.data)
        preordertrav(rootnode.rightchild)

inordertrav(newBST)

print('\nPOSTORDER: \n')  # POST:  ROOT LAST

def postordertrav(rootnode):
    if not rootnode:
        return 'Error, root is None!'
    else:
        postordertrav(rootnode.leftchild)
        postordertrav(rootnode.rightchild)
        print(rootnode.data)

postordertrav(newBST)

print('\nLEVELORDER: \n')  # FOR LEVEL WE CAN INCORPORATE QUEUE, DEQUEUEING AND PRINTING NODE VALUE AS WE CHECK LC RC

def levelordertrav(rootnode):
    if not rootnode:
        return 'Error, root is None!'
    else:
        customq = queue.Queue()
        customq.put(rootnode)
        while not customq.empty():
            root = customq.get()
            print(root.data)
            if root.leftchild is not None:
                customq.put(root.leftchild)
            if root.rightchild is not None:
                customq.put(root.rightchild)
    return 'Finished traverse!'

levelordertrav(newBST)


print('\n----------------------SEARCH VALUE IN BINARY SEARCH TREE -------------------------')
# Search using BST is faster because we know which side of tree to look at based on target value
# Left of root = smaller value,   Right of root = bigger value


def searchnodeBST(rootnode, target):
    if rootnode.data == target:
        return 'Found at the root!'
    elif target < rootnode.data:  # if target is less than current root
        if rootnode.leftchild.data == target:  # if its left child is the target, we found
            return 'Value found!'
        else:
            searchnodeBST(rootnode.leftchild, target)  # otherwise, recursively call the left child
    else:
        if rootnode.rightchild.data == target:  # same logic for right side
            return 'Value found!'
        else:
            searchnodeBST(rootnode.rightchild, target)


print(searchnodeBST(newBST, 50))
print(searchnodeBST(newBST, 40))
print(searchnodeBST(newBST, 60))

# Numbers that DNE in BST raise Nonetype error?

print('\n----------------------DELETE NODE IN BINARY SEARCH TREE -------------------------')
# Case 1: Node to be deleted is the leaf node
# Compare node to be deleted value with root, make your way to the leaf and straight up delete it


# Case 2: Node only has one child
# Start traversing through the root node. If has a child node, root's value is eliminated and child's value is now root


# Case 3: Node has 2 children
# Find successor (the smallest node in the right subtree) and replace value of node to delete w/ value of successor
# To find minimum value of right subtree (successor) we need a method that returns to us this value

def minvaluenode(bstnode):  # Traverses through BST and returns min value
    current = bstnode
    while current.leftchild is not None:
        minvaluenode(current.leftchild)  # Min values will always be on the left side according to BST properties
    return current


def deletenode(rootnode, nodevalue):  # NOT WORKING?
    if rootnode is None:  # checks rootnode
        return rootnode
    if nodevalue < rootnode.data:
        rootnode.leftchild = deletenode(rootnode.leftchild, nodevalue)
    elif nodevalue > rootnode.data:
        rootnode.rightchild = deletenode(rootnode.rightchild, nodevalue)
    else:  # for roots with only 1 child or none
        if rootnode.leftchild is None:
            temp = rootnode.rightchild
            rootnode = None
            return temp
        if rootnode.rightchild is None:
            temp = rootnode.leftchild
            rootnode = None
            return temp

        temp = minvaluenode(rootnode.rightchild)  # calling it for right subtree bc successor for BST is on the right
        rootnode.data = temp.data  # after finding we set data of value of node tbd to this values data
        rootnode.rightchild = deletenode(rootnode.rightchild, temp.data)
    return rootnode


# deletenode(newBST, 50) <------- NOT WORKING
levelordertrav(newBST)

print('\n----------------------DELETE ENTIRE BINARY SEARCH TREE -------------------------')
# root, left and right child to none


def deleteBST(rootnode):
    rootnode.leftchild = None
    rootnode.rightchild = None
    rootnode = None
    return 'BST successfully deleted!'


print(deleteBST(newBST))

print('\n----------------------BINARY SEARCH TREE TC SC QUIZ -------------------------')

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


class BST_set:

    tc_set = {'Creation of BST': 'O1', 'Insertion to BST': 'ON', 'Traversing BST': 'ON', 'Searching BST': 'ON',
              'Deleting node in BST': 'ON', 'Deleting entire BST': 'O1'}

    sc_set = {'Creation of BST': 'O1', 'Insertion to BST': 'ON', 'Traversing BST': 'ON', 'Searching BST': 'ON',
              'Deleting node in BST': 'ON', 'Deleting entire BST': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning!')
                BST_set.assess_tc(BST_set.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        BST_set.assess_sc(BST_set.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                BST_set.assess_sc(BST_set.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')


BST_set.assess_tc(BST_set.tc_set)

print('\nThe values that are OLOGN are due to having to either traverse in the left or right subtree based on what we'
      '\nwant to do. For insert, we look for a vacant place for the node, and where we place it depends on its value'
      '\nand whether we go left or right from the rootnode. Similar logic for searching a node and deleting a node,'
      '\nwhich all require OLOGN TC and SC. We recursively call each respective function, meaning if we take OLOGN TC'
      '\nwe will place OLOGN elements into stack memory.'
      '\nHOWEVER BST can still perform at ON TC (slow) if it becomes unbalanced in the worst case')

