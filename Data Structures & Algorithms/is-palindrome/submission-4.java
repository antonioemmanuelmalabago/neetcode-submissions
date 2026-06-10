class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            while (!isAlphaNum(s.charAt(left)) && left < right) {
                left++;
            }
            while (!isAlphaNum(s.charAt(right)) && right > left) {
                right--;
            }
            if (s.toLowerCase().charAt(left) != s.toLowerCase().charAt(right)) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }

    public boolean isAlphaNum(char c) {
        return (c >= 'a' && c <= 'z') || 
               (c >= 'A' && c <= 'Z') || 
               (c >= '0' && c <= '9');
    }
}
