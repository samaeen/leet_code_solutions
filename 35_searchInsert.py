class Solution(object):
    def searchInsert(self,nums,target):
        blankArray=[]
        for i in nums:
            if i==target:
                print(nums.index(target))
            else:
                blankArray.append(abs(target-i))
        if blankArray.index(min(blankArray))==0:
            print('0')
        else:
            print(blankArray.index(min(blankArray))+1)
nums=[3,5,6,8]
target=1
Solution().searchInsert(nums,target)

##But wait for it...I just remembered.....Easy solution
class Solution(object):
    def searchInsertBest(self,nums,target):
        nums.append(target)
        return sorted(nums).index(target)