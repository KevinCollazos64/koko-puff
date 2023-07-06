print('\n----------------------------------Circular Single Linked Lists-----------------------------------------------')


print('\nCircular Singly LL: Same as SLL but now last node in list is referencing first node.'
      '\nThis means the node after the tail is the head node, creating the circular structure of CSLL')
print('\nIf we only have one node, this means it is the head, tail, and it references itself')

print('\n----------------------------------CSLL Creation-----------------------------------------------')

# Creation algorithm: Start -> Parameter (node_value) -> create blank node, node.value = node_value -> node.next = node
# head = node, tail = node -> terminate


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):  # helps us print the CSLL
        node = self.head
        while node:
            yield node
            if node.next == self.tail.next:
                break
            node = node.next

    def createCSLL(self, node_value):
        node = Node(node_value)
        node.next = node
        self.head = node
        self.tail = node
        return 'The CSLL has been created!'

    def insertCSLL(self, value, location):
        if self.head is None:
            return 'CSLL DNE!'
        else:
            newnode = Node(value)
            if location == 0:  # Beginning
                newnode.next = self.head  # links newnode to as the node before the current head (first node)
                self.head = newnode  # head now references newnode as the first node in the LL
                self.tail.next = newnode  # links newnode as coming after the tail (circular definition)
            elif location == 1:  # End
                newnode.next = self.tail.next  # links head as coming after the newnode
                self.tail.next = newnode  # links newnode as coming after the current tail, taking its place as last
                self.tail = newnode  # sets newnode as the new tail in the list
            else:
                tempnode = self.head
                index = 0
                while index > location-1:  # -1 because we want to land before insertion index
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next  # declares node after our tempnode as next
                tempnode.next = newnode  # newnode comes in between our temp and next node
                newnode.next = nextnode  # next now becomes the node that comes after our newnode
            return 'Node inserted'

    def traverseCSLL(self):
        if self.head is None:
            return 'The list does not exist! No head!'
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.next
                if tempnode == self.tail.next:
                    break
        return 'Traversed!'

    def searchCSLL(self, target_value):
        if self.head is None:
            return 'The list does not exist! No head!'
        else:
            tempnode = self.head
            while tempnode:
                tempnode = tempnode.next
                if tempnode.value == target_value:
                    return tempnode.value
                elif tempnode == self.tail.next:
                    return 'Value does not exist in CSLL!'

    def deletenode(self, location):
        if self.head is None:
            return 'The list does not have any values'
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                else:
                    tempnode = self.head
                    while tempnode:
                        tempnode = tempnode.next
                        if tempnode.next == self.tail:
                            break
                        tempnode.next = self.tail.next
                        self.tail = tempnode
            else:
                current = self.head
                index = 0
                while index < location-1:
                    current = current.next
                    index += 1
                nextnode = current.next
                current.next = nextnode.next
        return 'Deleted!'

    def deleteCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None
        return 'Successfully deleted CSLL!'


circular = CSLL()
print(circular.createCSLL(15))

print('\n-----------------------------CSLL Insertion (Beg, Middle, End)------------------------------------------')

# Similar as SLL -> Check if LL exists -> Create new node to be inserted -> check location parameter (0,1, other)
# 0 : newnode.next = head, head = newnode, tail.next = newnode
# 1: newnode.next = tail.next, tail.next = newnode, tail = newnode
# other: loop to location, newnode.next = currentnode.next, currentnode.next = newnode

print(circular.insertCSLL(5, 0))
print(circular.insertCSLL(20, 1))
print(circular.insertCSLL(60, 2))
print(circular.insertCSLL(30, 1))

print('\n-----------------------------CSLL Traversal-----------------------------------------')

# Essentially the same as in a singly linked list.
# check head -> if exists, loop starting from head
# while tempnode: print node.value, temp = temp.next, but when temp = self.tail.next BREAK to prevent infinite loop

print(circular.traverseCSLL())

print('\n-----------------------------CSLL Search-----------------------------------------')

# Check if head exists -> If exists, loop through all elements comparing tempnode.value to target.value
# Break the loop by comparing tempnode to reference of tail

print(circular.searchCSLL(15))
print(circular.searchCSLL(24))

print('\n-----------------------------CSLL Deletion (Beg, Middle, End)-----------------------------------------')

# Beginning: First case, only one node. Change every reference to null
# Beginning: Second case, multiple nodes. Change head reference to second node, and last node to reference second node.
# Middle: Traverse, find target, set prevnode.next to node after target
# End: First case, only one node. Change every reference to null
# End: Second case, multiple nodes. Loop, change last nodes.prev reference to the first node. Change tail reference to
# lastnodes.prev physical address


print(circular.traverseCSLL())

print(circular.deletenode(3))
print(circular.traverseCSLL())

print('\n-----------------------------CSLL Entire Deletion-----------------------------------------')

# Destroy 3 links: head to node 1, tail to last node, and last node to node 1

print('\n-----------------------------CSLL Entire TC/SC-----------------------------------------')


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


class CSLL_set:

    tc_set = {'Creation of CSLL': 'O1', 'Insertion to CSLL': 'ON', 'Traversing CSLL': 'ON', 'Searching CSLL': 'ON',
              'Deleting node in CSLL': 'ON', 'Deleting entire CSLL': 'O1'}

    sc_set = {'Creation of CSLL': 'O1', 'Insertion to CSLL': 'O1', 'Traversing CSLL': 'O1', 'Searching CSLL': 'O1',
              'Deleting node in CSLL': 'O1', 'Deleting entire CSLL': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning!')
                CSLL_set.assess_tc(CSLL_set.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        CSLL_set.assess_sc(CSLL_set.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                CSLL_set.assess_sc(CSLL_set.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')


CSLL_set.assess_tc(CSLL_set.tc_set)

