print('\n----------------------------------Doubly Linked Lists-----------------------------------------------')

print('\nDoubly LL: Same as SLL but now each node also references the previous node along with the next')


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, nodevalue):
        node = Node(nodevalue)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        return 'Successfully created DLL'

    def insertDLL(self, nodevalue, location):
        if self.head is None:
            return 'DLL DNE!'
        else:
            new = Node(nodevalue)
            if location == 0:
                new.prev = None
                new.next = self.head
                self.head.prev = new
                self.head = new
            elif location == 1:
                new.next = None
                new.prev = self.tail
                self.tail.next = new
                self.tail = new
            else:
                temp = self.head
                index = 0
                while index < location-1:
                    temp = temp.next
                    index += 1
                nextnode = temp.next
                new.prev = temp
                temp.next = new
                new.next = nextnode
                nextnode.prev = new
            return 'Inserted!'

    def traverseDLL(self):
        if self.head is None:
            return 'Error, no head!'
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next
        return 'Successfully traversed!'

    def reversetraverseDLL(self):
        if self.head is None:
            return 'Error, no head!'
        else:
            temp = self.tail
            while temp:
                print(temp.value)
                temp = temp.prev
        return 'Traversed in reverse!'

    def searchDLL(self, target):
        if self.head is None:
            return 'Error, no head!'
        else:
            temp = self.head
            while temp:
                if temp.value == target:
                    return {temp.value}
                temp = temp.next
        return 'Value not found'

    def deletenode(self, location):
        if self.head is None:
            return 'Error, no head!'
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                temp = self.head
                index = 0
                while index > location-1:
                    temp = temp.next
                    index += 1
                nextnode = temp.next
                temp.next = nextnode.next
                nextnode.next.prev = temp
        return 'Successfully deleted!'

    def deleteall(self):
        if self.head is None:
            return 'Nothing to delete!'
        else:
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next
            self.head = None
            self.tail = None
        return 'Successfully deleted entire DLL'



print('\n----------------------------------Doubly Linked List Creation-----------------------------------------------')
# create node using parameter nodevalue -> node.next = null, node.prev = null -> head = node, tail = node

doubly = DLL()
print(doubly.createDLL(5))

print('\n----------------------------------Doubly Linked List Insertion (Beg, Middle, End)----------------------------')
# Parameters of nodevalue and location
# same as previous linked lists: check head, if exists check location of insertion.
# Beginning: new.prev = none// new.next = head// head.prev = new// head = new
# End: new.prev = tail // new.next = None // tail.next = new // tail = new
# Middle: loop to loc-1 // curr.next = new// new.prev = current//new.next = curr.next//new.next.prev = new

print(doubly.insertDLL(1, 0))
print(doubly.insertDLL(2, 0))
print(doubly.insertDLL(3, 0))
print(doubly.insertDLL(4, 0))

print('\n-------------------------------Doubly Linked List Traversal (Normal and Reversal)----------------------------')
# Essentially the same as traversing a Singly Linked List
# Check head, if exists, while loop printing the value of each node each iteration

print(doubly.traverseDLL())
print(doubly.reversetraverseDLL())

print('\n-------------------------------Doubly Linked List Search ----------------------------')
# Loop through all values comparing search target with current node

print(doubly.searchDLL(3))

print('\n-------------------------------Doubly Linked List Node Deletion (Beg, Mid, End) ----------------------------')
# Beg only 1 node: head & tail reference to null
# Beg multiple nodes: Change head reference to N2, N2.prev = null
# Med: Loop to loc-1, change current.next to current.next.next, and nextnode.prev to current
# End only 1 node: head and tail reference to null
# End multiple nodes: loop to the end until curr.next = None, self.tail = tail.prev, tail.prev.next = null

print(doubly.deletenode(2))
print(doubly.traverseDLL())

print('\n-------------------------------Doubly Linked List Entire Deletion ----------------------------')
# Head, tail, and every node.prev reference to null

print(doubly.deleteall())

print('\n-------------------------------Doubly Linked List Entire TC and SC quiz---------------------------')

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


class DLL_set:

    tc_set = {'Creation of DLL': 'O1', 'Insertion to DLL': 'ON', 'Traversing DLL': 'ON', 'Searching DLL': 'ON',
              'Deleting node in DLL': 'ON', 'Deleting entire DLL': 'ON'}

    sc_set = {'Creation of DLL': 'O1', 'Insertion to DLL': 'O1', 'Traversing DLL': 'O1', 'Searching DLL': 'O1',
              'Deleting node in DLL': 'O1', 'Deleting entire DLL': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning!')
                DLL_set.assess_tc(DLL_set.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        DLL_set.assess_sc(DLL_set.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                DLL_set.assess_sc(DLL_set.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')


DLL_set.assess_tc(DLL_set.tc_set)




