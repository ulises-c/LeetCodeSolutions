# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        midpoint = len(nums)//2
        new_list = []
        for i in range(len(nums)//2):
            new_list.append(nums[i])
            new_list.append(nums[i + midpoint])
            
        return new_list