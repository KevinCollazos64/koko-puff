
# Arrays are particularly efficient for numerical data.

# Numpy module, and array module are different ways to create an array with better memory efficiency than

# a list.

# Elements are stored as contiguous blocks of memory without pointers, reducing memory overhead.

# Array elements are randomly placed in RAM but guaranteed to be contiguous.


# Arrays can only store objects of the same data type.

# Arrays must have a pre-declared size and data type, so it is useful particularly when you know the amount

# of elements you are going to interacting with.


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


#1-D

# Create (array module, numpy module, when empty and when throwing values)
from array import *
import numpy as np

print ('-----------------------------------------------LEGEND -----------------------------------------------'
       '\nTC = Time Complexity\nSC = Space Complexity')
print ('-----------------------------------------------1-D Create (array module, numpy module, when empty and with values) -----------------------------------------------')

# create empty

empty_array = array('i', [])
print ('Empty array:', empty_array)

# create with values

sample_array1 = array('i', [1,2,3,4])
sample_array2 = np.array([[5,6,7,8], [9,10,11,12]])


print ('Array module:',sample_array1, '\n','Numpy module:', sample_array2)



# Insert (beginning, middle, end, full)
print ('-----------------------------------------------1-D Insert (beginning, middle, end, full array) -----------------------------------------------')

# beginning
sample_array1.insert(0,0)
print('Insert Beginning:', sample_array1)

# middle
sample_array1.insert(2,10)
print ('Insert Middle:', sample_array1)

# end
sample_array1.append(100)
print ('Insert End:', sample_array1)

# full array
sample_array1.insert(4,20)
print ('Insert to a Full array:', sample_array1)

print ('Note that the TC for insertion varies on insertion point!')

# Traverse (all elements)
print ('-----------------------------------------------1-D Traverse (all elements) -----------------------------------------------')

def traverse_array(arr):
    for i in arr:
        print (i)

traverse_array(sample_array1)

# Access (check index parameter)
print ('-----------------------------------------------1-D Access (check index parameter) -----------------------------------------------')
def access_element(arr, index):
    if len(arr) < index:
        print ('No index of that number in this array')
    else:
        print (arr[index])


access_element(sample_array1, 10)
access_element(sample_array1, 2)

# Search for a value
print ('-----------------------------------------------1-D Search for a value -----------------------------------------------')
def search_array(arr, value):
    for i in arr:
        if i== value:
            return True
    return 'Value not found'

print(search_array(sample_array1, 100))

# Delete a value
print ('-----------------------------------------------1-D Delete a value -----------------------------------------------')

sample_array1.remove(100)
print (sample_array1)
print('Remember that the TC of deletion varies with deletion point!')

# TC and SC of all operations for 1-D array
print ('-----------------------------------------------1-D TC and SC for all operations -----------------------------------------------')
class one_dimension:

    tc_set = {'1-D Creating empty array':'O1','1-D Insertion at the end': 'O1', '1-D Insertion anywhere else:': 'ON',
              '1-D Traversal': 'ON', '1-D Accessing a given cell': 'O1', '1-D Searching a given value': 'ON',
              '1-D Deleting a value at the end': 'O1', '1-D Deleting a value anywhere else': 'ON'}

    sc_set = {'1-D Creating empty array':'ON','1-D Insertion': 'O1',
              '1-D Traversal': 'O1', '1-D Accessing a given cell': 'O1', '1-D Searching a given value': 'O1',
              '1-D Deleting a value': 'O1'}

    def assess_tc (tc_set):
        for key in tc_set:
            print (key)
            ans = str(Question.ask_tc())
            if ans != tc_set[key]:
                print ('Incorrect! From the beginning!.')
                one_dimension.assess_tc(tc_set)
            else:
                print ('Correct!')
                continue
        print ('Now time for space complexity!')
        one_dimension.assess_sc(one_dimension.sc_set)

    def assess_sc (sc_set):
        for key in sc_set:
            print (key)
            ans = str(Question.ask_sc())
            if ans != sc_set[key]:
                print ('Incorrect! From the beginning!.')
                one_dimension.assess_sc(sc_set)
            else:
                print ('Correct!')
                continue
        print ('Well done!')



one_dimension.assess_tc(one_dimension.tc_set)

#2-D

# Create (numpy module, when empty and when throwing values)
print ('-----------------------------------------------2-D Create (numpy module, when empty and when throwing values) -----------------------------------------------')
twodarr = np.array([[1,2,3,4],
                    [5,6,7,8]])
empty_twodarr = np.array('i', [])

print ('2-D array with values:', twodarr, '\n 2-D array without values:', empty_twodarr)
# Insert (a row, and a column with axis parameter)
print ('-----------------------------------------------2-D Insert (a row (0), and a column (1) with axis parameter) -----------------------------------------------')
newrow_twodarr = np.insert(twodarr, 2, [9,10,11,12], axis=0)
newcol_twodarr = np.insert(twodarr, 0, [9,1], axis=1)

