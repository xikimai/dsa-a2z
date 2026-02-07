package ch07.solutions;

import java.util.*;

/**
 * Solution for Challenge 02: Sieve of Eratosthenes
 * =========================================
 * Chapter 7: Number Wizardry
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Classic sieve: create a boolean array, mark composites starting from
 * i*i for each prime i. Collect all unmarked numbers >= 2.
 *
 * TIME COMPLEXITY:  O(n log log n)
 * SPACE COMPLEXITY: O(n)
 */
public class Challenge02Sol {

    public static List<Integer> solve(int n) {
        List<Integer> primes = new ArrayList<>();
        if (n < 2) return primes;
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; (long) i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) primes.add(i);
        }
        return primes;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
