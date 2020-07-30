class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
                
        diff = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
        dp, dp_max = [0] * (len(prices) + 1), [0] * (len(prices) + 1)
            
        for i in range(len(prices) - 1):
            dp[i] = diff[i] + max(dp_max[i - 3], dp[i - 1])
            dp_max[i] = max(dp_max[i - 1], dp[i])
        return dp_max[-3]
