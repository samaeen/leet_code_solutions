class Solution:
    def findDuplicates(self, nums):
        output=[]
        lookin=set()
        for i in nums:
            if i not in lookin:
                lookin.add(i)
            else:
                output.append(i)
        return output