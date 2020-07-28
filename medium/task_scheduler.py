class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for t in tasks:
            freq[t] += 1
            
        most_freq = 0
        num_most_freq = 0
        for key in freq.keys():
            if freq[key] > most_freq:
                most_freq = freq[key]
                num_most_freq = 1
            elif freq[key] == most_freq:
                num_most_freq += 1
        
        return max(len(tasks), (most_freq - 1) * (n + 1) + num_most_freq)
