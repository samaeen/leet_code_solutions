from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        ct1, ct2, blankArray = Counter(nums1), Counter(nums2), []
        for element in ct1:
            if element in ct2:
                minimum = min(ct1[element], ct2[element])
                for j in range(minimum):
                    blankArray.append(element)
        return blankArray


nums1=[4,9,5]
nums2=[9,4,9,8,4]
Solution().intersect(nums1,nums2)