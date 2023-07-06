print('\n----------------------BINARY TREE REPRESENTATIONS -------------------------')

print('\n\nBT can be represented with a Linked Lists, and python lists (arrays)')
print('\n\nEach have their own usages, advantages and disadvantages')

# Linked list BT nodes look like :  [LEFT CHILD REF              DATA                 RIGHT CHILD REF]

# Array BT can look like: [ x (instruments) , Brass, Wind, Saxophone, Flute] where x is empty first cell for the root

print('\n----------------------CREATE BINARY TREE USING PYTHON LIST (PLBT) -------------------------')

# Initialize an empty python list
# Keep the first cell empty as this simplifies our math calculations
# Insert rootnode after the first cell (after [0])
# Then, we can calculate left and right child using these equations:
# Left child = cell[2x]
# Right child = cell[2x+1]

# Create an object of BT class with fixed size python list abd last used index set to 0
# We need a last used index variable because when we insert a new node we need to keep track of this

class BinaryTree:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.customlist = maxsize * [None]
        self.lastusedindex = 0

    def insertPLBT(self, value):
        if self.lastusedindex + 1 == self.maxsize:
            return 'Error, list is full!'
        else:
            self.customlist[self.lastusedindex+1] = value
            self.lastusedindex +=1
        return 'Successfully inserted'

    def searchPLBT(self, target):
        for i in range(len(self.customlist)):  # no -1 because the first cell is left blank
            if self.customlist[i] == target:
                return f'Found in cell {i}'
        return 'Not found!'

    def preordertrav(self, index):  # We have to provide the index because we can't start from [0] (empty)
        if index > self.lastusedindex:
            return 'Invalid Index!'
        else:
            print(self.customlist[index])  # root
            self.preordertrav(index*2)  # left
            self.preordertrav(index*2+1) # right

    def inordertrav(self, index):
        if index > self.lastusedindex:
            return 'Invalid Index!'
        else:
            self.preordertrav(index * 2)  # left
            print(self.customlist[index])  # root
            self.preordertrav(index * 2 + 1)  # right

    def postordertrav(self, index):
        if index > self.lastusedindex:
            return 'Invalid Index!'
        else:
            self.preordertrav(index * 2)  # left
            self.preordertrav(index * 2 + 1)  # right
            print(self.customlist[index])  # root

    def levelordertrav(self,index):
        if index > self.lastusedindex:
            return 'Invalid Index!'
        else:
            for i in range(index, self.lastusedindex+1):
                print(self.customlist[i])

    def deletenode(self, target):
        if self.lastusedindex == 0:
            return 'Error there are no values in this list!'
        for i in range(1, self.lastusedindex+1):
            if self.customlist[i] == target:
                self.customlist[i] = self.customlist[self.lastusedindex]
                self.customlist[self.lastusedindex] = None
                self.lastusedindex -= 1
        return 'Successfully deleted node'

    def deleteentire(self):
        self.customlist = None
        return 'Successfully deleted entire PLBT'


newPLBT = BinaryTree(10)

print('\n----------------------INSERT TO PYTHON LIST BINARY TREE ------------------------')

# Case 1: BINARY TREE IS FULL           note: LLBT does not have this issue, as it can be unlimited size but its slower
# Case 2: BINARY TREE IS NOT FULL AND WE HAVE TO FIND A VACANT PLACE

# For Case 2, we would have to traverse until left or right child = None

print(newPLBT.insertPLBT('Instruments'))
print(newPLBT.insertPLBT('Wind'))
print(newPLBT.insertPLBT('Brass'))
print(newPLBT.insertPLBT('Flute'))
print(newPLBT.insertPLBT('Recorder'))
print(newPLBT.insertPLBT('Trombone'))
print(newPLBT.insertPLBT('Saxophone'))


print('\n----------------------SEARCH VALUE IN PYTHON LIST BINARY TREE ------------------------')

# Since the tree is a list, we can use a for loop instead of queue to look for our target

print(newPLBT.searchPLBT('Brass'))

print('\n----------------------TRAVERSE PYTHON LIST BINARY TREE ------------------------')

# PREORDER: ROOT -> LEFT CHILD -> RIGHT CHILD (last visit is at the right subtrees right leaf)
# INORDER: LEFT CHILD -> ROOT -> RIGHT CHILD
# POSTORDER: LEFT CHILD -> RIGHT CHILD -> ROOT
# LEVELORDER:  BY LEVELS


print('\nPREORDER: \n')  # PRE: ROOT FIRST
newPLBT.preordertrav(1)

print('\nINORDER: \n')  # IN: ROOT 2ND
newPLBT.inordertrav(1)

print('\nPOSTORDER: \n')  # POST:  ROOT LAST
newPLBT.postordertrav(1)

print('\nLEVELORDER: \n')  # FOR LEVEL WE CAN JUST PRINT THE VALUES CONSECUTIVELY FROM RANGE INDEX TO LASTUSED +1
newPLBT.levelordertrav(1)

print('\n----------------------DELETE VALUE IN PYTHON LIST BINARY TREE ------------------------')
# Find deepest node (which is conveniently in the lastusedindex)
# Replace target node with deepest node
# Delete deepest node

print(newPLBT.deletenode('Flute'))  # Should replace Flute with Saxophone at index 4
newPLBT.levelordertrav(1)

print('\n----------------------DELETE ENTIRE PYTHON LIST BINARY TREE ------------------------')
# For lists we would just have to set the list to None or CustomList = []/None

print(newPLBT.deleteentire())

print('\n----------------------PYTHON LIST BINARY TREE TC SC QUIZ -------------------------')

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


class PLBT_set:

    tc_set = {'Creation of PLBT': 'O1', 'Insertion to PLBT': 'O1', 'Traversing PLBT': 'ON', 'Searching PLBT': 'ON',
              'Deleting node in PLBT': 'ON', 'Deleting entire PLBT': 'O1'}

    sc_set = {'Creation of PLBT': 'ON', 'Insertion to PLBT': 'O1', 'Traversing PLBT': 'O1', 'Searching PLBT': 'O1',
              'Deleting node in PLBT': 'O1', 'Deleting entire PLBT': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning!')
                PLBT_set.assess_tc(PLBT_set.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        PLBT_set.assess_sc(PLBT_set.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                PLBT_set.assess_sc(PLBT_set.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')


PLBT_set.assess_tc(PLBT_set.tc_set)


print('Comparing Linked List Binary Trees to Python List Binary trees, we see that:'
      '\nLinked List BT are more space efficient in creation, and do not have a maxsize'
      '\nConversely, Python List Binary Trees have a maxsize, and need to reserve a set amount of space in memory for N'
      '\nPython List Binary Trees are faster (O1 vs ON) for inserting nodes'
      '\nWith data size, performance of Linked List BT will decrease'
      '\nLinked Lists require ON SC for inserting, deleting, traversing, searching, while Python Lists require O1'
      '\nLinked Lists more flexible for BT that needs frequent modifications,'
      '\nwhile Python List BT may be better for static trees where there are less modification')

