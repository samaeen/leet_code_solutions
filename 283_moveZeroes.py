class Solution:
    def moveZeroes(self, nums):
        a=0
        while 0 in nums:
            nums.remove(0)
            a+=1
        for i in range(a):
            nums.append(0)