package Java;

class Solution_1480 {
// class Solution {
    public int[] runningSum(int[] nums) {
        int[] sum_list = new int[nums.length];
        int current_sum = 0;
        for(int i=0; i < nums.length; i++){
            int new_sum = nums[i] + current_sum;
            sum_list[i] = new_sum;
            current_sum = new_sum;
        }
        return sum_list;
    }
}
