class Solution:
    def containsDuplicate(self, nums):
        a=len(set(nums))
        b=len(nums)
        if a==b:
            return False
        else:
            return True
        