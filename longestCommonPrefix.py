class Solution:
    def longestCommonPrefix(self, strs):
    	for i in range(len(strs)):
    		print(strs[i][0])


a=["flower","flow","flight"]
#print(a[0][2])
#print(len(a))
print(Solution().longestCommonPrefix(a))