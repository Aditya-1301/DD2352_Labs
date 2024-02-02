import sys


def min_coin(c, s, g, p):
    return min(min(c, s), min(g, p))


def coin_change(n, a, b, c):
    if n < 0: return float("inf")
    if n == 0: return 0
    return min_coin(n, 1 + coin_change(n - a, a, b, c), 1 + coin_change(n - b, a, b, c),
                    1 + coin_change(n - c, a, b, c))


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    print(coin_change(n, a, b, c))
