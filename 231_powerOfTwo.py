class Solution:
    def isPowerOfTwo(self, n):
        return n > 0 and n == 2**round(math.log(n,2))