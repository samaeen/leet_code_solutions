'''
eida hoilo na keno bujhlam na :/
class Solution(object):
    def flipAndInvertImage(self, A):
        r= []
        for i in A:
            r.append(list(reversed(i)))
            
        outputArray = []
        for j in r:
            outputArray.append(map(lambda x: abs(x-1),j))
        
        return outputArray
'''

class Solution(object):
    def flipAndInvertImage(self, A):
        return [[abs(i-1) for i in list(reversed(row))] for row in A]
A=[[1,1,0],[1,0,1],[0,0,0]]
Solution().flipAndInvertImage(A)
