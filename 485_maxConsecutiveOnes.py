class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count=0
        position=0
        for i in nums:
            if i!=0:
                count+=1
            else:
                position=max(count,position)
                count=0
        return max(count,position)