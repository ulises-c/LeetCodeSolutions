# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_list = []
        current_sum = 0
        for i in range(len(nums)):
            new_sum = nums[i] + current_sum
            sum_list.append(new_sum)
            current_sum = new_sum
        return sum_list