package ch23.solutions;

public class Practice03Sol {
    public static int solve(String s) {
        if (s.isEmpty() || s.charAt(0) == '0') return 0;
        int n = s.length();
        int prev2 = 1, prev1 = 1;
        for (int i = 2; i <= n; i++) {
            int current = 0;
            if (s.charAt(i - 1) != '0') current += prev1;
            int twoDigit = Integer.parseInt(s.substring(i - 2, i));
            if (twoDigit >= 10 && twoDigit <= 26) current += prev2;
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }
}
