import collections
class Solution:
    def uniqueOccurrences(self, arr):
    	counts = list(collections.Counter(arr).values())
    	return len(counts) == len(set(counts))
arr=[1,2]
Solution().uniqueOccurrences(arr)