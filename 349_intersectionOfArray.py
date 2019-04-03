class Solution:
    def intersection(self, nums1, nums2):
        blankArray=[]
        for i in nums2:
        	if i in nums1:
        		blankArray.append(i)
        	else:
        		pass
        print(list(set(blankArray)))


nums1=[4,9,5]
nums2=[9,4,9,8,4]
Solution().intersection(nums1,nums2)