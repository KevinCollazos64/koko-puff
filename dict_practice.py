
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


print('\n-----------------------------------------------Dictionaries-----------------------------------------------')

# Dictionaries are a collection of elements that are unordered, changeable, and indexed.
# Can think of dictionaries as coatroom, where your output is based on the key you input (name:coat belonging to name)


print ('\n------------------------------------------Creating Dictionary-----------------------------------------------')

empty_dict = {}
sample_dict = {'Kevin': 5000, 'Johan': 2300, 'goldfish': 'The snack that smiles back'}

print('Empty dict:', empty_dict, '\nDict with values:', sample_dict)

print('Dictionary order may vary from what you declared, because elements are not indexed with integers (rather keys)')

print('\n-----------------------------------------Dictionaries in Memory-----------------------------------------'
      '\nDictionaries are implemented using hash tables. Dict are arrays whose indexes are obtained using hash function'
      '\non the keys. Goal of hash function is to distribute keys evenly in the array in memory'
      '\nHash table is a way of doing key-value lookups. Values are stored in an array and then hash function is used'
      '\nto find index of the array cell that corresponds to your key-value pair'
      '\nGood hash functions minimize the number of collisions(different keys having the same hash value = same index)'
      '\nand solve collisions by adding new values to element already present as a linked list')


print('When we create a dict such as:', sample_dict,
      '\nHash function calculates index of any value pair based on the key value, and after finding the index, it'
      '\nplaces it in memory. Starts with the very first pair')

print('\n---------------------------------------Insert/Update element in Dict-----------------------------------------'
      '\n(Generally using assignment operator which updates value or if its new will put it right in the dict)')

sample_dict['Kevin'] = 'No longer 5000'
sample_dict['Rafael'] = 'New'
print('Changing Kevin and adding Rafael...', sample_dict)


print('\n-----------------------------------------Traversing Dictionaries-----------------------------------------')


def traverse_dict(any_dict):
    for key in any_dict:
        print (key, any_dict[key])
    print('Traversed all elements!')


traverse_dict(sample_dict)

print('\n------------------------------Search element in Dictionary(Linear search)--------------------------------')


def search_dict(any_dict, value):
    for key in any_dict:
        if value == any_dict[key]:
            return key, value
    return 'Value not found in this dictionary'


print(search_dict(sample_dict, 2300))

print('\n-------------------------Delete/Remove from Dictionary(pop, popitem, clear, del)-----------------------------')

pop = sample_dict.pop('Kevin')
print(sample_dict, 'value returned and removed based on key using dict.pop(key)', pop)

popitem = sample_dict.popitem()
print(sample_dict, 'arbitrary removed pair using dict_popitem()', popitem)

del sample_dict['goldfish']
print(sample_dict, 'Goldfish pair removed using del dict[key] based on key')

print('\nTo delete entire dict, can use dict.clear() or del dict')

print('\n-----------------------------------Dictionary Methods-----------------------------------')

dict_methods = {'dict.copy():':'returns shallow copy of dictionary without modify original', 'dict.fromkeys(sequence[], value)':
                'returns a new dict w/ given sequence of elements as the keys of the dictionary', 'dict.get(key, value)':
                'searches for a key in dict, returns value if key is not found', 'dict.items()':
                'returns view object displaying list of dictionaries key value tuple pairs', 'dict.keys()':
                'returns view object that displays list of all keys in the dict', 'dict.setdefault(key, default_value)':
                'searches key, if DNE inserts it with value as default_value', 'dict.values()':'view object w/ values',
                'dict.update(other_dict)': 'updates dict w/ elements from iterable of key value pairs'}

traverse_dict(dict_methods)

print('\nSample dict:', sample_dict)
copy_sample = sample_dict.copy()
print('\nCopying...', copy_sample)

new_dict = {}.fromkeys([1, 'a', 2.5], 0)
print(f'Creating new dict with sequence and all values 0... {new_dict}')

exist = new_dict.get('a', 'not found')
print(f'\nGetting existent value... {exist}')

non_exist = new_dict.get('b', 'not found')
print(f'\nGetting non existent value... {non_exist}')

print(f'\nPrinting items...', new_dict.items())

print(f'\nPrinting keys...', new_dict.keys())

new_dict.setdefault('New', 'Inserted')
print(f'\nInserting new key with default value if DNE...{new_dict}')


print(f'\nSame call for key that already exists...', new_dict.setdefault('a', 'Inserted'))


print(f'\nPrinting values...{new_dict.values()}')

other_dict = {'Random': 500, 'Time': 'Essence'}

new_dict.update(other_dict)
print(f'\nUpdating dict...{new_dict}')

print('\n----------------------------------Dictionary operations/built-in functions-----------------------------------')

dict_functions = {'in operator': 'tells you if something appears as a key in the dictionary, boolean', 'for operator':
                  'for each instance of x, do y. Useful to visit all keys of dictionary', 'all()':
                  'returns true when all elements in iterable are true. if not, returns false', 'any()':
                  'returns true if any element in the collection is true', 'len()': 'returns num items in collection',
                  'sorted(iterable, reverse(boolean), key)': 'returns sorted list of items in iterable based on key.'}

traverse_dict(dict_functions)

print('\nIn operator checking if Random is present...', 'Random' in new_dict, 'Random' in new_dict.values())

print(f'\nAll() and Any()...{all(new_dict)}{any(new_dict)}')

print(f'\ndict len...{len(new_dict)}')

sample_nums = [1, 2, 3, 4, 5, 6]
new_nums = sorted(sample_nums, reverse=True)
print(f'\nSorting...{new_nums}')

print('\n----------------------------------Dictionary vs. Lists-----------------------------------')

list_qual = ['Ordered', 'Access via index', 'Collection of elements', 'Preferred if have ordered data', 'Duplicates']
dict_qual = ['Unordered', 'Access via keys', 'Collection of key-value pairs', 'Preferred if have unique key values',
             'No duplicates allowed']


def differences(qual1, qual2):
    for i in qual1:
        print('List qualities:', i)
    for i in qual2:
        print('Dictionary qualities:', i)
    print('Done!')


differences(list_qual, dict_qual)

print('\n-----------------------------------------Dictionary TC and SC-----------------------------------------------')


class Dict:

    dict_tc_set = {'Creating dict': 'OLENDICT', 'Inserting value in dict': 'O1', 'Traversing dict': 'ON',
               'Accessing cell': 'O1', 'Searching value': 'ON', 'Deleting value': 'O1'}

    dict_sc_set = {'Creating dict': 'ON', 'Inserting value in dict': 'O1', 'Traversing dict': 'O1',
               'Accessing cell': 'O1', 'Searching value': 'O1', 'Deleting value': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning')
                Dict.assess_tc(Dict.dict_tc_set)
            else:
                print('Correct!')
                continue
        print('Well done! Onto Space complexities...')
        Dict.assess_sc(Dict.dict_sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning')
                Dict.assess_sc(Dict.dict_sc_set)
            else:
                print('Correct!')
                continue
        print('All done with this section!')


Dict.assess_tc(Dict.dict_tc_set)











