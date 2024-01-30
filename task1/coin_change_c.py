"""
1(b) Memoization optimization
"""

import sys

cache = {}


def min_coin(c, s, g, p):
    return min(min(c, s), min(g, p))


def coin_change(n, a, b, c):
    if n < 0: return float("inf")
    if n == 0: return 0
    if n - a not in cache:
        cache[n - a] = coin_change(n - a, a, b, c)
    if n - b not in cache:
        cache[n - b] = coin_change(n - b, a, b, c)
    if n - c not in cache:
        cache[n - c] = coin_change(n - c, a, b, c)
    return min_coin(n, 1 + cache[n - a], 1 + cache[n - b],
                    1 + cache[n - c])


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    print(coin_change(50000, 5, 6, 7))
