class Solution {

   // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        for (String s : strs) {
            // Append the length of the string followed by '#' and the string itself
            encoded.append(s.length()).append("#").append(s);
        }
        return encoded.toString();
    }

    // Decodes a single string back into a list of strings.
    public List<String> decode(String s) {
        List<String> decoded = new ArrayList<>();
        int i = 0;
        while (i < s.length()) {
            // Find the position of the next delimiter (#)
            int j = s.indexOf('#', i);
            // The number before the # is the length of the next string
            int length = Integer.parseInt(s.substring(i, j));
            // Extract the string using the length
            decoded.add(s.substring(j + 1, j + 1 + length));
            // Move the index past the current string
            i = j + 1 + length;
        }
        return decoded;
    }
}
