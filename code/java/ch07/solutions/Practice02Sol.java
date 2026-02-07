package ch07.solutions;

import java.util.*;

/**
 * Solution for Practice 02: GCD and LCM
 * =========================================
 * Chapter 7: Number Wizardry
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Euclidean algorithm for GCD: gcd(a, b) = gcd(b, a % b).
 * LCM = a / gcd * b (divide first to prevent overflow).
 * If gcd is 0, lcm is 0.
 *
 * TIME COMPLEXITY:  O(log(min(a, b)))
 * SPACE COMPLEXITY: O(1)
 */
public class Practice02Sol {

    public static long[] solve(long a, long b) {
        long g = gcd(a, b);
        long lcm = (g == 0) ? 0 : a / g * b;
        return new long[]{g, lcm};
    }

    private static long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = Long.parseLong(sc.nextLine().trim());
        long b = Long.parseLong(sc.nextLine().trim());
        long[] result = solve(a, b);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
