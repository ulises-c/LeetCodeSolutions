# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def minPartitions(self, n: str) -> int:
        # greatest = 0
        # for char in n:
        #     if((int)(char) > greatest):
        #         greatest = (int)(char)
        # return greatest
        return max(set(n))