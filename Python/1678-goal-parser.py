# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        str_list = []
        new_str = ""
        for s in command:
            str_list.append(s)
        for i in range(len(str_list)):
            if(str_list[i] == "G"):
                new_str += "G"
            elif(str_list[i] == ")" and str_list[i-1] == "("):
                new_str += "o"
            elif(str_list[i] == ")" and str_list[i-1] == "l" and str_list[i-2] == "a" and str_list[i-3] == "("):
                new_str += "al"
        return new_str