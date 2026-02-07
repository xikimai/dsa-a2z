package ch07.solutions;

import java.util.*;

/**
 * Solution for Practice 01: All Divisors
 * =========================================
 * Chapter 7: Number Wizardry
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Loop from 1 to sqrt(n). If i divides n, add both i and n/i (unless
 * they are equal). Sort the result.
 *
 * TIME COMPLEXITY:  O(sqrt(n))
 * SPACE COMPLEXITY: O(number of divisors)
 */
public class Practice01Sol {

    public static List<Integer> solve(int n) {
        List<Integer> divs = new ArrayList<>();
        for (int i = 1; (long) i * i <= n; i++) {
            if (n % i == 0) {
                divs.add(i);
                if (i != n / i) divs.add(n / i);
            }
        }
        Collections.sort(divs);
        return divs;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
