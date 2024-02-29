# for (i,j) in sets:
#     ij.append((i//(i-j), (i,j)))

# print(ij)

# ij1 = sorted(ij, reverse=True)

# print(ij1)

# ij2 = [(i,j) for (_, (i,j)) in ij1]

# print(ij2) #, reverse=True))

# sets = [(4,2), (9,5), (3,2)]
# total = 0
# CDs = 0
# n = 6
# m = 3
# C = 99

# ij = [(x,(i-j)*C, i, j) for x,(i,j) in enumerate(sets)]

# coupons = sorted(ij)
# print(coupons)

# costs = []
# bought = []
# C = 99

# for (i,j) in ij2:
#     bought.append(i)
#     costs.append((i-j)*C)

# print(bought,costs)

"""
My understanding so far:
1. We need to go through the coupons in such a way that we get the best value for each coupon, i.e. by sorting the list of coupons by difference of the bi and fi values for each of the pairs
2. This needs to be done alongside the requirements 
    i.  total number of CDs bought >= n
    ii. total cost needs to be minimized
3. The algorithm needs to be formulated in some recursive way as to find the overall min cost we have to find all possible coupon combination costs
4. Probably a Dynamic Programming problem

OR 

5. Another Possible approach could be to treat all of the coupons as nodes in a graph and the way to find all the cost combinations for the coupons. 
Thus, we would have the cases for:
    i.   No Coupons
    ii.  Just one of the coupons
    iii. One of the combinations found using paths in the coupon graph


Rethinking about this problem again I think the problem can be constructed in the following way:

1. We can split the problem into 2 different parts: 
    i.  the first would be to consider the cases from 0 coupons to using at most one coupon from the m at our disposal
    ii. the second part would be to get the minimum of all the other combinations which can be taken for the m coupons
"""

# total = 0
# n = 6
# m = 3
# C = 99
# pairs = [(4,2), (9,5), (3,2)]

# def function():


# al = [[y for j,y in enumerate(ij) if j != i] for i in range(len(ij)) ]

# print(al)

# ------------------------------------------------------------------------------------------------------------------

# coupons = [(4, 2), (9, 5), (3,2)]


def min_cost1(c_list, total_cds, cost, used): # Innefficient 
    # if not c_list:  # base case: no more CDs left
    #     if total_cds >= n:
    #         return 0
    #     else:
    #         return (n - total_cds) * C  # cost of buying remaining CDs

    if len(c_list) == 1:
        # print(c_list, total_cds, cost)
        (i, j) = c_list[0]
        if total_cds + i >= n:
            # print(total_cds, total_cds + i)
            return min((i - j) * C, n*C) # cost of current CD
        else:
            # print(total_cds, total_cds + i)
            return (i - j) * C + (n - total_cds - i) * C  # cost of current CD + cost of buying remaining CDs

    local_min = float("inf")
    for z, (x, y) in enumerate(c_list):
        if (x, y) not in used:
            used_copy = used[:]
            used_copy.append((x, y))
            coupons_left = c_list[:z] + c_list[z+1:]
            if total_cds + x >= n:
                # print(local_min, total_cds, total_cds + x, cost)
                local_min = min(local_min, (x - y) * C + cost)
                all_local_minimums.add((local_min, total_cds + x))
            elif (x, y) not in coupons_left:
                # print(local_min, total_cds)
                # print(f"parameters for next recursion: {(c_list[1:], total_cds + x, cost + (x - y) * C)}")
                local_min = min(local_min, min_cost1(coupons_left, total_cds + x, cost + (x - y) * C, used_copy))
                all_local_minimums.add((local_min, total_cds + x))
    print(used, total_cds, cost)
    return local_min


# ----------------------------------------------------------------------------------------------------------------


# coupons = [(100, 93)]; n = 6
# coupons = [(2, 1), (9, 5), (4, 2),  (3, 2)]; n = 10
# coupons = [(9, 5), (11, 8), (7, 6), (6, 5)]; n = 20
# ----------------------------------------------------------------------------------------------------------------
coupons = [(4, 2), (9, 5), (3, 2)]; n = 6
C = 99
m = len(coupons)
all_local_minimums = set()
cache = {}


def min_cost(c_list, total_cds, cost, used): # Memoized
    if len(c_list) == 1:
        (i, j) = c_list[0]
        if total_cds + i >= n:
            return min((i - j) * C, n*C) # cost of current CD
        else:
            return (i - j) * C + (n - total_cds - i) * C  # cost of current CD + cost of buying remaining CDs
    
    if tuple(used) in cache: # Cache Hit
        return cache[tuple(used)]

    local_min = float("inf")
    for z, (x, y) in enumerate(c_list):
        print((x,y), used)
        if (x, y) not in used:
            used_copy = used[:] # I had to create copy as sometimes there were reused coupons when recursing
            used_copy.append((x, y))
            coupons_left = c_list[:z] + c_list[z+1:]
            if total_cds + x >= n: # or total_cds == n - y
                local_min = min(local_min, (x - y) * C + cost) 
                all_local_minimums.add((local_min, total_cds + x))
            # elif (x, y) not in coupons_left:
            else:
                local_min = min(local_min, min_cost(coupons_left, total_cds + x, cost + (x - y) * C, used_copy))
                all_local_minimums.add((local_min, total_cds + x))
            cache[tuple(used)] = local_min  # Store/Update in Cache
    print(used, total_cds, cost)
    return local_min


# print(f"Answer: {min_cost1(coupons, 0, 0, [])}")
# print([(a, b) for (a, b) in all_local_minimums if b >= n])

# all_local_minimums = set()
print(f"Answer: {min_cost(coupons, 0, 0, [])}\n")
print(f"All local minimums: {[(a, b) for (a, b) in all_local_minimums if b >= n]}\n")
print(f"Cache: {cache}\nSize of cache: {len(cache)}\n")

# ---------------------------------------------------------------------------













    
