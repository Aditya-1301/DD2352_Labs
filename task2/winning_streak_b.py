import sys

n, p, k, cache = None, None, None, {}


def g(x):
    if x < k: 
        return 0.0
    if x == k:
        return p**k
    if x in cache:
        return cache[x]
    result = g(x-1) + (p**k)*(1-p)*(1-g(x-k-1))
    cache[x] = result
    return result


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    n = int(input())
    k = int(input())
    p = float(input())
    print(g(n))
