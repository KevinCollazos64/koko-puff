print('\n----------------------BINARY HEAP-------------------------\n')

print('\nBinary heaps are binary trees with some additional properties:'
      '\n1) A binary heap is either a MIN heap or a MAX heap;'
      '\nMin heap has the root as the minimum amongst all values in the BH (any node must be LESS than children)'
      '\nMax heap has the root has the maximum amongst all values in the BH (any node must be MORE than children)\n'
      '\n2) A binary heap is always a complete tree; This means all levels are completely filled except for the last,'
      '\nand the last level has its keys as leftmost as possible (makes BH ideal for PLIST or array implementation)')


# In the case of fixed size array, we don't want any cells to be empty because they take up space in memory. A complete
# Tree ensures that most of the array will be filled

# We need BH for problems where we have to satisfy these conditions:
# Find min/max number among set of numbers in logN time
# Additional insertions cannot take more than OLOGN time

# Our possible solutions include storing elements in a sorted array (finding min: O1, insertion ON)
# Storing in a linked list (but insertion still takes ON)
# Our last solution is a binary heap, which GUARANTEES that insertions will only take OLOGN time

# BH is the heart of Prim's Algorithm, Heap sort, and priority requeue (you need BH to solve these)

# Implementation options for BH:
# 1) Array or list (Array is usually best suited for BH)
# 2) Reference/pointer implementation

# Looking back at the Binary Tree section, LC and RC are stored in memory using equations (LC = 2X, RC = 2X+1)
# This is also how binary heaps are stored in memory

print('\n----------------------BINARY HEAP CREATION-------------------------\n')
# initialize a fixed size list
# set heapsize to 0


class Binaryheap:
    def __init__(self, maxsize):
        self.customlist = (maxsize + 1) * [None]
        self.heapsize = 0
        self.maxsize = maxsize + 1  # We add 1 because we will not use cell O (to simplify our math)



newBH = Binaryheap(5)
print(newBH)

print('\n----------------------BINARY HEAP OPERATIONS-------------------------\n')
# PEEK - Returns the "peak" of the tree, which should always be index 1


def peekBH(rootnode):
    if not rootnode:
        return 'Error with root!'
    else:
        return rootnode.customlist[1]  # we know rootnode resides in the index of 1


# HEAPSIZE - Returns the number of filled cells

def getheapsize(rootnode):
    if not rootnode:
        return 'Error with root!'
    else:
        return rootnode.heapsize


# LEVEL ORDER TRAVERSAL (mainly using this type because we use this traversal in our insertion and deletion methods)

def levelordertravbh(rootnode):
    if not rootnode:
        return 'Error with root!'
    else:
        for i in range (1, rootnode.heapsize + 1):  # don't start at 0 b/c 0 cell should be empty. heapsize +1 accounts
            print(rootnode.customlist[i])


print('\n----------------------BINARY HEAP INSERTION -------------------------\n')
# Firstly we need a helper function, heapify which compares given index to its parents and makes adjustments if needed


def heapifyTreeInsert(rootnode, index, heaptype):  # index of node we want to adjust, and heaptype is either max or min
    parentindex = int(index/2)  # LC index = 2X
    if index <= 1:
        return
    if heaptype == 'Min':
        if rootnode.customlist[index] < rootnode.customlist[parentindex]:  # in min heap, child must > parent
            temp = rootnode.customlist[index]  # assign index violating heap property to a temp variable
            rootnode.customlist[index] = rootnode.customlist[parentindex]  # switch the indices of parent and child
            rootnode.customlist[parentindex] = temp  # assign parent index to temp
        heapifyTreeInsert(rootnode, parentindex, heaptype)  # recursive call for left OR right child
    elif heaptype == 'Max':
        if rootnode.customlist[index] > rootnode.customlist[parentindex]:  # in max heap, child must < parent
            temp = rootnode.customlist[index]  # assign index violating heap property to a temp variable
            rootnode.customlist[index] = rootnode.customlist[parentindex]  # switch indices
            rootnode.customlist[parentindex] = temp
        heapifyTreeInsert(rootnode, parentindex, heaptype)  # recursive call for left OR right child


# Then we can devise our insert method (check if heapsize full, assign nodevalue to customlist index, add 1 to heapsize,
# and call heapify to make adjustments if needed)    Parameters: root, value of new node, and heaptype

