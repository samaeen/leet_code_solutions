class Solution:
    def judgeCircle(self, moves):
    	pos=[0,0]
    	for i in moves:
    		if i=='U':
    			pos[0]+=1
    		if i=='D':
    			pos[0]-=1
    		if i=='L':
    			pos[1]-=1
    		if i=='R':
    			pos[1]+=1
    	if pos==[0,0]:
    		return True
    	else:
    		return False

moves="RLUURDDDLU"
Solution().judgeCircle(moves)