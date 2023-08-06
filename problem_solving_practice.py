print('--------------------------------------A RECIPE FOR PROBLEM SOLVING  -----------------------------------------\n'
      '\n 1) Understand the problem'
      '\n 2) Look at examples'
      '\n 3) Break it down'
      '\n 4) Solve or simplify'
      '\n 5) Look back and refactor')

# It is better to have a set approach for solving problems so that you can improve over time following the same approach

print('\n--------------------------------------UNDERSTANDING THE PROBLEM -----------------------------------------\n'
      '\n - Restate the entire problem in your own words'
      '\n - What are the inputs that go into the problem?'
      '\n - What are the outputs that come from the problem?'
      '\n - Can the outputs be determined from the inputs? In other words do we have enough info to solve problem?'
      '\n - What should I label the important piece of data that are part of the problem?')

# EX: Write a program that takes 2 numbers and returns their sum
#  - Implement addition
#  - Int, float, or ?
#  - Int, float, or ?
#  - Yes
#  - Add, sum

print('\n----------------------------------------EXPLORE EXAMPLES ----------------------------------------------------\n'
      '\n - Start with a simpler example'
      '\n - Progress to more complex examples'
      '\n - Explore examples with empty input'
      '\n - Explore examples with invalid input')

# These steps help identify concrete examples within the problem

# Ex: Write a function that takes in a string and returns the count of each letter in the string
#   1) Simple example: charCount('bbbb')   output : { b : 4 }
#   2) Complex example: charCount('My name is Kevin')
#   3) Empty example: charCount('')
#   4) Invalid input: charCount(1)

# After coming up with these examples, can use them in code or can ask the interviewer for more clarification

print('\n----------------------------------------BREAK IT DOWN ----------------------------------------------------\n'
      '\n - Write out steps you need to make (basic components of the solution'
      '\n - Writing small comments before your code can help you formulate your approach')

# charCount example:
# declare object to return at the end
# loop over string (visit each character)
# Return obj (dict w/ keys and values)
# Sub comments:
#   - if char is letter and in object add + 1 to value
#   - if char is letter and not in object add char to object w/ value 1

print('\n---------------------------------------SOLVE OR SIMPLIFY ----------------------------------------------------\n'
      '\n If you cannot simplify (ignore the parts giving you trouble):'
      '\n   - Find the core difficulty'
      '\n   - Temporarily ignore that difficulty'
      '\n   - Write simplified solution'
      '\n   - Then, incorporate that difficulty')

# EX: Breaking charCount problem down you could get code like this:
# result = {}
# for i in str.lower():
#     result[i] += 1
# else:
#     result[i] = 1
# return result

# Whats important is that you show something for yourself instead of just being stuck on the hard part

print('\n--------------------------------------LOOK BACK AND REFACTOR-------------------------------------------------\n'
      '\n - Look at the solution you currently have ; Analyze and reflect'
      '\n - Can we check the result?'
      '\n - Can we drive the result differently?'
      '\n - Did we underestimate anything at first glance?'
      '\n - Can we use this method or result for another problem?'
      '\n - Can we improve the performance of the solution? (time complexity and space complexity wise'
      '\n - How would other people solve this problem?')


print('\n-----------------------------------------SUMMARY-----------------------------------------------------------\n'
      '\n 1) Understand problem - Ask questions to interviewer, clarify problem, make sure you completely understand'
      '\n 2) Explore examples - Understand the problem, play around with different inputs, examine nature of output'
      '\n 3) Break it down - Write pseudocode or general comments of the steps you need to take'
      '\n 4) Solve/simplify - Solve, ignore difficult part that is troubling you. Return to it later and implement'
      '\n 5) Look back and refactor - Improve efficiency, legibility')

print('\n-----------------------------------------BACKTRACKING-------------------------------------------------------\n'
      '\n - A general algorithmic technique that considers searching every possible combination in order to solve the'
      '\n computational problem and is a form of recursion\n')

# Uses brute force approach for finding the desired outputs
# Much faster than brute force enumeration of all possible candidates
# Eliminates a large number of candidates with a single test

#                                         brute force approach
#                                       /                       \
#                             Backtracking                  Dynamic programming
#                             (all solutions)               (best solution)

# Many problems solved using backtracking are not optimization problems

print('Backtracking is mostly used when we have multiple solutions and you want all these solutions'
      '\n we can discard several bad states with just one iteration')
# If partial candidate A cannot be completed to a solution, then we can eliminate A as a solution

print('\nThere are 3 types of problems in backtracking:'
      '\n 1) Decision problem - Search for the feasible solution'
      '\n 2) Optimization problem - Search for the best solution'
      '\n 3) Enumeration problem - Find all feasible solutions')

# We can represent all states as a tree, and check if these states are the solutions or not
# By eliminating states, we can improve the performance of backtracking (the main advantage of backtracking)

print('\nIf you consider a tree structure and we apply backtracking, a form of recursion, we are basically'
      '\n using DEPTH-FIRST SEARCH!'
      '\n - Backtracking checks whether given node is a valid solution or not ~ if it is, continue to the child of that'
      '\n node. Else we skip the ENTIRE subtree'
      '\n - Discard several invalid solutions with just one iteration'
      '\n - Enumerates all subtree of the node to find valid solution')

# ex: how many possible ways can we rearrange (red, black, blue)
# ROOT - RED (BLACK, BLUE) or (BLUE, BLACK)
# |     \
# BLACK  BLUE  - (BLACK, RED) or (RED, BLACK)
# (BLUE, RED)
# or (RED, BLUE)

# In case of backtracking, when we solve the problem, those problems will have constraints that we need to check
# constraints and get solution which satisfies

# For example, one constraint could be that red CANNOT be in the middle
# So we check solution 1 by 1, and we eliminate (BLUE, RED, BLACK) and (BLUE, RED, BLACK)

# To the states that are not acceptable solutions, we apply bounding function which improves search performance

print('\n---------------------------------BACKTRACKING VS. BRUTE FORCE APPROACH--------------------------------------\n'
      '\n BACKTRACKING IS FASTER!')

# Lets say we represent a problem like this (nodes represent states, and parent child represents given actions

#                                               Root
#                                             /      \
#                                           A           B
#                                         /   \       /   \
#                                        C    D       E    F
#                                       / \  / \     / \  / \
#                                      G  H  I  J    K  L M  N

# A brute force approach would check A, then B, C, D, E, F, G, H, I, J, K until we get solution K in 12 steps
# Using backtracking we follow a standard depth first search
# We check A, if it satisfies all the constraints that we face in our backtracking problem
# If it does, we move to the next state
# We then check C, and find out it violates constraints
# So now, we apply bounding to kill the state, dismissing the children nodes of the killed state (ignore G and H)
# We go back to A, and now check D. If D also violates, bound and kill the state (ignoring its children)
# Go to B, then visit E (not viable solution) then we go to K (solution found in 10 STEPS!)

# The algorithm essentially backtracks to the previous state if the current one is not feasible





