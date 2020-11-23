class Solution:
    def generateParenthesis(self, n: int):
        dp = [[] for i in range(n+1)]
        dp[0].append("")
        for k in range(1, n+1):
            for p in range(k):
                for left in dp[p]:
                    for right in dp[k-1-p]:
                        dp[k].append("({}){}".format(left, right))
        return dp[n]
