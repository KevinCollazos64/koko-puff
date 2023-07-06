print('\n----------------------------------Circular Doubly Linked Lists-----------------------------------------------')


print('\nCircular Doubly LL: Same as DLL but now last node references the first to run full circle')


class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CDLL:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createCDLL(self, nodevalue):
        newnode = Node(nodevalue)
        self.head = newnode
        self.tail = newnode
        newnode.next = newnode
        newnode.tail = newnode
        return 'CDLL successfully created!'

    def insertnode(self, value, location):
        if self.head is None:
            return 'CDLL DNE!'
        else:
            new = Node(value)
            if location == 0:
                self.head.prev = new
                new.next = self.head
                new.prev = self.tail
                self.tail.next = new
                self.head = new
            elif location == 1:
                self.tail.next = new
                new.prev = self.tail
                new.next = self.head
                self.head.prev = new
                self.tail = new
            else:
                temp = self.head
                index = 0
                while index < location-1:
                    temp = temp.next
                    index += 1
                nextnode = temp.next
                temp.next = new
                new.prev = temp
                new.next = nextnode
                nextnode.prev = new
        return 'Node successfully inserted!'

    def traversalCDLL(self):
        if self.head is None:
            return 'Error the CDLL DNE!'
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next
                if temp.next == self.head:
                    print(temp.value)
                    break
        return 'Traversed!'

    def reversetraverse(self):
        if self.head is None:
            return 'Error the CDLL DNE!'
        else:
            temp = self.tail
            while temp:
                print(temp.value)
                temp = temp.prev
                if temp.prev == self.tail:
                    print(temp.value)
                    break
        return 'Traversed in reverse!'

    def searchCDLL(self, target):
        if self.head is None:
            return 'Error the CDL DNE!'
        else:
            temp = self.head
            while temp:
                temp = temp.next
                if temp.value == target:
                    return {temp.value}
                elif temp == self.tail:
                    break
            return 'Value not found'

    def deletenode(self, location):
        if self.head is None:
            return 'Error CDLL DNE!'
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                temp = self.head
                index = 0
                while index < location-1:
                    temp = temp.next
                    index += 1
                temp.next = temp.next.next
                temp.next.prev = temp
        return 'Node deleted'

    def deleteentire(self):
        if self.head is None:
            return 'Error the CDLL DNE!'
        else:
            self.tail.next = None
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next
            self.head = None
            self.tail = None
            return 'Successfully deleted CDLL!'


circdub = CDLL()

print('\n-----------------------------Circular Doubly Linked Lists Creation-----------------------------------------')

# create node with nodevalue, set head, tail, new.prev, new.next references to this node
print(circdub.createCDLL(1))

print('\n------------------------Circular Doubly Linked Lists Insertion (Beg, middle, end)----------------------------')
# check head, if exists, check location parameter
# 0: head.prev = new//new.next = head//new.prev = tail//tail.next = new//head = new
# 1: tail.next = new//new.prev = tail//new.next = head//head.prev = new//tail = new
# else: loop to loc -1, next = temp.next, temp.next = new, new.prev = temp, new.next = next, next.prev = new

print(circdub.insertnode(2, 1))
print(circdub.insertnode(3, 1))
print(circdub.insertnode(4, 1))
print(circdub.insertnode(5, 1))

print('\n----------------------Circular Doubly Linked Lists Traversal (forward and reverse) -------------------------')
# Logic: loop through all nodes, printing their values and checking if the node you are on is tail. If tail, BREAK

print(circdub.traversalCDLL())
print(circdub.reversetraverse())

print('\n-------------------------Circular Doubly Linked Lists Search ----------------------------')
# check head. if exists, loop through each node, comparing to target, stop if found target or if temp == tail to break

print(circdub.searchCDLL(3))
print(circdub.searchCDLL(20))

print('\n----------------------Circular Doubly Linked List Node Deletion (Beg, Mid, End) -------------------------')
# beg: only 1 node: all references to null
# beg: multiple nodes: head.next = head//tail.next = head.next//head.next.prev = tail
# end: only 1 node: all references to null
# end: multiple nodes: head.prev = tail.prev // tail.prev.next = head// tail.prev = tail
# mid: loop to loc-1, curr.next = curr.next.next//curr.next.next.prev = curr

print(circdub.deletenode(2))
print(circdub.traversalCDLL())

print('\n----------------------Circular Doubly Linked List Node Entire Deletion -------------------------')
# Not enough to remove all links going forward, but also the ones going backward
# Loop through each node changing references to null

print(circdub.deleteentire())

print('\n----------------------Circular Doubly Linked List Node Entire TC and SC quiz -------------------------')

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


class CDLL_set:

    tc_set = {'Creation of CDLL': 'O1', 'Insertion to CDLL': 'ON', 'Traversing CDLL': 'ON', 'Searching CDLL': 'ON',
              'Deleting node in CDLL': 'ON', 'Deleting entire CDLL': 'ON'}

    sc_set = {'Creation of CDLL': 'O1', 'Insertion to CDLL': 'O1', 'Traversing CDLL': 'O1', 'Searching CDLL': 'O1',
              'Deleting node in CDLL': 'O1', 'Deleting entire CDLL': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning!')
                CDLL_set.assess_tc(CDLL_set.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        CDLL_set.assess_sc(CDLL_set.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                CDLL_set.assess_sc(CDLL_set.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')


CDLL_set.assess_tc(CDLL_set.tc_set)

