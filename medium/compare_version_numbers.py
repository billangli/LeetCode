class Solution:
    def index(self, string: str, substring: str) -> int:
        if substring not in string:
            return len(string)
        return string.index(substring)
    
    def compareVersion(self, version1: str, version2: str) -> int:
        dot1 = self.index(version1, '.')
        dot2 = self.index(version2, '.')
        num1 = int(version1[:dot1])
        num2 = int(version2[:dot2])
        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
        elif dot1 == len(version1) and dot2 == len(version2):
            return 0
        else:
            next_version1 = version1[dot1+1:] if dot1 != len(version1) else '0'
            next_version2 = version2[dot2+1:] if dot2 != len(version2) else '0'
            return self.compareVersion(next_version1, next_version2)
