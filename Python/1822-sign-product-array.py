# https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        arr_sum = 1
        for n in nums:
            arr_sum *= n
        if(arr_sum > 0):
            return 1
        elif(arr_sum < 0):
            return -1
        else:
            return 0