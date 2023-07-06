print('\n----------------------QUEUE -------------------------')

print('\nFollows FIFO order (FIRST in first out), complete OPPOSITE of LIFO in Stacks'
      '\nCan be visualized as a queue IRL. The first person in line gets out first'
      '\nWe need queue when apps use first coming data first (ex: Printer queue, call center phone systems)'
      '\nSimilar to Stacks, there are many ways we can implement a queue (List w/o limit, List w/Limit, Linked List'
      '\nHowever, Linked List Queues are superior in terms of time and space complexities, although more difficult'
      '\nIf we set a max size to a python list, queue becomes time efficient, but the set up takes On space in memory'
      '\nIf we dont set a max size, it does not take up space, but instead will be very slow timewise because deleting'
      '\nand inserting elements at the beginning requires constant shifting of elements to the left, taking On TC'
      '\nLinked List implementation does not face any of these issues, but is harder to set up')

print('\n----------------------CREATE QUEUE USING LINKED LIST + Operations-------------------------')
# Create Queue class
# Create object of LinkedList class (head points to null, tail points to null)
# Then we can start enqueuing elements
# When we enqueue an element to a queue LL, we are basically inserting the node at the end of the LL
print('\nOperations for a Queue LL are: Enqueue (like push), Dequeue (like pop), Peek, isEmpty, deleteEntire')


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


LLQ = Queue()
print(LLQ.isempty())
print(LLQ.enqueue(1))
print(LLQ.enqueue(2))
print(LLQ.enqueue(3))
print(LLQ.enqueue(4))
print(LLQ.enqueue(5))
print(LLQ.isempty())
print(LLQ.dequeue())  # Should reflect FIFO
print(LLQ.peek())
print(LLQ.delete())

print('\n------------LIST W/O MAX SIZE, LIST W/ MAX SIZE, LINKED LIST QUEUE OPERATIONS TC AND SC QUIZ---------------')


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


class Queue_list_set:

    tc_set = {'Creation of LIST W/O MAX SIZE Queue': 'O1', 'Enqueue': 'ON', 'Dequeue': 'ON', 'Peek': 'O1',
              'isEmpty': 'O1', 'isFull': '-', 'Delete entire Queue': 'O1'}

    sc_set = {'Creation of LIST W/O MAX SIZE Queue': 'O1', 'Push': 'O1', 'Pop': 'O1', 'Peak': 'O1',
              'isEmpty': 'O1', 'isFull': '-', 'Delete entire Queue': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning!')
                Queue_list_set.assess_tc(Queue_list_set.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        Queue_list_set.assess_sc(Queue_list_set.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                Queue_list_set.assess_sc(Queue_list_set.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')


Queue_list_set.assess_tc(Queue_list_set.tc_set)

print('\nEnqueue and Dequeue both take ON TC for a list without a set max size. This is because although there is no'
      '\nlimit to how many elements you can add, once max capacity has been reached in memory after an enqueue call,'
      '\nrelocation of data occurs which will take ON tc. Similarly when we dequeue, we remove first element of list,'
      '\nwhich means the rest of the elements shift one step ,left, which takes ON TC.')


class Queue_listmax_set:

    tc_set = {'Creation of LIST W/ MAX SIZE Queue': 'O1', 'Enqueue': 'O1', 'Dequeue': 'O1', 'Peek': 'O1',
              'isEmpty': 'O1', 'isFull': 'O1', 'Delete entire Queue': 'O1'}

    sc_set = {'Creation of LIST W/ MAX SIZE Queue': 'ON', 'Enqueue': 'O1', 'Dequeue': 'O1', 'Peek': 'O1',
              'isEmpty': 'O1', 'isFull': 'O1', 'Delete entire Queue': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning!')
                Queue_listmax_set.assess_tc(Queue_listmax_set.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        Queue_listmax_set.assess_sc(Queue_listmax_set.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                Queue_listmax_set.assess_sc(Queue_listmax_set.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')

Queue_listmax_set.assess_tc(Queue_listmax_set.tc_set)

print('If we give queue list a max size, it becomes faster but takes up space because we reserve N number of cells'
      'in memory corresponding with the length we need our list to be')

class Queue_LL_set:

    tc_set = {'Creation of LINKED LIST Queue': 'O1', 'Enqueue': 'O1', 'Dequeue': 'O1', 'Peek': 'O1',
              'isEmpty': 'O1', 'isFull': 'O1', 'Delete entire Queue': 'O1'}

    sc_set = {'Creation of LINKED LIST Queue': 'O1', 'Enqueue': 'O1', 'Dequeue': 'O1', 'Peek': 'O1',
              'isEmpty': 'O1', 'isFull': 'O1', 'Delete entire Queue': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning!')
                Queue_LL_set.assess_tc(Queue_LL_set.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        Queue_LL_set.assess_sc(Queue_LL_set.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                Queue_LL_set.assess_sc(Queue_LL_set.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')

Queue_LL_set.assess_tc(Queue_LL_set.tc_set)

print('\nUsing a LinkedList for a Queue solves our time and space problems.'
      '\nPython also has other queue modules with respective usages: Collections, Queue, and Multiprocessing Modules')

