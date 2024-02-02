import sys

n, p, k, map = None, None, None, {}


def g(x):
    if x < k: 
        return 0.0
    if x == k:
        return p**k
    if x in map:
        return map[x]
    result = g(x-1) + (p**k)*(1-p)*(1-g(x-k-1))
    map[x] = result
    return result



if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    n = int(input())
    k = int(input())
    p = float(input())
    print(g(n))


# if (x, y) in map:
#     return map[(x, y)]
# result = p * f(x - 1, y - 1) + (1 - p) * f(x - 1, k)
# map[(x, y)] = result
# return result