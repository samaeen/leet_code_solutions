class Solution:
    def titleToNumber(self, s):
        sum = 0
        for i,t in enumerate(s[::-1]):
            sum = sum + (ord(t)-64)*(26**i)
        return sum