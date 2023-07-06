
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


print('\n----------------------------------------------Tuples-----------------------------------------------')

print('\nTuples are a sequence of values, similar to a list'
      '\nValues stored can be any type, and they are indexed by integers'
      '\nTuples are comparable (can be sorted), hashable (can use as key values in a dictionary), and are IMMUTABLE'
      '\nAn object is hashable if it has a value that remains the same throughout its lifetime'
      '\nImmutable means cannot change after declaration')

print('\n----------------------------------------------Creating Tuples-----------------------------------------------')

t = 'a', 'b', 'c', 'd'
t2 = ('a', 'b', 'c')

print('If creating tuple with only one value, must include comma at the end or it will be treated as a string')

t_onevalue = ('a',)

print(t, t2, t_onevalue)

print('\n-----------------------------Tuples in Memory/Accessing element-----------------------------------------------')

print('\nComputer memory can be visualized as a grid'
      '\nElements of tuple are stored contiguously on grid, optimizing access because the computer knows where to look'
      '\nVarious list operators work for Tuples as well (slicing, indexing)'
      '\nHowever, in list, we can modify any element using bracket operator, but with tuples we cannot (immutable)')

# slicing is [inclusive:exclusive]

slice = t[1:2]
print(slice, t2[0])

print('\n-----------------------------Traversing Tuples (same as list)-----------------------------------------------')

# using for i


def traverse_tup(any_tup):
    for i in any_tup:
        print(i)
    print('Done!')


# using rangelen


def range_tup(any_tup):
    for i in range(len(any_tup)):
        print (any_tup[i])
    print('Complete!')


traverse_tup(t)
range_tup(t2)


print('\n---------------------------Search in Tuple(in op., tup.index(value)------------------------------------------')

print('a' in t)
print(t.index('c'))

def search_tup(any_tup, value):
    for i in range(0, len(any_tup)):
        if any_tup[i] == value:
            return f'{value} found at {i} index'
    return 'Value not found'


print(search_tup(t, 'a'))


print('\n--------------------Tuple Operations/Functions(+, *, in, count, index, len, min, tuple)----------------------')

print('\nTuples respond to + and * like lists but the result is a new tuple, not a string')
t3 = t+t2
print(t3)

t4 = t2*3
print(t4)


# prints frequency of input value

print(t4.count('a'))
print(len(t))

# converts list to tuple

nums = [1, 2, 3, 4]
print(tuple(nums))

print(min(nums))

print('\n--------------------------------------Tuple additional info---------------------------------------------')

print('\nFunctions that work for both lists and tuples are: len, max, min, sum, any, all, sorted, count, index'
      '\nTuples can be stored in lists, and lists can be stored in Tuples. Both can be nested!'
      '\nWe generally use tuples for heterogeneous data types, and lists for homogenous data types.'
      '\nIterating a tuple is faster than a list because it is immutable.'
      '\nIf you are dealing with data that will not change, using a tuple guarantees it will be protected.')

print('\n---------------------------------------Tuple TC and SC-----------------------------------------------------')


class Tup:

    tc_set = {'Creating Tuple': 'O1', 'Traversing Tuple': 'ON', 'Accessing given element': 'O1', 'Searching value': 'ON'}
    sc_set = {'Creating Tuple': 'ON', 'Traversing Tuple': 'O1', 'Accessing given element': 'O1', 'Searching value': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print ('Incorrect! From the beginning!')
                Tup.assess_tc(Tup.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        Tup.assess_sc(Tup.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                Tup.assess_sc(Tup.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')

Tup.assess_tc(Tup.tc_set)

