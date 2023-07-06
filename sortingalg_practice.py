import math


print('-----------------------------------------SORTING ALGORITHMS-----------------------------------------------\n')

#                                              SORTING
#                                           /          \
#                               Space used                    Stability
#                               /       \                       /    \
#                         in place   out place             stable     unstable

# in place : sorting alg does not req extra space for sorting (ex: bubble sort)
# out place: sorting alg requires extra space for sorting  (ex: merge sort)

# stable sorting: If sorting alg after sorting does not change sequence of similar content in which they appear,
# then this sorting is called stable sorting (ex: insertion sort)

# unstable sorting: sequence does change (ex: quick sort)

# for example, lets say we sort [10, 20a, 15, 30, 20b]
# stable sort would output : [10, 15, 20a, 20b, 30]
# unstable sort would output : [10, 15, 20b, 20a, 30]    **original order of 20 is swapped**

# practical uses of sorting: Excel (built-in functionality), Online shopping (sort by review, price, etc)
# the first of various kinds of sorting is bubble sorting

# Sorting terminology:

# Increasing order: If successive element greater than the previous     ex: 1,2,3,4,5
# Decreasing order: If successive element less than previous    ex: 5,4,3,2,1
# Non-increasing order: If successive element is less than or equal to previous     ex: 11,9,7,7,5
# Non-decreasing order: If successive element is greater than or equal to previous    ex: 1,3,3,5,7

# Essentially, NON indicates duplicate values

print('\n-----------------------------------------BUBBLE SORT-----------------------------------------------\n')
# Repeatedly compare adjacent elements and switch them if they are in the wrong order
# After one full run of bubble sort, the largest element has moved to the right edge and is considered fully sorted
# Continues until all elements are fully sorted
# [3,4,2,1] -> [(3,4),2,1] -> [3,(4,2),1] -> [3,(2,4),1] -> etc until largest value all the way to the right & repeats

def bubsort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):  # use -i-1 b/c we are comparing adjacent pairs
            if a[j] > a[j+1]:  # every time we decrease number of loops as we sort any given element
                a[j], a[j+1] = a[j+1], a[j]
    print(a)

a = [1,5,8,2,3,4]

bubsort(a)

print('\nUse bubble sort when:'
      '\n - Input is already sorted'
      '\n - Space is a concern'
      '\n - Easy to implement (just 2 nested for loops)\n'
      '\nAvoid bubblesort when:'
      '\n - Time is a concern (average tc is on^2 very poor)')

print('\n-----------------------------------------SELECTION SORT-----------------------------------------------\n')
# Divides given array into sorted and unsorted
# Repeatedly find the minimum element and move it to the sorted part
# Finds min in [3,2,4,1] -> Sorted [1], Unsorted[3,2,4] -> Sorted [1,2], Unsorted [3,4] etc

def selecsort(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i+1):  # another loop w/ i+1 bc we have to compare elements
            if a[min_index] > a[j]:  # if minindex > curr index, set curr index as the new minimum
                min_index = j
    print(a)


selecsort(a)


print('\nUse selection sort when:'
      '\n - We have insufficient memory'
      '\n - Easy to implement \n'
      '\nAvoid selection sort when:'
      '\n - Time is a concern (average tc is on^2 very poor)')

print('\n-----------------------------------------INSERTION SORT-----------------------------------------------\n')
# Divides array into sorted and unsorted
# Takes first element from unsorted array and finds correct position in sorted array
# Repeats until unsorted array is empty (loop of some kind)
# [3,2,4,1] -> Sorted[3], Unsorted[2,4,1] (no comparisons because first element in sorted)
# -> Next is 2, compare 2 with 3 since its already in sorted, calculate it comes before so now Sorted [2,3]

def insersort(a):
    for i in range(1, len(a)):  # range starts from 1 bc we compare current element w/ next element, and 1 is next
        key = a[i]  # current element = i
        j = i-1  # previous element = j
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1  # we include this bc every time we will take the previous element (Stops from running infinitely)
            a[j+1] = key
    return a


print(insersort(a))

print('\nUse insertion sort when:'
      '\n - We have insufficient memory'
      '\n - Easy to implement '
      '\n - When we have continuous inflow of numbers and want to keep them sorted\n'
      '\nAvoid insertion sort when:'
      '\n - Time is a concern (average tc is on^2 very poor)')


print('\n-----------------------------------------BUCKET SORT-----------------------------------------------\n')
# Creates buckets and distributes elements of array into buckets
# Sorts buckets individually and merges buckets after sorting

# numbuckets = round(sqrt(numelements))
# appropriate bucket = ceil(value * numbuckets/maxValue) where maxValue is the greatest value in the array

def bucksort(a):
    numberbuckets = round(math.sqrt(len(a)))
    maxValue = max(a)
    arr = []

    for i in range(numberbuckets):
        arr.append([])  # here we create 2-d arrays
    for j in a:  # then loop through elements of list, applying formula to find which cell they go in
        index_b = math.ceil(j*numberbuckets/maxValue)
        arr[index_b-1].append(j)

    for i in range(numberbuckets):
        arr[i] = insersort(arr[i])  # add element to the right bucket num

    k = 0
    for i in range(numberbuckets):  # looks through the number of buckets
        for j in range(len(arr[i])):  # for each of the buckets, we merge them inside list
            a[k] = arr[i][j]
            k += 1
    return a


print(bucksort(a))


print('\nUse bucket sort when:'
      '\n - Input is uniformly distributed over range (ex: 1,2,3,4,5 NOT 1,2,3,55,56,57)\n'
      '\nAvoid bucket sort when:'
      '\n - Space is a concern')

