class Solution:
    def balancedStringSplit(self, s):
        l=0
        r=0
        count=0
        for i in s:
            if i=='L':
                l+=1
            if i=='R':
                r+=1
            if l==r:
                l=0
                r=0
                count=count+1
        return count