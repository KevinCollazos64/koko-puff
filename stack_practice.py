print('\n----------------------STACK -------------------------')

print('\nFollows LIFO order (Last in first out )'
      '\nCan be visualized as a stack of plates. The last plate you stack will be the first to access'
      '\nWe need stack when apps use last coming data first (ex: back button on browser)')

print('\n----------------------CREATE STACK W/O SIZE LIMIT USING LIST -------------------------')
# initialize an empty list or linked list in stack class

# Lists : Easy implement. Speed problem when list gets larger
# Goal is to provide easy fast access to random elements in the list
# Becomes a problem when system needs to reallocate memory due to list size exceeding block of memory

# Linked Lists: Harder to implement. Fast performance
# Memory is not an issue because elements are not located contiguously


class Stack:
    def __init__(self):
        self.list = []  # initializes a list stack without size limit

    def __str__(self):  # prints values in stack vertically
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isempty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):  # pushes new value into stack
        self.list.append(value)
        return 'element added'

    def pop(self):  # Memory allocation (usually reserves few items more than needed) leads to O(N) TC. Worst case ON^2
        if self.isempty():
            return 'Empty list'
        else:
            return self.list.pop()   # returns but does not remove top element

    def peek(self):
        if self.isempty():
            return 'Empty list'
        else:
            return [len(self.list)]

    def delete(self):
        self.list = None
        return 'Deleted list'


print('\n-------------- LIST W/O SIZE LIMIT STACK OPERATIONS (push, pop, peak, isempty, delete)----------------------')

customstack = Stack()
print(customstack.isempty())
print(customstack.push(1))
print(customstack.push(2))
print(customstack.push(3))
print(customstack.push(4))
print(customstack.pop())
print(customstack.peek())
print(customstack.delete())

print('\n----------------------CREATE STACK W/ SIZE LIMIT USING LIST -------------------------')


class Stacklimit:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.list = []

    def isempty(self):
        if self.list == []:
            return True
        else:
            return False

    def isfull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False

    def push(self, value):
        if self.isfull():
            return 'List is full'
        else:
            self.list.append(value)

    def pop(self):  # Memory allocation (usually reserves few items more than needed) leads to O(N) TC. Worst case ON^2
        if self.isempty():
            return 'Empty list'
        else:
            return self.list.pop()  # returns but does not remove top element

    def peek(self):
        if self.isempty():
            return 'Empty list'
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        self.list = None
        return 'Deleted list'


print('\n-------------- LIST W/ SIZE LIMIT STACK OPERATIONS (isFull, isEmpty push, pop, peak, delete)-----------------')

limitstack = Stacklimit(5)
print(limitstack.isempty())
print(limitstack.push('eggs'))
print(limitstack.push('bacon'))
print(limitstack.push('grits'))
print(limitstack.push('sausage'))
print(limitstack.push('waffles'))
print(limitstack.isfull())
print(limitstack.pop())
print(limitstack.peek())
print(limitstack.delete())

print('\n-------------- LIST STACK OPERATIONS TC AND SC QUIZ-----------------')


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


class Stack_list_set:

    tc_set = {'Creation of LIST Stack': 'O1', 'Push': 'O1/ON^2', 'Pop': 'O1', 'Peek': 'O1',
              'isEmpty': 'O1', 'Delete entire stack': 'O1'}

    sc_set = {'Creation of LIST Stack': 'O1', 'Push': 'O1', 'Pop': 'O1', 'Peek': 'O1',
              'isEmpty': 'O1', 'Delete entire stack': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning!')
                Stack_list_set.assess_tc(Stack_list_set.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        Stack_list_set.assess_sc(Stack_list_set.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                Stack_list_set.assess_sc(Stack_list_set.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')


Stack_list_set.assess_tc(Stack_list_set.tc_set)


print('\n----------------------CREATE STACK USING LINKED LIST + OPERATIONS -------------------------')
# create stack
# create object of linked list class
# Once blank stack created, insert elements using push method
# Every time we push a node to the stack, we insert the node to the beginning of the LL
# This means we change the next reference to point to the first node in the list
# Operations: pop (removes head reference. In case of LL the first element is the one which is inserted last)
# peek (returns value of most recently added element, which in case of LL is the head reference)
# isEmpty (if self.head = None, list is empty)
# delete (self.head = None and all nodes will be deleted)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


class Stack:  # Creates stack with only head value and this value points to None (because currently empty)
    def __init__(self):
        self.LinkedList = LinkedList()


    def isempty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        return 'Value added!'

    def pop(self):
        if self.isempty():
            return 'Error, LL is empty'
        else:
            nodevalue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodevalue

    def peek(self):
        if self.isempty():
            return 'Error, LL is empty'
        else:
            nodevalue = self.LinkedList.head.value
            return nodevalue

    def deleteall(self):
        self.LinkedList.head = None
        return 'Successfully deleted'


LLstack = Stack()
print(LLstack.isempty())
print(LLstack.push(1))
print(LLstack.push(2))
print(LLstack.push(3))
print(LLstack.push(4))
print(LLstack.push(5))
print(LLstack.isempty())
print(LLstack.pop())
print(LLstack.peek())
print(LLstack.deleteall())

print('\n--------------LINKED LIST STACK OPERATIONS TC AND SC QUIZ-----------------')


class Stack_LL_set:

    tc_set = {'Creation of LL Stack': 'O1', 'Push': 'O1', 'Pop': 'O1', 'Peek': 'O1',
              'isEmpty': 'O1', 'Delete entire stack': 'O1'}

    sc_set = {'Creation of LL Stack': 'O1', 'Push': 'O1', 'Pop': 'O1', 'Peek': 'O1',
              'isEmpty': 'O1', 'Delete entire stack': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning!')
                Stack_LL_set.assess_tc(Stack_LL_set.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        Stack_LL_set.assess_sc(Stack_LL_set.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                Stack_LL_set.assess_sc(Stack_LL_set.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')


Stack_LL_set.assess_tc(Stack_LL_set.tc_set)
