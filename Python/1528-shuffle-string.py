# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        hash_map = {}
        # sorted_list = []
        new_str = ""
        for i in range(len(s)):
            # hash_map.set_val(indicies[i], s[i])
            hash_map[indices[i]] = s[i]
        for i in range(len(hash_map)):
            # sorted_list.append(hash_map.get(i))
            new_str += hash_map.get(i)
        # print(hash_map)
        return(new_str)