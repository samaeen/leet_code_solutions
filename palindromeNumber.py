class Solution:
    def isPalindrome(self, x):
        y=str(x)
        r=y[::-1]
        if r==y:
            return True
        else:
            return False