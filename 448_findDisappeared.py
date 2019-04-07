class Solution:
    def findDisappearedNumbers(self, nums):
        return list(set(range(1, len(nums)+1)) - set(nums))


#eta keno holo na?
class Solution:
    def findDisappearedNumbers(self, nums):
        return [i for i in range(1,max(nums)+1) if i not in nums]