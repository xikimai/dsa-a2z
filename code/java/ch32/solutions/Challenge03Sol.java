package ch32.solutions;

import java.util.*;

public class Challenge03Sol {
    public static int solve(String s, int k) {
        int n = s.length();
        if (k > n) return 0;
        Set<String> seen = new HashSet<>();
        for (int i = 0; i <= n - k; i++)
            seen.add(s.substring(i, i + k));
        return seen.size();
    }
}
