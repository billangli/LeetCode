class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        days = set(days)
        dp = [0] * (last_day + 30)
        
        for d in range(1, last_day + 1):
            if d in days:
                dp[d] = min(
                    dp[d - 1] + costs[0],
                    dp[d - 7] + costs[1],
                    dp[d - 30] + costs[2]
                )
            else:
                dp[d] = dp[d - 1]
            
        return dp[last_day]
