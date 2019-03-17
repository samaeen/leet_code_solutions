class Solution:
    def outInt(self,s):
    	outInt=0
    	for c in s:
    		outInt=outInt*10+ord(c)-ord('0')
    	return outInt

    def addStrings(self, num1, num2):
    	print(str(self.outInt(num1)+self.outInt(num2)))


num1='9'
num2='99'
Solution().addStrings(num1,num2)