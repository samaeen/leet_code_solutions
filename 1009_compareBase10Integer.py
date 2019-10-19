class Solution:
	def bitwiseComplement(self, N):
		compNum = bin(N)[2:]
		compNum = compNum.replace('0', 'a')		
		compNum = compNum.replace('1', 'b')
		compNum = compNum.replace('b', '0')
		compNum = compNum.replace('a', '1')
		print(int(compNum,2))
		


Solution().bitwiseComplement(7)