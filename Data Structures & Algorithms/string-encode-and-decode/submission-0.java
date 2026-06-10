class Solution {
    // Encodes a list of strings to a single string
    public String encode(List<String> strs) {

        // Handle the edge case where list is empty
        if (strs.size() == 0) {
            // Use a special character (ASCII 258) to represent an empty list
            return Character.toString((char)258);
        }

        // Define a separator character (ASCII 257) that does not appear in normal text
        String separator = Character.toString((char)257);
        StringBuilder sb = new StringBuilder();

        // Append each string followed by a separator
        for (String s : strs) {
            sb.append(s);
            sb.append(separator);
        }

        // Remove the last separator to avoid extra split issues
        sb.deleteCharAt(sb.length() - 1);

        return sb.toString();
    }

    // Decodes a single encoded string back to a list of strings
    public List<String> decode(String s) {

        // Handle the case where the input is the special empty list marker
        if (s.equals(Character.toString((char)258))) {
            return new ArrayList();
        }

        // Define the same separator used during encoding
        String separator = Character.toString((char)257);

        // Split the string using the separator, preserving empty strings
        return Arrays.asList(s.split(separator, -1));
    }
}