class Solution:
    def numJewelsInStones(self, J, S):
        J=[i for i in J]
        count=0
        for i in S:
            if i in J:
                count=count+1
            else:
                count=count
        return count