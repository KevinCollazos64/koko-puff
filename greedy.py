print('---------------------GREEDY ALGORITHMS--------------------------\n')
# An algorithmic paradigm that builds the solution piece by piece, one at a time
# Finding the best local solutions = greedy
# Beneficial for solutions where local optimal solution(greedy choice) leads to global solution

# Examples:
#  - Insertion Sort(Divide array into sorted and unsorted, from unsorted we put first element in perfect sorted location)
#  - Selection Sort(Divide arr into sorted and unsorted, chooses min value and puts it in perfect sorted location)
#  - Topological Sort(Each node 1 by 1, checks if fulfills criteria of greedy choice (if node != global optimal solxn)
#  - Prim's Algorithm(Tries to minimize edges between vertices - finds min edge until we get our global solxn)
#  - Kruskal Algorithm(Selects min edges, adds increasing cost of edges at each step, attempts to avoid cycles)
#  - Dijkstra
#  - Activity Selection Problem
#  - Coin change problem
#  - Fractional knapsack problem

print('---------------------ACTIVITY SELECTION PROBLEM--------------------------\n')
print('\nGiven N number of activities with start and end time, select the maximium number of activities that can be' 
      '\nperformed by a single person, assuming that a person can only work on a single activity at a time')

# Key word in greedy algorithm is freeze - at a given point in time, we take the best solution, freeze it, then we never
# come back to it

# Looking at the problem carefully, we can solve by sorting the finish time

activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]]

# This is a 2-D array so we can sort using lambda function

# Sort activities based on a finish time
# Select first activity from sorted array and print it
# For all remaining activities:
#   If the start time of this activity is greater or equal to finish time of previously selected activities,
#   Then select that activity and print it

def maxactivities(activities):
    activities.sort(key = lambda x:x[2])  # sort on first activity
    i = 0
    first = activities [i][0]
    print(first)
    for j in range(len(activities)):
        if activities[j][1] > activities[i][2]:  # if start of current activity (j) > end time of last activity (i)
            print(activities[j][0])
            i = j


print(maxactivities(activities))

# TC : NLOGN b/c sorting 2-d and for loop iterating each element
# SC : O1 uses constant space

print('\n---------------------COIN CHANGE PROBLEM--------------------------\n')
print('\nYou are given coins of different denominations and a total amount of money' 
      '\nFind the minimum number of coins that you need to make up the given amount')

# Inf supply { 1, 2, 5, 10, 20, 50, 100, 1000}
# Ex 1) Total = 70
#       answer = 2 - > 50 + 20 = 70


# Greedy b/c we find the biggest coin < total num
# Add this coin to result and subtract coin from total
# If Total = 0: print result else repeat step 1 and 2

def coinchange(totalnum, coins):
    n = totalnum
    coins.sort()
    index = len(coins)-1
    while True:
        coinvalue = coins[index]
        if n >= coinvalue:
            print(coinvalue)
            n = n - coinvalue
        if n < coinvalue:
            index -= 1
        if n == 0:
            break

# TC: O(N) b/c while loop visits all coins in coin list
# SC: O1



print('\n---------------------FRACTIONAL KNAPSACK--------------------------\n')
print('\nGiven a set of items, each with a weight and value, determine the number of each item to include in a'
      '\n collection such that the total weight is less than or equal to a given limit and the total value is as large '
      '\n as possible')

# EX) Trying to hit max value product while staying within weight limit
# 20 KG VALUE 100, 30 KG VALUE 120, 10 KG VALUE 60

# Essentially calculate density or ratio for each item
# Sort the items based on this ratio
# Take items w/ the highest ratio sequentially until weight allows
# Add the next item as much (fractional) as we can

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value/weight


def knapsack(items, capacity):
    items.sort(key = lambda x: x.ratio, reverse=True)  # for descending order
    usedcapacity = 0
    totalvalue = 0
    for i in items:
        if usedcapacity + i.weight <= capacity:
            usedcapacity += i.weight
            totalvalue += i.value

        else:
            unusedweight = capacity - usedcapacity  # If exceeds weight, takes fraction of value and adds it
            value = i.ratio * unusedweight
            usedcapacity += unusedweight
            totalvalue += value

        if usedcapacity == capacity:
            break
    print(totalvalue)

# TC: ONLOGN b/c we are sorting and iterating through a list
# SC : O1


