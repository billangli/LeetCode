class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) < 1:
            return 0
        if s == "0":
            return 0
        if s[-2:] == "00":
            return 0
        
        dp = [0] * (len(s) + 2)
        dp[len(s)] = 1
        dp[len(s) + 1] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] != "0":
                dp[i] = dp[i + 1]
            if i <= len(s) - 2 and 10 <= int(s[i:i + 2]) <= 26:
                dp[i] += dp[i + 2]
        return dp[0]


if __name__ == "__main__":
    print(Solution().numDecodings("10"))
    print(Solution().numDecodings("12"))
    print(Solution().numDecodings("226"))
    print(Solution().numDecodings("32"))
    print(Solution().numDecodings("3"))