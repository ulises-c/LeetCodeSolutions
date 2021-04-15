# https://leetcode.com/problems/find-common-characters/submissions/

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        storing_array = []
        new_array = []
        for k in range (0, len(A)):
            for j in range (0, len(A[k])):
                storing_array.append(A[k][j])
        print(storing_array)
        
        for k in range(0, len(storing_array)):
            print(storing_array.count(storing_array[k]))
            if(storing_array.count(storing_array[k]) >= len(A) and storing_array[k] not in new_array):
                x = storing_array.count(storing_array[k]) // len(A)
                for j in range(0, x):
                    new_array.append(storing_array[k])
        
        return(new_array)
