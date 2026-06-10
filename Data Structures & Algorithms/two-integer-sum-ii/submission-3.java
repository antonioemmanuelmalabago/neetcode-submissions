// Increasing order
// 1-indexed (starting from 1)
// Both elements must be unique

class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // Initialized pointers
        int left = 0;
        int right = numbers.length - 1;

        // Iterate until pointers are valid
        while (left < right) {
            // Compute for sum
            int sum = numbers[left] + numbers[right];
            // Check if sum is greater than target
            if (sum > target) {
                right--;
            // Check if sum is less than target
            } else if (sum < target) {
                left++;
            // If sum is equal to target, return their 1-indexed
            } else {
                return new int[]{left + 1, right + 1};
            }
        }

        return new int[0];
    }
}
