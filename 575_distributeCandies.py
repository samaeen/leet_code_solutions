class Solution:
    def distributeCandies(self, candies):
        return round(min(len(candies) / 2, len(set(candies))))