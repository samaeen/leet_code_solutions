class Solution(object):
    def hammingWeight(self, n):
        count=0
        for i in str(bin(n)): #you cannot start with 0 in python...that's whyconvert to bin
            if i=='1':
                count+=1
            else:
                count=count
        return count