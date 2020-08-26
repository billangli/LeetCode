class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        counter3, counter5 = 0, 0
        result = []
        
        for i in range(1, n + 1):
            num = ''
            counter3 += 1
            counter5 += 1
            
            if counter3 == 3:
                num += 'Fizz'
                counter3 = 0
            if counter5 == 5:
                num += 'Buzz'
                counter5 = 0
                
            num = '{}'.format(i) if num == '' else num
            result.append(num)
            
        return result