def insertnodeBH(rootnode, nodevalue, heaptype):
    if rootnode.heapsize+1 == rootnode.maxsize:  # + 1 because 0 cell is left empty
        return 'Heap already full!'
    else:
        rootnode.customlist[rootnode.heapsize+1] = nodevalue
        rootnode.heapsize += 1
        heapifyTreeInsert(rootnode, rootnode.heapsize, heaptype)
        return 'Value added!'

insertnodeBH(newBH, 5, 'Max')
insertnodeBH(newBH, 10, 'Max')
insertnodeBH(newBH, 15, 'Max')
insertnodeBH(newBH, 20, 'Max')
insertnodeBH(newBH, 25, 'Max')

print('Level order trav:\n')
levelordertravbh(newBH)
print('\nPeek:', peekBH(newBH))
print('\nGetting heap size...', getheapsize(newBH))

print('\n----------------------BINARY HEAP EXTRACTION -------------------------\n')
# The only node that can be extracted from heap is the ROOTNODE (property of binary heap)
# Before you can extract the root, have to find the last element to replace it (last index)


# Extraction helper function

def heapifytreeextract(rootnode, index, heaptype):  # index of element we want to adjust
    leftindex = index * 2
    rightindex = index * 2 + 1
    swapchild = 0

    if rootnode.heapsize < leftindex:
        return
    elif rootnode.heapsize == leftindex:
        if heaptype == 'Min':  # check if currentnode > child, which is left index, then we swap
            if rootnode.customlist[index] > rootnode.customlist[leftindex]:  # MIN violation (children must be greater)
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[leftindex]
                rootnode.customlist[leftindex] = temp
            return
        else:  # check if current node < leftindex, means that root is <child, so in max heap root must be > child
            if rootnode.customlist[index] < rootnode.customlist[leftindex]:  # this means we switch their values
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[leftindex]
                rootnode.customlist[leftindex] = temp
            return  # Up to here is only the 2nd condition, where we only have left child for the rootnode
    else:  # 3rd condition is if we have 2 children. In case of min heap we have to find the smallest child and swap
        if heaptype == 'Min':  # with the parent.
            if rootnode.customlist[leftindex] < rootnode.customlist[rightindex]:  # in max heap, we find the biggest
                swapchild = leftindex  # child and we swap
            else:
                swapchild = rightindex  # here we are looking for the smallest child, and then replace with parent node
            if rootnode.customList[index] > rootnode.customlist[swapchild]:  # if root > the smallest child, we replace
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[swapchild]
                rootnode.customlist[swapchild] = temp
        else:  # addresses max heap, essentially the reverse of the min code
            if rootnode.customlist[leftindex] > rootnode.customlist[rightindex]:
                swapchild = leftindex
            else:
                swapchild = rightindex
            if rootnode.customlist[index] < rootnode.customlist[swapchild]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[swapchild]
                rootnode.customlist[swapchild] = temp
        heapifytreeextract(rootnode, swapchild, heaptype)


# actual extraction function

def extractnode(rootnode, heaptype):
    if rootnode.heapsize == 0:
        return
    else:
        extractednode = rootnode.customlist[1]
        rootnode.customlist[1] = rootnode.customlist[rootnode.heapsize]
        rootnode.customlist[rootnode.heapsize] = None
        rootnode.heapsize -= 1
        heapifytreeextract(rootnode, 1, heaptype)
        return f'Node Extracted!{extractednode}'


print('Extracting Node...')
print(extractnode(newBH, 'Max'))

print('\n----------------------BINARY HEAP ENTIRE DELETION -------------------------\n')
# just have to set the rootnode custom list to None

def deleteentireBH(rootnode):
    if not rootnode:
        return 'Nothing to delete!'
    else:
        rootnode.customlist = None


print('\n----------------------BINARY HEAP TC SC QUIZ -------------------------')


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


class BH_set:

    tc_set = {'Creation of BH': 'O1', 'Peek BH': 'O1', 'GetHeapsize BH': 'O1', 'Traversing BH': 'ON',
              'Inserting node in BH': 'OLOGN', 'Extracting node in BH': 'OLOGN', 'Delete entire BH': 'O1'}

    sc_set = {'Creation of BH': 'ON', 'Peek BH': 'O1', 'GetHeapsize BH': 'O1', 'Traversing BH': 'O1',
              'Inserting node in BH': 'OLOGN', 'Extracting node in BH': 'OLOGN', 'Delete entire BH': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning!')
                BH_set.assess_tc(BH_set.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        BH_set.assess_sc(BH_set.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                BH_set.assess_sc(BH_set.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')


BH_set.assess_tc(BH_set.tc_set)
