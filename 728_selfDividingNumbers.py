class Solution(object):
    def selfDividingNumbers(self, left, right):
        outputArray = []
        for i in range(left, right + 1):
            for j in str(i):
                if j == '0' or 0 !=i % int(j):
                    break
            else:
                outputArray.append(i)
        
        return outputArray  