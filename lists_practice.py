
# Lists are data structures that hold an ORDERED collection of items that can be of varying data types (order does not
# change once declared)


# Elements in a list have a relationship with their corresponding indices, called mapping.
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

    def ask_shoulduse ():
        answers = ['Y', 'N']
        ans = str((input('Should we use arrays in this situation? Input y for yes and n for no (remove spaces)')).upper())
        if ans not in answers:
            print ('Please provide a valid input.')
            Question.ask_shoulduse()
        return ans

print ('-----------------------------------------------LISTS -----------------------------------------------'
       '\nLists share some similar logic with arrays in terms of accessing and use of indices, but can store data of varying data types.')


print ('-----------------------------------------------Creating a List-----------------------------------------------')
empty_list = []
print('Empty List:', empty_list)
sample_list = [2, 'Oranges', ['Coconuts', 2.56]]
print('List with elements:', sample_list)


print('-----------------------------Accessing/Traversing (with and without editing element)List-----------------------'
    '\nLists follow the same logic as arrays here.')

sample_list[2] = 6
print('Same list with updated [2]:', sample_list)

def traverse_list(any_list):
    print('Traversing list...')
    for i in any_list:
        print(i)

traverse_list(sample_list)

def alter_element(any_list):
    print('\nEditing elements of list...')
    for i in range(len(any_list)):
        any_list[i] = str(any_list[i]) + '+'
        print(any_list[i])

alter_element(sample_list)

print('\n-------------------Inserting to a list (beginning, end, middle, list to another list-----------------')

print('There are various methods to append to a list: \nlist.append(y)\nlist.extend(newlist) (to add list to another list)\nlist.insert(index,value)')

sample_list.append('Potatoes')
print('using append:', sample_list)

sample_list.extend([1, 2, 3])
print('After adding new list:', sample_list)

sample_list.insert(0, 3.14)
print('using insert at index 0:', sample_list)

print('\n-------------------------------------------Slice/Delete from a List------------------------------------------')
print('\nSlicing works with this syntax: slice[ : ] where its inclusive before the colon and exclusive after.'
      '\nIf referring to the beginning or end, you can leave the corresponding side blank')

sample_list[:2] = ['x', 'y']
print('\nSlicing first 2 elements of list...', sample_list)

print('\nOther methods for deleting are \nlist.pop(x)- returns element at index x, or if blank will return last'
      '\ndel list[x] - does not return element like pop, can be used to delete more than one element'
      '\nlist.remove(value) - useful when you do not know the index'
      '\nRemember that all methods will move all elements left or right after deletion if not deleting at the end')

print('Popping last value of list...', sample_list.pop(), '\nNew list:', sample_list)

del sample_list[:1]
print('Using del to eliminate first element:', sample_list)

sample_list.remove('Potatoes')
print('Using remove to eliminate Potatoes from the list:', sample_list)

print('\n-------------------------Search for element in List (IN operator and Linear Search)------------------------')


def in_search(any_list, value):
    if value in any_list:
        return any_list.index(value)
    else:
        return False


print('Testing for value present using IN operator:', in_search(sample_list, 'Oranges+'))
print('Testing for value not present using IN operator:', in_search(sample_list, 6500))


def linear_search(any_list, value):
    for i in any_list:
        if i == value:
            return any_list.index(value)
    return False


print('Testing linear search for present value:', linear_search(sample_list, 1))
print('Testing linear search for absent value:', linear_search(sample_list, 121000))

print('\n-------------------------Other list operators------------------------'
      '\n+(concatenate lists)\n*(multiplies instances of elements)\nmin()max() (returns corresponding element)\nsum()')

a = [1, 2, 3]
b = ['a', 'b', 'c']
c = a + b
print('Concatenating...', c)

d = a*3
print ('Multiplying...', d)

print('Maximum:',max(a))

print('Minimum:', min(a))

print('Sum:', sum(a))

print('\n-------------------------Lists and Strings------------------------'
      '\nStrings can be split up into their component characters and put into a list using list(var)'
      '\nSimilarly a string of multiple words can be split up using var.split()')

dummy_string = 'Antidisestablishmentarianism Antidisestablishmentarianism Antidisestablishmentarianism'
new_dummy = list(dummy_string)
print('Splitting dummy string...', new_dummy)

dummy_split = dummy_string.split()
print('Splitting dummy by words...', dummy_split)

delimiter = 'a'
split_delim = dummy_string.split(delimiter)
print('Splitting by delimiter "a" (case sensitive)...', split_delim)

print ('Rejoining...', delimiter.join(split_delim))

print('\n-------------------------List Drawbacks-----------------------'
      '\nList methods directly modify the argument and return none. Opposite of string methods which returns a new'
      'string and leaves the original alone.')

myList = [2, 4, 5, 3, 2]
hold = myList
myList = myList.sort()
print(myList)
print(hold)

print('Good way to avoid these issues is to store the original list in another variable')

print('\n-------------------------List vs. Arrays-----------------------')

print('\nBoth DS are mutable\nBoth can be iterated and indexed through\nBoth can be sliced'
      '\nHowever, arrays are more optimized for arithmetic computations (numpy module useful)')


print('\n-------------------------List TC and SC-----------------------')


class Lists:

    tc_set = {'Creating List': 'O1', 'Inserting value at end of list': 'O1', 'Inserting value anywhere else': 'ON',
              'Traversing given list': 'ON', 'Accessing given cell': 'O1', 'Searching given value': 'ON',
              'Deleting value at the end': 'O1', 'Deleting value anywhere else': 'ON'}

    sc_set = {'Creating List': 'ON', 'Inserting value at end of list': 'O1', 'Inserting value anywhere else': 'O1',
              'Traversing given list': 'O1', 'Accessing given cell': 'O1', 'Searching given value': 'O1',
              'Deleting value at the end': 'O1', 'Deleting value anywhere else': 'O1'}

    def assess_tc(tc_dict):
        for key in tc_dict:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_dict[key]:
                print('Incorrect! From the beginning...')
                Lists.assess_tc(tc_dict)
            else:
                print('Correct!')
                continue
        print('Well done! Onto space complexities...')
        Lists.assess_sc(Lists.sc_set)

    def assess_sc(sc_dict):
        for key in sc_dict:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_dict[key]:
                print('Incorrect! From the beginning...')
                Lists.assess_tc(sc_dict)
            else:
                print('Correct!')
                continue
        print('Well done!')


Lists.assess_tc(Lists.tc_set)

