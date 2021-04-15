# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        set_j = set(jewels)
        count = 0
        for j in set_j:
            for s in stones:
                if(j in s):
                    count += 1
        return count