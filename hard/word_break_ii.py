class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = defaultdict(list)
        for w in wordDict:
            words[w[0]].append(w)
            
        dp = defaultdict(list)
        
        def helper(index):
            if index not in dp:
                for w in words[s[index]]:
                    if len(w) <= len(s) - index and w == s[index:index+len(w)]:
                        if len(w) == len(s) - index:
                            dp[index].append(w)
                        else:
                            for suffix in helper(index + len(w)):
                                dp[index].append(w + " " + suffix)
            return dp[index]
        
        return helper(0)
