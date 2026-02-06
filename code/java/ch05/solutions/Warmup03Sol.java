package ch05.solutions;

import java.util.*;

/**
 * Solution for Warmup 03: Count Vowels
 * =====================================
 * Chapter 5: Collections
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use a set of vowels for O(1) lookup. Convert each character to
 * lowercase and check membership.
 *
 * TIME COMPLEXITY:  O(n) where n is the string length
 * SPACE COMPLEXITY: O(1)
 */
public class Warmup03Sol {

    public static int solve(String s) {
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        int count = 0;
        for (char c : s.toLowerCase().toCharArray()) {
            if (vowels.contains(c)) {
                count++;
            }
        }
        return count;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        System.out.println(solve(line));
        sc.close();
    }
}
