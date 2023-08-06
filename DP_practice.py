print('--------------------DIVIDE AND CONQUER ALGORITHMS--------------------------\n')
# recursively divide a big problem into sub problems, solve the sub problems and combine to wholistic solution

print('Properties:'
      '\n - Optimal substructure: If any problems overall optimal solution can be constructed from the optimal'
      '\n   solutions of its subproblems , then this problem has optimal substructure.'
      '\n   Ex: Fib(n) = Fib(n-1) + Fib(n-2)'
      '\n Divide and Conquer algorithms are very effective when problem has optimal substructure property')

# Common divide and conquer algorithm:
#    Merge sort - We find solutions for sub arrays, then combine to get main array solution(individually sort and merge)
#    Quick sort - We divide array into 2 sub arrays, recursively apply the same algorithm to each (pivot and left and
#                 right markers, L & R markers move until we find a number greater than the pivot number

print('\n--------------------FIBONACCI SERIES USING DIVIDE AND CONQUER--------------------------\n'
      '\nA series of numbers in which each number is the sum of the two preceding numbers. First two numbers are always'
      '\n 0 and 1.'
      '\n Ex: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55\n'
      '\n Fibonacci(N) = Fibonacci(N-1) + Fibonacci(N-2)'
      '\n   ^ main            ^ sub 1          ^ sub 2'
      '\n   continues until we reach 0 or 1'
      '\n You hit a point where cant be divided any further (aka Fib(2) or Fib(1)'
      '\n Solutions to these sub problems leads us to the larger solution')


print('\n--------------------DYNAMIC PROGRAMMING--------------------------\n')
# breaks problem into subproblems and stores the solution. If we encounter the same problem we use the previous solution

print('\n Dynamic programming is the optimization of Divide and Conquer. We do the same thing in both, but for'
      '\n DP if the problem appears again we use the previous solution instead of solving themm multiple times,'
      '\n increasing efficiency of the algorithm.\n'
      '\n EX: 1 + 1 + 1 + 1 + 1 = 5'
      '\n     1 + 1 + 1 + 1 + 1 + 2 = 7'
      '\n      ^-we-know-5----^\n'
      '\n DP properties:'
      '\n   1) Optimal substructure'
      '\n   2) Overlapping subproblem: Problem has overlapping subproblems if finding its solution involves solving the'
      '\n      same subproblem multiple times.')

# For ex, for fibonacci, once we solve Fib(2), we no longer have to solve Fib(2) anymore as a reptition. We can just use
# one answer for Fib(2) to find larger problem solution

print('\n DP Method 1: Top down w/ memoization'
      '\n- Start from Top(main problem) dividing problem into sub problems. While we solve these sub problems, we store'
      '\n  the result of sub problems in cache, so when we face the same sub problem, we dont solve again = Memoization')

# Fibonacci (n):
#     if n< 1 return error
#     if n = 1 return 0
#     if n = 2 return 1
#     Else return Fibonacci(n-1) + Fibonacci(n-2)

# Two recursive calls, so TC is on**2 which is pretty slow

# According to the fib tree, if we want to find the 6th number of fibonacci series we need to calculate the fibonacci
# series of 5 and fibonacci series of 4
# Then to find the solution for 5, we need to find solution of fib(4) and fib(3)
# This continues until we reach fib(1) or fib(2)

print('\n Optimized Fibonacci:'
      '\n Fibonacci (n):'
      '\n   if n<1 return error'
      '\n   if n=1 return 0'
      '\n   if n=2 return 1'
      '\n   if not n in memo:'
      '\n         memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)'
      '\n   return memo[n]')

# Fib(6) array gets filled as
# _____F1_____F2_____F3_____F4_____F5_____F6_____
#      0      1      -      -      -    F4+F5
#      0      1      -      -    F3+F4  F4+F5
#      0      1      -   F2+F3   F3+F4  F4+F5
#      0      1    F1+F2 F2+F3   F3+F4  F4+F5
#      0      1      1      -      -      -
#      0      1      1      2      -      -
#      0      1      1      2      3      -
#      0      1      1      2      3      5

# We know that first two numbers of fibonacci are 0 and 1, so we can solve F3(0 + 1)


def fibmemo(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n not in memo:
        memo[n] = fibmemo(n-1, memo) + fibmemo(n-2, memo)

    return memo[n]


print('\n DP method 2: Bottom up with Tabulation\n'
      '\n - Tabulation is opposite of the top down approach and avoids recursion.'
      '\n We solve all the related subproblems, and fill up a temporary table. Based on the results in the table, the'
      '\n solution to the original problem is computed'
      '\n Similar to memoization, we solve the problem and maintain a map of already solved sub problems')

# We avoid recursion, allowing TC to improve

# bottom up tabulation logic
# def fibonaccitab(n):
#     tb = [0,1]
#     for i in range(2, n+1):
#           tb.append(tb[i-1] + tb[i-2])
#     return tb[n-1]

# TC: ON
# SC: ON

# b/c index starts from - we avoid recursion her


def fibtab(n):
    tb = [0,1]
    for i in range(2, n+1):  # n-1 b/c index starts from 0
        tb.append(tb[i-1] + tb[i-2])
    return fibtab(n-1)


# we use a temp list to find fibonacci series without calling the method recursively
# TC: ON traversing range N times
# SC: ON b/c we created a temp table  which takes n number of elements

# Top down vs. Bottom up
# _____DCA_____TOPDOWN_____BOTTOMUP_____             <--- Fib numbers
#     O(n**2)      O(n)        O(n)

# TOP DOWN:
#     - Easy to come up w/ solution as it is extension of DCA
#     - Slow (b/c we use recursion)
#     - Unnecessary use of stack (recursion calls)
#     - Use when we need a quick solution

# BOTTOM UP:
#     - Difficult to come up w/ solution
#     - Fast (b/c we eliminate recursion)
#     - Stack is not used (we use memory but not stack)
#     - Use when we need an efficient solution


# Is merge sort DP?
# No, because it does not have the overlapping subproblem property(each time the array is divided, the quotients are
# independent and different from each other (do not have the same solution)). No repetitive sub problems.



