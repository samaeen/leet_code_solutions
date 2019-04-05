#soja bangla
class Solution:
    def isPowerOfThree(self, n):
        if n>0 and n == 3**round(math.log(n,3)):
            return True
        else:
            return False
#kothin bangla
class Solution:
    def isPowerOfThree(self, n):
        return n > 0 and n == 3**round(math.log(n,3))