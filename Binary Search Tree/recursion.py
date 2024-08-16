# Initialize the dp array with -1 for n+1 elements
def solve(n):
    dp = [-1] * (n + 1)

    def helper(n):
        # base case
        if n < 0:
            return 0
        if n == 0:
            return 1

        # Checking if already calculated
        if dp[n] != -1:
            return dp[n]

        # Storing the result and returning
        dp[n] = helper(n - 1) + helper(n - 3) + helper(n - 5)
        return dp[n]

    return helper(n)

# Example usage
print(solve(6))  # Output: 3
