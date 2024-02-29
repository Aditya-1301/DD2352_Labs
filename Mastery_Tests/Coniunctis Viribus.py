# for i,v in enumerate(x):
#     train = []
#     i = 0
#     while sumv < root*root:
#         sumv += v
#         root += 1
#         train.append(v)
#         if sumv >= root*root:
#             trains.append(train)
#             train = []
#             sumv = 0
#             root = 0
#         # elif i == len(x):
#         #     trains.append(x[:i-1])
#         #     x = x[i-1:]
#         #     sumv = 0
#         #     root = 0
#         # else: 
#         #     print(i)
# def min_trains(x):
#     train = []
#     sum_v = x[0]
#     i = 0
#     j = 0
#     root = j - i + 1
#     while sumv >= root * root:
#         if j < n:
#             v = x[j]
#         else:
#             trains.append(train)
#             break
#         if sumv + v < (root + 1) * (root + 1):
#             trains.append(train)
#             train = []
#             sumv = 0
#             i = j
#         else:
#             train.append(v)
#             sumv += v
#             j += 1
#         root = j - i + 1
#     print(trains)


# x = [4, 1, 6, 1, 2]
# trains = set()
# # train = []
# n = 5
# cap = 0
# need = 0


# sum = 0
# root = 0

# for i in range(n):
#     for j in range(i, n, 1):
#         root = j - i + 1
#         sum += x[j]
#         print(sum, root)
#         if sum >= root*root:
#             # sum += x[j]
#             train.append(x[j])
#         else:
#             trains.append(train)
#             sum = 0
#             i = j
# min_trains(x)
# if sum(x) >= n**2:
#     print(1)
# else:
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i <= j:
#             train = tuple(x[i:j])
#             need = j - i + 1
#             cap = sum(train)
#             if cap >= need * need:
#                 trains.add(train)
#                 i = j

# def min_train(x, n):
#     if sum(x) >= n ** 2:
#         return 1
#     else:



# print(trains)


"""
SubProblem:
sum += x[i]
min = inf
for i in range(start, end + 1):
    if sum >= (i-start+1)**2:
        min = min (min, 1 + func(i+1, end))
return min

The main problem is just the sum of each of the subproblems put together

Comments: 
1. I had many different attempts at this question because at first I misinterpreted the question and then I started to realise that my understanding of this question was fundamentally flawed as my understanding of the problem couldn't even make sense of the test case.
2. I hadn't realised that with the statement talking about it starting at any 'i' and going till some 'j' meant it could have any beginning or ending points and each check doesn't always begin with the case of i = 0.
3.

Other possible approaches:
1. Brute Force (Probably not super efficient) -> Another approach wouuld be to continue iterating and finding every possible train sequence and the train iterations where any of the subproblems fail. Keep track of all the trains formed in a matrix and the row with the smallest length should be the answer.
2. Another way to look at this problem can be to go with the approach of thinking of this like the knapsack problem
3. Recursive Solution above makes the most intuitive sense
"""

# def min_train(capacities, start, end):
#     if start > end:
#         return 0
#     if (start, end) in cache: 
#         return cache[(start,end)] 
#     cap = 0
#     current_min_train = float("inf")
#     for i in range(start, end + 1):
#         cap += capacities[i]
#         need = i - start + 1
#         if cap >= (need)**2:
#             current_min_train = min(current_min_train, 1 + min_train(capacities, i+1, end))
#         cache[(start, end)] = current_min_train
#     return current_min_train


# def minT(x, n):
#     if sum(x) >= len(x)**2:
#         return 1 
#     else:
#         return min_train(x, 0, n-1) 


# print(minT(x, n))

"""
My understanding and intuition towards the problem:
1. The first thing to check is if the entire list of capacities fits the criteria for it to be considered a train. That is if the sum of the input capacities list is greater than or equal to the square of its length, then we can just return 1 as the base list itself can be treated as a train.
2. Otherwise my intuition was to go through the list of values and at each level check for the criteria for to form a train, by maintaining a "capacity sum"  which would be compared with the associated need at that level within the list. By this I mean:

Level 1 or when considering the first element in the list: 
capacity_sum = x1 
need = 1

Level 2: 
capacity_sum = x1 + x2
need = 2^2 = 4

...

Level i: 
capacity_sum = x1 + x2 + x3 + ... xi
need = (i-1+0+1)^2 = i^2

we reset the start = i and capacity_sum = 0, when the criteria fails. After this we continue iterating through the list. 

This was my original intuition towards the problem but I soon realized that this approach would fail. This was because, I didn't consider that by this logic, the minimum number of trains for input capacities list = [4,1,6,1,2] would be 3 ([4,1,6],[1],[2]) while the true answer is 2 ([4,1][6,1,2])

3. This meant to find the minimum number of trains I need to find the min at each level and bubble that value up using a recursive approach. I choose to 
"""

x = [4, 1, 6, 1, 2]
x = [4, 1, 1, 1, 1]
# x = [1,3]
# x = [1,2,3,4,5]
# n = len(x)

def min_trains(x):
    n = len(x)
    level_min = [float('inf')] * (n + 1)
    level_min[0] = 0
    
    for j in range(1, n + 1):
        for i in range(j):
            cap_sum = sum(x[i:j])
            need = (j - i) ** 2  # we only do j - i as j starts at 1 while i starts at 0 
            if cap_sum >= need:
                level_min[j] = min(level_min[j], level_min[i] + 1)
    print(level_min)
    return level_min[n]


print(min_trains(x))


"""
1. Based on how the question is defined, the main idea is to find the minimum number of trains which can be formed for each index j such that  1 <= j <= n and it abides by the maintainence requirement.  
2. The maintainence requirement in the question is defined as such:
(sum of all carriages within the train) >= (j - i + 1)^2 {here i -> index of first carriage | j -> index of last carriage}
3. My intuition was to solve this problem using a dynamic programming approach. With most dynamic programming problems, the overall problem is usually divided into some subproblems, which add up to give the final solution. For this question, I iterate over all possible start points (i) for a possible train which might end at index 'j' and check for the associated maintainence condition by comparing the sum from index i to j and the need (j-i+1). At each endpoint j, my goal was to determine the minimum number of trains required to cover all carriages up to that point.
4. Here I setup a list "level_min" to keep track of minimum number of trains needed up to index j. This list has default values set to infinity for all indices aside from 0, for which the value is 0. 
5. When iterating through the different start points,this list is updated with the minumum of the current value at index j and 1 + level_min[i]. Here level_min[i] is the minimum number of trains needed up to index i. Adding 1 here is used to signify the formation of a new train starting from i and ending at j. 
6. Here the subproblem is finding the minimum number of trains needed at some index 1 <= j <= n, and is generalized when I consider all the start points for forming the train as well. 
7. This algorithm should have a time complexity of O(n^2), as it operates using a nested for loop of size n.
"""

