// Open bracket closed by same close bracket
// Closed in correct order: ()[], ([])

class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        // Initialized an empty stack
        let openBrackets = [];
        // Create dictionary for brackets
        let closeToOpen = {')':'(', '}':'{', ']':'['};

        // Iterate through each character in the string
        for (let i = 0; i < s.length; i++) {
            // Check if current character is not key in dictionary
            if (!(s[i] in closeToOpen)) {
                // This means the character is (maybe) an opening bracket
                openBrackets.push(s[i]);
            } else {
                // Check if stack is not empty and if current 'closing' bracket matches the opening in stack
                if (!(openBrackets.length === 0) && openBrackets[openBrackets.length - 1] === closeToOpen[s[i]]) {
                    openBrackets.pop();
                } else {
                    return false;
                }
            }
        }

        // Check if stack is empty
        return openBrackets.length === 0;
    }
}