print('\n-----------------------------------------MERGE SORT-----------------------------------------------\n')
# An example of a divide and conquer algorithm (divides problem into small chunks)
# Divides input array into 2 halves and keeps halving recursively until becomes too small to be broken further
# Merges halves by sorting them (sortorder())

def merge(a, l,m,r):
    n1 = m-l+1  # num elements in first sub array
    n2 = r-m  # num elements in second sub array

    L = [0] * n1  # L & R arrays based on number of each element
    R = [0] * n2

    for i in range (0, n1):  # adds elements to left sub array
        L[i] = a[l+i]

    for j in range(0, n2):  # adds elements to right sub array
        R[j] = a[m+1+j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]  # when we merge, has to be in sorted order
            i+=1
        else:
            a[k] = R[j]
            j+=1
        k += 1
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1


def mergesort(a,l,r):
    if l < r:
        m = (l + (r - 1)) // 2
        mergesort(a, l, m)
        mergesort(a, m + 1, r)  # +1 because m in included
        merge(a, l, m, r)
    return a


print(mergesort(a, 0, 5))

print('\nUse merge sort when:'
      '\n - You need a "stable" sort'
      '\n - Average expected time is O(NlogN)\n'
      '\nAvoid bucket sort when:'
      '\n - Space is a concern')


print('\n-----------------------------------------QUICK SORT-----------------------------------------------\n')
# Selects first number as pivot
# Aim is to get all numbers less than pivot on the left, and all numbers more than pivot on the right

# Then, you switch the pivot with the last small number before the list of bigger numbers
# In short, quicksort uses pivot function recursively, for the L & R list

def swap(a, ind1, ind2):
    a[ind1], a[ind2] = a[ind2], a[ind1]

# Pivot function 1) rearranges to have pivot in middle
# and 2) returns the swap index


def pivot(a, pivind, endind):
    swapind = pivind  # When we start quicksort, swap ind and piv ind are the same number (first)
    for i in range(pivind +1, endind+1):  # Then we need to loop, so we can use loop variable i
        if a[i] < a[pivind]:  # then we check if [i] <.> pivot number. If > pivot, go next. If <pivot, we swap
            swapind +=1
            swap(a, swapind, i)  # Runs through all elements of the list. At end we need to still swap
        swap(a, pivind, swapind)  # the element located at index of swap with the pivot index
        return swapind  # not returning the value, but instead the index!


def quicksort(a, left, right):  # L& R indices of list ,respectively
    if left<right:  # base case so it doesnt run infinitely (if left = right, we only have one element in list = sorted)
        pivind = pivot(a, left, right)
        quicksort(a, left, pivind -1)
        quicksort(a, pivind+1, right)
    return a

def quicksorthelper(a):
    return quicksort(a, 0, len(a)-1)

print(quicksorthelper(a))


print('\n-----------------------------------------HEAP SORT-----------------------------------------------\n')
# 1) Insert data to BH
# 2) Extract data to BH

# This is best suited for arrays, and will not work with linked lists
# Heapsort typically always uses min heap (all elements get sorted by the nature of minimum heaps)


def heapify (a, n, i):  # initialize smallest number as the first index that comes from param
    smallest = i
    l = 2*i + 1  # These are the formulas to calculate left and right child
    r = 2*i + 2

    # If LC<root, smaller # = LC. If RC<root, smaller # = RC
    # We find smallest # so we put it as a node in the heap tree

    if l < n and a[l] < a[smallest]:
        smallest = l
    if r < n and a[r] < a[smallest]:  # we check if smallest number is != root, which is i index
        smallest = r  # then in that case we swap smaller w/ the rootnode
    if smallest != i:
        a[i], a[smallest] = a[smallest], a[i]
        heapify (a, n, smallest)

def heapsort(a):
    n = len(a)
    for i in range (int(n/2)-1, -1, -1):  # -1 step, and will continue until 0 (exclusive)
        heapify(a, n, i)

    for i in range(n-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)  # returns in descending order

    return a  # returns in descending order

print(heapsort(a))


print('\n----------------------SORTING ALG TC SC QUIZ -------------------------')


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


class sortalg_set:

    tc_set = {'Bubble sort': 'ON^2', 'Selection sort': 'ON^2', 'Insertion sort': 'ON^2', 'Bucket sort': 'ONLOGN',
              'Merge sort': 'ONLOGN', 'Quick sort': 'ONLOGN', 'Heap sort': 'ONLOGN'}

    sc_set = {'Bubble sort': 'O1', 'Selection sort': 'O1', 'Insertion sort': 'O1', 'Bucket sort': 'ON',
              'Merge sort': 'ON', 'Quick sort': 'ON', 'Heap sort': 'O1'}

    def assess_tc(tc_set):
        for key in tc_set:
            print(key)
            ans = Question.ask_tc()
            if ans != tc_set[key]:
                print('Incorrect! From the beginning!')
                sortalg_set.assess_tc(sortalg_set.tc_set)
            else:
                print('Correct!')
                continue
        print('Great! Onto space complexities...')
        sortalg_set.assess_sc(sortalg_set.sc_set)

    def assess_sc(sc_set):
        for key in sc_set:
            print(key)
            ans = Question.ask_sc()
            if ans != sc_set[key]:
                print('Incorrect! From the beginning!')
                sortalg_set.assess_sc(sortalg_set.sc_set)
            else:
                print('Correct!')
                continue
        print('All done!')


sortalg_set.assess_tc(sortalg_set.tc_set)
