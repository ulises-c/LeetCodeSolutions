# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        initial_greatest = candies[0]
        greater_candies = []
        for i in range(len(candies)):
            if(candies[i] > initial_greatest):
                initial_greatest = candies[i]
        for i in range(len(candies)):
            if(candies[i] + extraCandies >= initial_greatest):
                greater_candies.append(True)
            else:
                greater_candies.append(False)
        return greater_candies