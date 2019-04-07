class Solution:
    def firstMissingPositive(self, nums):
        output=[]
        lookin=set()
        for i in nums:
            if i not in lookin:
                lookin.add(i)
            else:
                output.append(i)
        output=[i for i in nums if i>0]
        return min(output)