print ('Row added:', newrow_twodarr, '\nColumn added:', newcol_twodarr)
# Access
print ('-----------------------------------------------2-D Access (check index parameter)-----------------------------------------------')

print ('index moves up down, then left right following a[i][j] where [i] is the row and [j] is the column')

def access_2D(arr, row_index, col_index):
    if row_index >= len(arr) or col_index >= len(arr[0]):
        print ('That index does not exist in this array!')
    else:
        print (arr[row_index][col_index])

access_2D(twodarr,2, 1)
access_2D(twodarr, 1, 1)
# Traverse
print ('-----------------------------------------------2-D Traversal -----------------------------------------------')

def traverse_2D(arr):
    for i in range (len(arr)):
        for j in range(len(arr[0])):
            print (arr[i][j])

traverse_2D(twodarr)

# Search
print ('-----------------------------------------------2-D Search element  -----------------------------------------------')

def search_2D(arr, target):
    for i in range (len(arr)):
        for j in range (len(arr[0])):
            if arr[i][j] == target:
                print (f'Target found at row {i} column {j}')
                break
    return ('Value not found in this array')

search_2D(twodarr, 5)
print (search_2D(twodarr, 10))

# Delete
print ('-----------------------------------------------2-D Delete (using numpy built in function) -----------------------------------------------')
new2D_delrow = np.delete (twodarr, 0, axis = 0)
new2D_delcol = np.delete (twodarr, 1, axis = 1)

print ('Deleted row:', new2D_delrow)
print ('Deleted column:', new2D_delcol)

# TC and SC of all operations for 1-D array
print ('-----------------------------------------------2-D TC and SC for all operations -----------------------------------------------')

class two_dimension:

    tc_set = {'2-D Creating empty array': 'O1', '2-D Insertion at the end': 'O1', '2-D Insertion anywhere else:': 'OMN',
              '2-D Traversal': 'OMN', '2-D Accessing a given cell': 'O1', '2-D Searching a given value': 'OMN',
              '2-D Deleting a value at the end': 'O1', '2-D Deleting a value anywhere else': 'OMN'}

    sc_set = {'2-D Creating empty array': 'OMN', '2-D Insertion': 'O1',
              '2-D Traversal': 'O1', '2-D Accessing a given cell': 'O1', '2-D Searching a given value': 'O1',
              '2-D Deleting a value': 'O1'}

    def twod_assessTc (tc_set):
        for key in tc_set:
            print (key)
            ans = str(Question.ask_tc())
            if ans != tc_set[key]:
                print ('Incorrect. Restart!')
                two_dimension.twod_assessTc(two_dimension.tc_set)
            else:
                print ('Correct!')
                continue
        print ('Well done! Now time for space complexities!')
        two_dimension.twod_assessSC(two_dimension.sc_set)

    def twod_assessSC (sc_set):
        for key in sc_set:
            print (key)
            ans = str(Question.ask_sc())
            if ans != sc_set[key]:
                print ('Incorrect. Restart!')
                two_dimension.twod_assessSC(two_dimension.sc_set)
            else:
                print ('Correct!')
                continue
        print ('Great Job!')

two_dimension.twod_assessTc(two_dimension.tc_set)

print ('-----------------------------------------------When to use and avoid arrays? -----------------------------------------------')

class situational:

    useoravoid_arr = {'To store values of the same data type': 'Y', 'To store values of different data types' : 'N',
              'To access random numbers': 'Y', 'To optimize reserve memory': 'N'}

    def assess_situations(situation_set):
        for key in situation_set:
            print (key)
            ans = str(Question.ask_shoulduse())
            if ans != situation_set[key]:
                print ('Incorrect. From the beginning!')
                situational.assess_situations(situational.useoravoid_arr)
            else:
                print ('Correct!')
                continue
        print ('Well done! All finished with array section!')
        situational.additional_notes()

    def additional_notes():
        print ('Here are some additional notes to enhance your understanding of arrays:\n Arrays are great for accessing random numbers because it will always take O(1) TC.'
               '\nArrays are not optimal when you need to consider reserve memory because it takes memory in RAM that may not be fully utilized'
               '\nWhen you add to an already full array, the system will create a brand new array of larger size and copy paste elements onto the new array, greatly affecting its performance'
               '\nSimilarly, if we wanted to play around with variables of different data types, a new array would have to be made for each data type, so arrays should be avoided in this context'
               '\nIn summary, arrays are quick at accessing elements and good for same data type or when you know the number of elements, but'
               '\nwhen it comes to having different data types, inserting new elements anywhere besides the end, or for searching/traversing, arrays take up too much space/ are too slow')

situational.assess_situations(situational.useoravoid_arr)




