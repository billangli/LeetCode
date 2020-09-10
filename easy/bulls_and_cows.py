class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_counts, guess_counts = defaultdict(int), defaultdict(int)
        bulls = 0
        
        for i in range(len(secret)):
            if secret[i] == guess[i]: bulls += 1
            secret_counts[secret[i]] += 1
            guess_counts[guess[i]] += 1
            
        total_matches = 0
        for i in range(10):
            total_matches += min(secret_counts[str(i)], guess_counts[str(i)])
        cows = total_matches - bulls
        
        return "{}A{}B".format(bulls, cows)
