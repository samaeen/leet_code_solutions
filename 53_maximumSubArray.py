class Solution:
    def maxSubArray(self, nums):
    	nums=sorted(set(nums))
    	nums=nums[::-1]
    	nums=nums[:4]
    	s=sum(nums)
    	print(nums)

nums=[-2,1,-3,4,-1,2,1,-5,4]
Solution().maxSubArray(nums)