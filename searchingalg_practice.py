import math

print('-----------------------------------------SEARCHING ALGORITHMS-----------------------------------------------\n')
# Need searching algorithms for irl things such as creating new username (alg checks database to confirm username exist)

print('-----------------------------------------LINEAR SEARCH-----------------------------------------------\n')
# Check each element 1 by 1 asking is this what we're looking for?
# TC is O(N) because we're looking through each element
# If we have an unsorted array, linear search is fine.
# If array is sorted, we can use other search algorithms

def linsearch(array ,value):
    for i in range(len(array)-1):
        if array[i] == value:
            return i
    return -1

samp1 = [1,2,3,4,5]

print(linsearch(samp1, 3))

print('-----------------------------------------BINARY SEARCH-----------------------------------------------\n')
# Much faster than linear search, but only works on sorted arrays
# Half of the elements can be eliminated at a time, instead of one by one

# Create fxn with 2 param (sorted_array, value)
# 2 pointers (left at start of arr, right at end) used to calculate middle
# While middle != value and start <= end: if middle > value, move right pointer down... if mid < value, move left up
# If value never found return -1

def binsearch(sorted_arr, target):
    l, r = 0, len(sorted_arr)-1
    m = math.floor((l+r)/2)
    while not (sorted_arr[m] == target) and l <= r:
        if target < sorted_arr[m]:
            r = m-1
        else:
            l = m+1
        m = math.floor((l + r)/2)

    if sorted_arr[m] == target:
        return m
    else:
        return -1


samp2 = [3, 4, 5, 6, 7, 8, 9]
print(binsearch(samp2, 5))

