# https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        matches = 0
        for i in items:
            if(ruleKey == "type" and ruleValue == i[0]):
                matches += 1
            if(ruleKey == "color" and ruleValue == i[1]):
                matches += 1
            if(ruleKey == "name" and ruleValue == i[2]):
                matches += 1
        return matches