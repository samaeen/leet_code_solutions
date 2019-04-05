class Solution:
    def shortestToChar(self, S, C):
    	outputArray=[]
    	arrayofchar=[]
    	for i,v in enumerate(S):
    		if v==C:
    			arrayofchar.append(i)
    	for i in range(len(S)):
    		outputArray.append(min([abs(j-i) for j in arrayofchar]))
    	print(outputArray)

S="loveleetcode"
C="e"
Solution().shortestToChar(S,C)