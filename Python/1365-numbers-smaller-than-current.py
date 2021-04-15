# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        smaller_list = []
        for num in nums:
            amt_smaller = 0
            for n in nums:
                if(num > n):
                    amt_smaller += 1
            smaller_list.append(amt_smaller)
        return smaller_list