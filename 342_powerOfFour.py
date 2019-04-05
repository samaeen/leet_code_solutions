class Solution:
    def isPowerOfFour(self, num):
        return num > 0 and num == 4**round(math.log(num,4))