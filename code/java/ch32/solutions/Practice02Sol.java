package ch32.solutions;

public class Practice02Sol {
    public static String solve(String[] words) {
        if (words.length == 0) return "";
        StringBuilder prefix = new StringBuilder();
        for (int i = 0; i < words[0].length(); i++) {
            char ch = words[0].charAt(i);
            for (int j = 1; j < words.length; j++) {
                if (i >= words[j].length() || words[j].charAt(i) != ch)
                    return prefix.toString();
            }
            prefix.append(ch);
        }
        return prefix.toString();
    }
}
