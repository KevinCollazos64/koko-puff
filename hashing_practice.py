print('---------------------HASHING--------------------------\n'
      '\nHashing is a method of sorting and indexing data\n'
      'Allows large amounts of data to be indexed using keys commonly created by formulas\n')

# Say we want to store "Apple" "Application" and "Appendix"
# Each string goes through a function that assigns it a number unique to that string
# Every time that string goes through the function it will always yield same result
# Then these numbers get stored in some data structure (list, array) based on index
# Which can then be accessed based on their index and would take O(1) TC


print('\nHashing is very time efficient in case of insertion, deletion, search operation;\n'
      'Array/Python List - OLOGN (only in ideal condition, must be sorted, otherwise its ON)\n'
      'Linked List - ON (must traverse all elements in worst case)\n'
      'Tree - OLOGN (only if tree is balanced)\n'
      'Hashing - O1/ON (if hash has few collisions, takes O1. More could mean ON')


# Terminology:

# Hash function - Function that can be used to map data of arbitrary size to data of fixed size
# Key - Input data by the user
# Hash value - A value returned by the Hash function
# Hash table - Data structure that implements associative array abstract data type, a structure that
# can map keys to the values
# Collision - When two different keys to a hash function produce the same hash value (output)
# In python, dictionaries are using the same logic as hash tables

print('\n---------------------HASH FUNCTIONS--------------------------\n')

# Ex 1) Mod function - Takes int as input, returns smaller value to be used as index


def mod(int, numbercells):
    return int%numbercells

print(mod(500, 15))
print(mod(2400, 9))

# Ex 2) ASCII function - Takes strings as input, and returns a number

def modASCII(string, numbercells):
    total = 0
    for i in string:
        total += ord(i)
    return total%numbercells

# A good hash function is one that distributes hash values uniformly across hash tables (avoids collisions)
# And it has to use all the input data (to avoid collisions)


print('\n---------------------COLLISION RESOLUTION TECHNIQUES--------------------------\n')
# Direct chaining - Implements the buckets as linked list. Colliding elements are stored in this list
# ^ This means every cell in hash table will store the reference of linked list, so we do not store the string itself
print('\n Direct chaining- \n1) Create new node and store the phys. loc of this node at the index'
      '\n2) Example: node created, phys. loc is 222. So we insert 222 in index 3'
      '\n3) If we get index 3 from another string as well, we assign new node to node that exists in the index'
      '\n In other words we update the nodes next reference to the new node created')

# By direct chaining we are not actually inserting values to the hash table

print('\nOpen addressing - Colliding elements are stored in other vacant buckets. During storage and lookup these'
      '\nare found through probing (linear, quadratic)\n'
      '\nLinear probing - When you encounter duplicate index, continue linearly to the next vacant cell'
      '(ex: 2 is dup, go 3)\n'
      '\nQuadratic probing - Add arbitrary quadratic polynomial to the index until empty cell is found'
      '(ex: 2 is dup, add 2^2)\n'
      '\nDouble Hashing - Interval between probes is computed by another hash function')


print('\n---------------------HASH TABLE IS FULL--------------------------\n')
print('\nDirect Chaining- Using DC, full hash table is never an issue b/c we can just link whatever new node has a'
      '\nduplicate index to the element at that index already\n'
      '\nOpen Addressing - Here you would just create 2x size of the current hash, and recall hashing for current keys')

# When we create new hash table, affects performance because we call hash functions for all strings in the old hash to
# insert to the new hash. If num string = N, may take ON Tc


print('\n---------------------PRO/CON OF COLLISION TECHNIQUES--------------------------\n')

print('\nDirect chaining:'
      '\n - Uses reference and Pointer'
      '\n - We do not have a fear of exhausting hash table buckets, because hash table never gets full'
      '\n - Can infinitely add nodes, but this affects the TC (becomes closer to ON)'
      '\n - A huge Linked List will cause performance leaks\n')

print('\nOpen addressing:'
      '\n - Easy implementation (just create array based on hash function, assign values based on hash values'
      '\n - When hash table is full, creation of new hash table affects performance (TC becomes closer to ON\n')

print('\nIF INPUT SIZE IS KNOWN, ALWAYS USE OPEN ADDRESSING (bc we dont want to create a new hash table)'
      '\n - We never exhaust hash tables since input is known and it will still search fast.)\n'
      '\nIF DELETION OPERRATION IS VERY HIGH, then in this case we use DIRECT CHAINING. This is because'
      '\nif we use open addressing, frequent deletion may leave empty cells (performance leaks) and is not efficient SC')

print('\n---------------------PRACTICAL USES OF HASHING--------------------------\n')

print('\n1) Passwords on servers - When we try to log in, password we enter is converted into a hash, then the server\n'
      'checks if value exists in the database or not. If it exists, we can login. Hashing is also one way traffic\n'
      'meaning we can only get a hash value from a key, not a key from a hash value. This makes password storing safe')

print('\n2) File systems - File path is mapped to physical location on a disk. Hashing is what a system uses to know\n'
      'the exact location of these files in hard disk sectors. File path would be the key, and then is converted to a\n'
      'hash value. This hash value is used to store physical location of that file on hard disk.')

print('\n---------------------PROS AND CONS OF HASHING--------------------------\n')

print('\nPROS:\n'
      '- On average; Insertion, deletion, search operations take O1 TC (minimal collisions)\n'
      '- A well constructed and evenly distributed hash table can achieve a constant TC\n'
      '\nCONS:\n'
      '- When hash function is poor, insertion/deletion/search takes ON TC in the worst case')

