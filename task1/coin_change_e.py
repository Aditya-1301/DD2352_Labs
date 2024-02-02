import sys

def min_coin(c, s, g, p):
    return min(min(c, s), min(g, p))

def coin_change(n, a, b, c):
    dp = [0] * (n + 1)  # Initialize an array to store results for all amounts from 0 to n
    for i in range(1, n + 1):
        dp[i] = min_coin(dp[i - a] if i - a >= 0 else float('inf'),
                         dp[i - b] if i - b >= 0 else float('inf'),
                         dp[i - c] if i - c >= 0 else float('inf'),
                         float('inf')) + 1
    return dp[n]

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    n = int(input("Enter target amount: "))
    a = int(input("Enter value of coin a: "))
    b = int(input("Enter value of coin b: "))
    c = int(input("Enter value of coin c: "))
    print(coin_change(n, a, b, c))
