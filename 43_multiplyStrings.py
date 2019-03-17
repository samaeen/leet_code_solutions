class Solution:
    def outInt(self,s):
    	outInt=0
    	for c in s:
    		outInt=outInt*10+ord(c)-ord('0')
    	return outInt

    def multiply(self, num1, num2):
    	print(str(self.outInt(num1)*self.outInt(num2)))


num1='123'
num2='456'
Solution().multiply(num1,num2)