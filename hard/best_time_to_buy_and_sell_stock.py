class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def max_subsequence_sum(array: List[int], start: int, end: int) -> int:
            """
            Given array[start:end] return a tuple that contains the following values
                seq_start: start index of the max sequence
                seq_end: end index of the max sequence
                max_sum: the sum of the max sequence, i.e. sum(array[seq_start:seq_end])
            Note that max_sum >= 0
            """
            max_sum, curr, seq_start, seq_end, temp_start = 0, 0, start, start, start
            for i in range(start, end):
                if curr + array[i] > 0:
                    curr += array[i]
                    if curr > max_sum:
                        max_sum = curr
                        seq_start = temp_start
                        seq_end = i + 1
                else:
                    curr = 0
                    temp_start = i + 1
            return (seq_start, seq_end, max_sum)
        
        def min_subsequence_sum(array: List[int], start: int, end: int) -> int:
            min_sum, curr, seq_start, seq_end, temp_start = 0, 0, start, start, start
            for i in range(start, end):
                if curr + array[i] < 0:
                    curr += array[i]
                    if curr < min_sum:
                        min_sum = curr
                        seq_start = temp_start
                        seq_end = i + 1
                else:
                    curr = 0
                    temp_start = i + 1
            return (seq_start, seq_end, min_sum)
                    
            
        if len(prices) < 2: return 0
        
        # Get diff array
        diffs = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
        max_value = 0
        inner_max, outer_max = [0, 0], [0, 0]
        
        # Find max subsequence
        max_start, max_end, max_value = max_subsequence_sum(diffs, 0, len(diffs))
        
        # Find min subsequence in max subsequence
        min_start, min_end, _ = min_subsequence_sum(diffs, max_start, max_end)
        
        # Find two max subsequences in max subsequence
        _, _, inner_max[0] = max_subsequence_sum(diffs, max_start, min_start)
        _, _, inner_max[1] = max_subsequence_sum(diffs, min_end, max_end)
        
        # Find max subsequence of the two ends
        _, _, outer_max[0] = max_subsequence_sum(diffs, 0, max_start)
        _, _, outer_max[1] = max_subsequence_sum(diffs, max_end, len(diffs))
        
        other_maxes = sorted(inner_max + outer_max)
        return max(max_value + max(outer_max), other_maxes[-1] + other_maxes[-2])
