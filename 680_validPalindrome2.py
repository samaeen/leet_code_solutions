class Solution:
    def isPalindrome(self, x):
        y=x
        r=y[::-1]
        if r==y:
            print("palindrome")
        else:
            for i in r:
