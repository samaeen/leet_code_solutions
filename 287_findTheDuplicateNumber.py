class Solution:
    def findDuplicate(self, nums):
    	blankArray={}
    	for i in nums:
    		if i in blankArray:
    			print(i)
    			print(blankArray)
    		blankArray[i]=""


nums=[1,3,4,2,2]
Solution().findDuplicate(nums)