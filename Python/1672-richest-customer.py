# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for i in range(len(accounts)):
            current_wealth = 0
            for j in range(len(accounts[i])):
                current_wealth += accounts[i][j]
                if(current_wealth > richest):
                    richest = current_wealth
        return richest