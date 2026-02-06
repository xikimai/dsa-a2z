package ch03.solutions;

import java.util.Scanner;

/**
 * Solution for Practice 03: Reverse Number
 * ==========================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Handle the sign separately. Work with the absolute value:
 *   1. Extract the last digit with num % 10
 *   2. Append it to the reversed number: reversed = reversed * 10 + digit
 *   3. Remove the last digit: num /= 10
 *   4. Repeat until num is 0
 * Re-apply the sign at the end.
 *
 * Leading zeros are automatically dropped because integer arithmetic
 * ignores leading zeros (e.g., 0021 is just 21).
 *
 * TIME COMPLEXITY:  O(d) — where d is the number of digits
 * SPACE COMPLEXITY: O(1) — just a few variables
 */
public class Practice03Sol {

    public static int solve(int n) {
        int sign = (n < 0) ? -1 : 1;
        int num = (n < 0) ? -n : n;
        int reversed = 0;
        while (num > 0) {
            reversed = reversed * 10 + num % 10;
            num /= 10;
        }
        return sign * reversed;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(solve(n));
        scanner.close();
    }
}
