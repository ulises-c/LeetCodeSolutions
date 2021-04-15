# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in range(0, len(nums), 2):
            # print("{} {}".format(nums[i], nums[i+1]))
            for j in range(nums[i]):
                new_list.append(nums[i+1])
        return new_list