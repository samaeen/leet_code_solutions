class Solution:
    def removeDuplicates(self, nums):
    	for i in range(len(nums)-1,0,-1):
    		if nums[i] == nums[i-1]:
    			del nums[i]
    	print(len(nums))

#class Solution:
#    def removeDuplicates(self, nums):
#    	blankArray={}
#    	print(len(blankArray.fromkeys(nums)))

nums = [1,1,2]
Solution().removeDuplicates(nums)
