import sys

n, p, k, cache = None, None, None, {}


def f(x, y):
    if y == 0: 
        return 1.0
    if x == 0 and y > 0:
        return 0.0
    if (x, y) in cache:
        return cache[(x, y)]
    result = p * f(x - 1, y - 1) + (1 - p) * f(x - 1, k)
    cache[(x, y)] = result
    return result


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    n = int(input())
    k = int(input())
    p = float(input())
    print(f(n, k))
    