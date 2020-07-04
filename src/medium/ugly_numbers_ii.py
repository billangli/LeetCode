class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        idx2 = 0
        idx3 = 0
        idx5 = 0
        while len(ugly_numbers) < n:
            num2 = ugly_numbers[idx2] * 2
            num3 = ugly_numbers[idx3] * 3
            num5 = ugly_numbers[idx5] * 5
            if num2 <= num3 and num2 <= num5:
                if num2 > ugly_numbers[-1]:
                    ugly_numbers.append(num2)
                idx2 += 1
            elif num3 < num2 and num3 <= num5:
                if num3 > ugly_numbers[-1]:
                    ugly_numbers.append(num3)
                idx3 += 1                
            else:
                if num5 > ugly_numbers[-1]:
                    ugly_numbers.append(num5)
                idx5 += 1
        return ugly_numbers[-1]
