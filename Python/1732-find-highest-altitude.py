class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_alt = 0
        highest_alt = 0
        for change in gain:
            current_alt += change
            if(current_alt > highest_alt):
                highest_alt = current_alt
        return highest_alt