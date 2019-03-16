class Solution:
    def missingNumber(self, nums):
        a=sum(range(len(nums)+1))-sum(nums)
        print(a)

nums=[9,6,4,2,3,5,7,0,1]
Solution().missingNumber(nums)