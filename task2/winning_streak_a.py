import sys

n, p, k, map = None, None, None, {}

def f(x, y):
    if y == 0: 
        return 1.0
    if x == 0 and y > 0:
        return 0.0
    if f"{x-1}{k}" not in map:
        map[f"{x-1}{k}"] = f(x-1, k)
    if f"{x-1}{y-1}" not in map:
        map[f"{x-1}{y-1}"] = f(x-1, y-1)
    if x >= 1 and y >= 1:
        return p * map[f"{x-1}{y-1}"] + (1 - p) * map[f"{x-1}{k}"]


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    n = int(input())
    k = int(input())
    p = float(input())
    print(f(n,k))
    