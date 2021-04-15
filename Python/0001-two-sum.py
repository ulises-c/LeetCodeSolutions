# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos1 = 'empty'
        pos2 = 'empty'
        complement = 'empty'
        for i in range(len(nums)):
            complement = target - nums[i]
            extra_complement = target - complement
            if(complement in nums and (extra_complement != complement or nums.count(complement) > 1)):
                pos1 = i
                break
        for i in range(len(nums)):
            if(nums[i]==complement and i != pos1):
                pos2 = i
                break
        return [pos1, pos2]