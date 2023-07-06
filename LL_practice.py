# Linked Lists are a series of independent (un)ordered elements with references to the next and/or last node

# Can't skip over nodes, must visit all previous nodes sequentially before target node

print('\n---------------------------------------Linked Lists-----------------------------------------------------')

print('\nSingly LL: List of nodes storing value and reference to the next node in one direction'
      '\nCircular Singly LL: Same as SLL but now last node in list is referencing first node'
      '\nDoubly LL: Same as SLL but now each node also references the previous node along with the next'
      '\nCircular Doubly LL: Same as DLL but now last node references the first to run full circle')


print('\n---------------------------------------LL in Memory-----------------------------------------------------')

print('\nArrays are contiguously stored in computer memory for easy retrieval. In case of LL elements are randomly'
      '\nallocated in memory and can be accessed through references, allowing for as many nodes as required. This also'
      '\nmeans LL size does not have to be declared beforehand and we cannot access any given element directly since'
      '\nthey are all randomly stored. We can only access target node by visiting every node before it + references'
      '\nHead stores the physical location of the first node'
      '\nTail stores the physical location of the last node')

print('\n------------------------------------Creation of Singly LL--------------------------------------------------')


# 1) Create LL class with head and tail, initialize w/ null

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):  # allows us to print SLL
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):

        newnode = Node(value)  # initializes node value

        if self.head is None:  # if no current head, makes new node the head AND tail
            self.head = newnode
            self.tail = newnode

        else:
            if location == 0:  # if 0, means this is the first node so must reference the physical loc of current head.
                newnode.next = self.head
                self.head = newnode

            elif location == 1:  # if 1, we insert at the end, so current tail.next = new node, and new tail is new node
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode

            else:  # inserting to middle of SLL
                tempnode = self.head
                index = 0
                while index < location:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next  # identify next node in list so we can insert between current and next node
                tempnode.next = newnode
                newnode.next = nextnode
                if tempnode == self.tail:
                    self.tail = newnode

    def traverseSLL(self):
        if self.head is None:
            print ('No head!')
        else:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next

    def searchSLL(self, target):
        if self.head is None:
            print ('SLL DNE!')
        else:
            node = self.head
            while node is not None:
                if node.value == target:
                    return node.value
                node = node.next
            return 'Value DNE in this list'

    def deletenodeSLL(self, location):
        if self.head is None:
            print ('SLL DNE')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next  # head stores loc of first node, so head.next refers to node after first
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                node = self.head
                index = 0
                while index < (location-1):  # we do -1 because we want to land right before the node we want to delete
                    node = node.next
                    index += 1
                nextnode = node.next  # identify the next node so that curr node next is next node next (deletes middle)
                node.next = nextnode.next

    def deleteEntire(self):
        if self.head is None:
            return 'No SLL to delete'
        else:
            self.head = None
            self.tail = None
            return 'Successfully deleted'


# 2) Create Node class with blank node and assign value to it, reference to null

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# 3) Link Head and tail with these nodes

singleLL = SLinkedList()
nodeA = Node(1)
nodeB = Node(2)

singleLL.head = nodeA
singleLL.head.next = nodeB
singleLL.tail = nodeA

print([node.value for node in singleLL])


print('\n----------------------------Insertion to Singly LL (Beg, Mid, End)------------------------------------------')

# Create a new node
# Check if there is any existing nodes or not. If none, insert right away and reference head+tail to this node
# Consider all 3 cases of insertion; Beginning, Middle and End

# Examine method defined under SLinkedList class

singleLL.insertSLL(1, 0)
singleLL.insertSLL(2, 0)
singleLL.insertSLL(3, 0)
singleLL.insertSLL(4, 2)

print([node.value for node in singleLL])

print('\n----------------------------Traversing Single LL------------------------------------------')

# Check if head exists. If no return error
# Start from head (assign variable) and while loop until the end, printing its value

singleLL.traverseSLL()

print('\n----------------------------Search for value in Single LL------------------------------------------')

# Check if head exists. If no return error
# Start from head (assign variable) and while loop until target parameter matches node value
# if nothing found print error message

print(singleLL.searchSLL(4))

print('\n---------------------------Deleting value in Single LL (beg, mid, end)--------------------------------------')

# Check if head exists. If no return error.
# Consider all situations similar to Insertion (beginning, mid, end)
# Method should have location of deletion. 0 = start, 1 = End, 1+ = Anywhere else.
# Define program when loc == 0 and loc == 1 first
# Loop through SLL with an index until the index number matches location of deletion.


print([node.value for node in singleLL])
singleLL.deletenodeSLL(0)
singleLL.deletenodeSLL(1)
singleLL.deletenodeSLL(2)
singleLL.traverseSLL()

print('\n---------------------------------------Deleting entire Single LL---------------------------------------------')

# Check if head exists. If no return error
# Set head and tail to null

singleLL.deleteEntire()
print([node.value for node in singleLL])


print('\n---------------------------------------TC and SC of Single LL---------------------------------------------')


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


class SLL:

    tc_set = {'Creation of SLL': 'O1', 'Insertion to SLL': 'ON', 'Traversing SLL': 'ON', 'Searching SLL': 'ON',
              'Deleting node in SLL': 'ON', 'Deleting entire SLL': 'O1'}

    sc_set = {'Creation of SLL': 'O1', 'Insertion to SLL': 'O1', 'Traversing SLL': 'O1', 'Searching SLL': 'O1',
              'Deleting node in SLL': 'O1', 'Deleting entire SLL': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning!')
                SLL.assess_tc(SLL.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        SLL.assess_sc(SLL.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                SLL.assess_sc(SLL.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')


SLL.assess_tc(SLL.tc_set)

