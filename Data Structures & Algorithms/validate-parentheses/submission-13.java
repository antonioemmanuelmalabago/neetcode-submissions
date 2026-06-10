class Solution {
    public boolean isValid(String s) {
        // Create stack of openBrackets using ArrayList
        ArrayList<Character> openBrackets = new ArrayList<Character>();
        // Create dictionary of open-close bracket pairs
        HashMap<Character, Character> closeToOpen = new HashMap<Character, Character>();
        closeToOpen.put(')', '(');
        closeToOpen.put(']', '[');
        closeToOpen.put('}', '{');

        // Iterate through each character in the string
        for (int i = 0; i < s.length(); i++) {
            // Check if character is 'not' closing bracket
            if (!closeToOpen.containsKey(s.charAt(i))) {
                // If not, add to openBrackets stack
                openBrackets.add(s.charAt(i));
            } else {
                // Check if stack is not empty and if current 'closing' bracket matches the opening in stack
                if (!openBrackets.isEmpty() && openBrackets.get(openBrackets.size() - 1) == closeToOpen.get(s.charAt(i))) {
                    // If yes, remove the opening bracket from the stack
                    openBrackets.remove(openBrackets.size() - 1);
                } else {
                    // Else, the string is not valid
                    return false;
                }
            }
        }

        // Check if stack is empty
        if (openBrackets.size() != 0) {
            return false;
        }

        return true;
    }
}
