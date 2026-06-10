// Case-insensitive
// Ignores non-alphanum

class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        // Declare left and right pointers
        let left = 0;
        let right = s.length - 1;

        // Continue loop while pointers are valid
        while (left < right) {
            // Move left pointer until valid character
            while (!this.isAlphaNum(s[left]) && left < right) {
                left++;
            }
            // Move right pointer until valid character
            while (!this.isAlphaNum(s[right]) && right > left) {
                right--;
            }
            // Check if left and right characters are same
            if (s[left].toLowerCase() !== s[right].toLowerCase()) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }

    isAlphaNum(c) {
        return (c >= 'a' && c <= 'z') || 
               (c >= 'A' && c <= 'Z') || 
               (c >= '0' && c <= '9');
    }
}
