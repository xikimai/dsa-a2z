package ch07.learn;

import java.util.*;

/**
 * Example 02: GCD Race and Number Theory Toolkit
 * ================================================
 * Chapter 7: Number Wizardry
 *
 * This file demonstrates three pillars of competitive programming math:
 *   1. GCD — comparing subtraction vs Euclidean algorithm (with timing)
 *   2. Sieve of Eratosthenes — visual demo of prime generation
 *   3. Binary exponentiation — computing huge powers in O(log n)
 *
 * Build and run:
 *   cd code/java
 *   javac ch07/learn/Example02GcdRace.java
 *   java ch07.learn.Example02GcdRace
 */
public class Example02GcdRace {

    // ── 1. GCD by Subtraction ─────────────────────────────────────────
    // The ancient approach: keep subtracting the smaller from the larger.
    // Simple but SLOW when numbers are far apart (e.g., gcd(1000000, 3)).

    static long gcdSubtract(long a, long b) {
        if (a == 0) return b;
        if (b == 0) return a;
        while (a != b) {
            if (a > b) a -= b;
            else b -= a;
        }
        return a;
    }

    // ── 2. GCD by Euclidean Algorithm ─────────────────────────────────
    // Replace subtraction with modulo — dramatically faster!
    // gcd(a, b) = gcd(b, a % b), and it reaches 0 in O(log(min(a,b))) steps.

    static long gcdEuclidean(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    static void demoGcdRace() {
        System.out.println("=== Part 1: GCD Race — Subtraction vs Euclidean ===\n");

        // Small example with step-by-step trace
        System.out.println("  Step-by-step: gcd(48, 18)");
        System.out.println("  Subtraction:  48-18=30, 30-18=12, 18-12=6, 12-6=6 -> 6  (4 steps)");
        System.out.println("  Euclidean:    48%18=12, 18%12=6, 12%6=0 -> 6         (3 steps)\n");

        // Timing race!
        long[][] pairs = {
            {252, 105},
            {10000, 3},
            {1000000, 7},
            {999999937L, 999999929L}   // two large primes
        };

        System.out.printf("  %-25s  %12s  %12s%n", "Input", "Subtract(ns)", "Euclid(ns)");
        System.out.println("  " + "-".repeat(55));

        for (long[] pair : pairs) {
            long a = pair[0], b = pair[1];
            String label = "gcd(" + a + ", " + b + ")";

            // Skip subtraction for very large inputs — it would take forever
            long subtractTime;
            if (a > 100000 || b > 100000) {
                subtractTime = -1; // too slow
            } else {
                long start = System.nanoTime();
                gcdSubtract(a, b);
                subtractTime = System.nanoTime() - start;
            }

            long start = System.nanoTime();
            long result = gcdEuclidean(a, b);
            long euclidTime = System.nanoTime() - start;

            if (subtractTime < 0) {
                System.out.printf("  %-25s  %12s  %,12d  (gcd = %d)%n",
                    label, "TOO SLOW!", euclidTime, result);
            } else {
                System.out.printf("  %-25s  %,12d  %,12d  (gcd = %d)%n",
                    label, subtractTime, euclidTime, result);
            }
        }

        System.out.println("\n  Lesson: Euclidean is O(log n) vs subtraction's O(n). Huge difference!\n");
    }

    // ── 3. Sieve of Eratosthenes ─────────────────────────────────────

    static List<Integer> sieve(int limit) {
        boolean[] isPrime = new boolean[limit + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; (long) i * i <= limit; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= limit; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= limit; i++) {
            if (isPrime[i]) primes.add(i);
        }
        return primes;
    }

    static void demoSieve() {
        System.out.println("=== Part 2: Sieve of Eratosthenes ===\n");

        // Visual demo with a small grid
        int n = 50;
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;

        System.out.println("  Starting grid (2 to " + n + "): all marked as potential primes\n");

        for (int i = 2; (long) i * i <= n; i++) {
            if (isPrime[i]) {
                int crossed = 0;
                for (int j = i * i; j <= n; j += i) {
                    if (isPrime[j]) crossed++;
                    isPrime[j] = false;
                }
                if (crossed > 0) {
                    System.out.printf("  Sieving %d: crossed out %d composites (starting from %d^2 = %d)%n",
                        i, crossed, i, i * i);
                }
            }
        }

        System.out.print("\n  Primes up to " + n + ": ");
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) System.out.print(i + " ");
        }
        System.out.println("\n");

        // Performance
        System.out.println("  How fast is the sieve?");
        int[] sizes = {1000, 10000, 100000, 1000000};
        for (int size : sizes) {
            long start = System.nanoTime();
            List<Integer> primes = sieve(size);
            long elapsed = System.nanoTime() - start;
            System.out.printf("    Primes up to %,9d: found %,6d primes in %,10d ns%n",
                size, primes.size(), elapsed);
        }
        System.out.println("\n  The sieve runs in O(n log log n) — almost linear!\n");
    }

    // ── 4. Binary Exponentiation ──────────────────────────────────────

    static long power(long base, long exp, long mod) {
        long result = 1;
        base %= mod;
        while (exp > 0) {
            if (exp % 2 == 1) {
                result = result * base % mod;
            }
            exp /= 2;
            base = base * base % mod;
        }
        return result;
    }

    static void demoBinaryExp() {
        System.out.println("=== Part 3: Binary Exponentiation ===\n");

        System.out.println("  Problem: compute 2^100 mod (10^9 + 7)");
        System.out.println("  Naive approach: multiply 2 a hundred times -> 100 multiplications");
        System.out.println("  Binary exp: use the binary representation of 100 -> ~7 multiplications\n");

        // Step-by-step trace for 2^13
        System.out.println("  Trace: 2^13 mod 1000000007");
        System.out.println("    13 in binary = 1101");
        System.out.println("    exp=13 (odd):  result *= 2    -> result=2,    base: 2->4");
        System.out.println("    exp=6  (even): skip,          -> result=2,    base: 4->16");
        System.out.println("    exp=3  (odd):  result *= 16   -> result=32,   base: 16->256");
        System.out.println("    exp=1  (odd):  result *= 256  -> result=8192, base: 256->65536");
        System.out.println("    Answer: 8192  (check: 2^13 = 8192) \n");

        // Show some computations
        long mod = 1000000007L;
        System.out.println("  Power computations (mod 10^9 + 7):");
        long[][] tests = {
            {2, 10}, {2, 100}, {2, 1000},
            {3, 50}, {7, 77}, {123456789, 987654321}
        };
        for (long[] test : tests) {
            long result = power(test[0], test[1], mod);
            System.out.printf("    %d ^ %d mod 10^9+7 = %d%n", test[0], test[1], result);
        }

        System.out.println("\n  Binary exponentiation runs in O(log exp) — even 2^(10^18) is fast!");
        System.out.println("  This is essential for competitive programming.\n");
    }

    // ── Main ─────────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("Chapter 7: GCD Race and Number Theory Toolkit");
        System.out.println("==============================================\n");

        demoGcdRace();
        demoSieve();
        demoBinaryExp();

        System.out.println("KEY TAKEAWAYS:");
        System.out.println("  1. Always use Euclidean GCD, never subtraction");
        System.out.println("  2. Sieve of Eratosthenes finds all primes up to n in near-linear time");
        System.out.println("  3. Binary exponentiation computes a^b mod m in O(log b)");
        System.out.println("  These three tools solve 90% of math problems in contests!");
    }
}
