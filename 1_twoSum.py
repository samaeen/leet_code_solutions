class Solution(object):
    def twoSum(self,nums,target):
        hash_table=dict()
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return (nums.index(hash_table[nums[i]]),i)		
            else:
                hash_table[target-nums[i]]=nums[i]