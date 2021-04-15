# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_str = (str)(n)
        n_list = []
        for char in n_str:
            n_list.append((int)(char))
        n_sum = 0
        n_prod = 1
        for entry in n_list:
            n_sum += entry
            n_prod *= entry
        return n_prod - n_sum