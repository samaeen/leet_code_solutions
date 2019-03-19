#this is the easiest
class Solution:
    def thirdMax(self, nums):
    	nums=sorted(set(nums))
    	if len(nums)<3:
    		return max(nums)
    	else:
    		return nums[-3]

nums=[1,2,2,3]
Solution().thirdMax(nums)