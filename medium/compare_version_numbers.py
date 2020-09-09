class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1, nums2 = version1.split('.'), version2.split('.')
        counter = 0
        while counter < max(len(nums1), len(nums2)):
            n1 = int(nums1[counter]) if counter < len(nums1) else 0
            n2 = int(nums2[counter]) if counter < len(nums2) else 0
            if n1 < n2: return -1
            if n1 > n2: return 1
            counter += 1
        return 0
