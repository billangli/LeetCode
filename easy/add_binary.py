class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = "0"
        result = ""
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        elif len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
            
        for i in range(len(a) - 1, -1, -1):
            if carry == "0":
                if a[i] == "0" and b[i] == "0":
                    result = "0" + result
                elif a[i] == "1" and b[i] == "1":
                    result = "0" + result
                    carry = "1"
                else:
                    result = "1" + result
            else:
                if a[i] == "0" and b[i] == "0":
                    result = "1" + result
                    carry = "0"
                elif a[i] == "1" and b[i] == "1":
                    result = "1" + result
                else:
                    result = "0" + result
                    
        if carry == "1":
            result = "1" + result
        return result
                
