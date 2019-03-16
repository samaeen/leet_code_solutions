##time limit problem
class Solution:
    def singleNumber(self, nums):
    	blankArray=[]
    	for i in nums:
    		if i in blankArray:
    			blankArray.remove(i)
    		else:
    			blankArray.append(i)
    	print(blankArray[0])

nums=[2,2,4]
Solution().singleNumber(nums)
