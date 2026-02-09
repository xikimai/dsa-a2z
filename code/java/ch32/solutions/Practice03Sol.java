package ch32.solutions;

import java.util.*;

public class Practice03Sol {
    public static int solve(String s) {
        Set<String> subs = new HashSet<>();
        int n = s.length();
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j <= n; j++)
                subs.add(s.substring(i, j));
        return subs.size() + 1; // +1 for empty string
    }
}
