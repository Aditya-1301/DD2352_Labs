# x = [4, 1, 6, 1, 2]


# def check(trains):
#     n = len(trains)
#     local_mins = [float("inf")] * (n+1)
#     local_mins[0] = 0
#     for j in range(1,n+1):
#         for i in range(j):
#             cap = sum(trains[i:j])
#             need = (j-i)**2
#             if cap >= need:
#                 print(i, j, trains[i:j], cap, need, local_mins[j], local_mins[i] + 1)
#                 local_mins[j] = min(local_mins[j], 1 + local_mins[i])
#                 print(i, j, trains[i:j], cap, need, local_mins[j], local_mins[i] + 1)
#     print(local_mins)
#     return local_mins[n]

# print(check(x))

# coupons = [(4, 2), (9, 5), (3, 2)]; n = 6 
# # Some other possible test cases:
# # coupons = [(2, 1), (9, 5), (4, 2),  (3, 2)]; n = 10
# # coupons = [(9, 5), (11, 8), (7, 6), (6, 5)]; n = 20
# C = 99
# m = len(coupons)
# all_local_minimums = set()
# cache = {}


# def min_cost(c_list, total_cds, cost, used):
#     if len(c_list) == 1:
#         (i, j) = c_list[0]
#         if total_cds + i >= n:
#             return min((i - j) * C, n*C) # cost of current CD
#         else:
#             return (i - j) * C + (n - total_cds - i) * C  # cost of current CD + cost of buying remaining CDs
    
#     if tuple(used) in cache:
#         return cache[tuple(used)]

#     local_min = float("inf")
#     for z, (x, y) in enumerate(c_list):
#         if (x, y) not in used:
#             used_copy = used[:]
#             used_copy.append((x, y))
#             coupons_left = c_list[:z] + c_list[z+1:]
#             if total_cds + x >= n:
#                 local_min = min(local_min, (x - y) * C + cost)
#                 all_local_minimums.add((local_min, total_cds + x))
#             elif (x, y) not in coupons_left:
#                 local_min = min(local_min, min_cost(coupons_left, total_cds + x, cost + (x - y) * C, used_copy))
#                 all_local_minimums.add((local_min, total_cds + x))
#             cache[tuple(used)] = local_min
#     return local_min


# print(f"Answer: {min_cost(coupons, 0, 0, [])}")
# print([(a, b) for (a, b) in all_local_minimums if b >= n])



# def min_cost(c_list, remaining_cds, used_coupons, cache):
#     if remaining_cds <= 0:
#         return 0
#     if tuple(used_coupons) in cache:
#         return cache[tuple(used_coupons)]

#     min_cost_val = float('inf')  # Renamed to min_cost_val to avoid conflict
#     for i, coupon in enumerate(c_list):
#         new_remaining_cds = remaining_cds - coupon[0]
#         if new_remaining_cds >= 0 and used_coupons[i] < coupon[0]:
#             new_used_coupons = used_coupons[:]
#             new_used_coupons[i] += coupon[1]
#             cost = min_cost(c_list, new_remaining_cds, new_used_coupons, cache)
#             min_cost_val = min(min_cost_val, cost + (coupon[0] - new_remaining_cds) * C)
#     cache[tuple(used_coupons)] = min_cost_val
#     return min_cost_val

# # Example usage:
# C = 99
# n = 6
# # coupons = [(9, 5), (4,2), (3,2)]
# coupons = [(100,95)]
# used_coupons = [0] * len(coupons)
# cache = {}
# print(f"Answer: {min_cost(coupons, n, used_coupons, cache)}")


# coupons = [(4, 2), (9, 5), (3, 2)]
# C = 99
# n = 6
# m = len(coupons)

# """
# What we want to achive by adding a cache to this, is to improve the overall time complexity of the solution and make this solution easier to understand
# -> The intution for the cache and the associated value which is stored is the mapping between the current combination of used coupons and the associated minimum cost from the coupons.
# -> This mapping makes the most sense, and its easy to reuse values from the cache in a way where if for the current combination of coupons we have used some of the same coupons as in a previous iteration then we can get the cost from the cached value rather than recomputing the full value
# -> 
# """


# def min_cost(c_list, total_cds, cost, used):
#     if len(c_list) == 1:
#         (i, j) = c_list[0]
#         if total_cds + i >= n:
#             return (i - j) * C
#         else:
#             return (i - j) * C + (n - total_cds - i) * C 

#     local_min = float("inf")
#     for z, (x, y) in enumerate(c_list):
#         if (x, y) not in used:
#             used_copy = used[:]
#             used_copy.append((x, y))
#             coupons_left = c_list[:z] + c_list[z+1:]
#             if total_cds + x >= n:
#                 local_min = min(local_min, (x - y) * C + cost)
#                 all_local_minimums.add((local_min, total_cds + x))
#             elif (x, y) not in coupons_left:
#                 local_min = min(local_min, min_cost(coupons_left, total_cds + x, cost + (x - y) * C, used_copy))
#                 all_local_minimums.add((local_min, total_cds + x))
#     return local_min


# print(f"Answer: {min_cost(coupons, 0, 0, [])}")
# print([(a, b) for (a, b) in all_local_minimums if b >= n])




    