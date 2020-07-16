class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif x == 0:
            return 0            
        
        def posPow(x: float, n: int) -> float:
            """Calculates x^n where n > 0"""
            result = 1
            power = x
            mask = 1
            while n >= mask:
                if n & mask:
                    result *= power
                power *= power
                mask <<= 1
            return result
        
        if n < 0:
            return 1 / posPow(x, -n)
        else:
            return posPow(x, n)
