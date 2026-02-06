package ch04.solutions;

import java.util.Scanner;

/**
 * Solution for Practice 02: Password Strength
 * =============================================
 * Chapter 4: Functions
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use helper functions hasDigit() and hasUpper() that scan each character.
 * Then combine: weak if too short, strong if both conditions met, medium
 * if only one condition met, weak if neither.
 *
 * TIME COMPLEXITY:  O(n) where n is the password length
 * SPACE COMPLEXITY: O(1)
 */
public class Practice02Sol {

    public static boolean hasDigit(String s) {
        for (int i = 0; i < s.length(); i++) {
            if (Character.isDigit(s.charAt(i))) return true;
        }
        return false;
    }

    public static boolean hasUpper(String s) {
        for (int i = 0; i < s.length(); i++) {
            if (Character.isUpperCase(s.charAt(i))) return true;
        }
        return false;
    }

    public static String solve(String password) {
        if (password.length() < 8) return "weak";
        boolean digit = hasDigit(password);
        boolean upper = hasUpper(password);
        if (digit && upper) return "strong";
        if (digit || upper) return "medium";
        return "weak";
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String password = sc.nextLine().trim();
        System.out.println(solve(password));
        sc.close();
    }
}
