package ch07.learn;

/**
 * Example 01: Digit Explorer
 * ==============================
 * Chapter 7: Number Wizardry
 *
 * This file demonstrates the fundamental digit operations that underpin
 * many math-based coding problems: extracting digits, counting them,
 * reversing a number, checking for palindromes, and Armstrong numbers.
 *
 * Build and run:
 *   cd code/java
 *   javac ch07/learn/Example01DigitExplorer.java
 *   java ch07.learn.Example01DigitExplorer
 */
public class Example01DigitExplorer {

    // ── 1. Extracting Digits ──────────────────────────────────────────
    // The mod-10 trick: n % 10 gives the last digit, n / 10 removes it.

    static void demoExtractDigits() {
        System.out.println("=== Part 1: Extracting Digits ===");
        System.out.println("The key trick: n % 10 = last digit, n / 10 = remove last digit\n");

        int n = 4728;
        System.out.println("  Breaking down " + n + ":");
        int temp = n;
        int position = 1;
        while (temp > 0) {
            int digit = temp % 10;
            System.out.printf("    Step %d: %d %% 10 = %d   (remaining: %d / 10 = %d)%n",
                position, temp, digit, temp, temp / 10);
            temp /= 10;
            position++;
        }
        System.out.println();
    }

    // ── 2. Counting Digits ────────────────────────────────────────────

    static int countDigits(long n) {
        n = Math.abs(n);
        if (n == 0) return 1;
        int count = 0;
        while (n > 0) {
            count++;
            n /= 10;
        }
        return count;
    }

    static void demoCountDigits() {
        System.out.println("=== Part 2: Counting Digits ===");
        System.out.println("Keep dividing by 10 until you hit 0.\n");

        long[] examples = {0, 7, 42, 12345, -999, 1000000000L};
        for (long num : examples) {
            System.out.printf("  countDigits(%d) = %d%n", num, countDigits(num));
        }
        System.out.println("\n  Pro tip: Math.floor(Math.log10(n)) + 1 also works for n > 0,");
        System.out.println("  but the loop approach handles 0 and negatives cleanly.\n");
    }

    // ── 3. Reversing a Number ─────────────────────────────────────────

    static long reverseNumber(long n) {
        long sign = n < 0 ? -1 : 1;
        n = Math.abs(n);
        long reversed = 0;
        while (n > 0) {
            reversed = reversed * 10 + n % 10;
            n /= 10;
        }
        return sign * reversed;
    }

    static void demoReverse() {
        System.out.println("=== Part 3: Reversing a Number ===");
        System.out.println("Build the reversed number digit by digit: result = result * 10 + digit\n");

        long n = 1234;
        long temp = n;
        long reversed = 0;
        System.out.println("  Reversing " + n + " step by step:");
        while (temp > 0) {
            long digit = temp % 10;
            long oldReversed = reversed;
            reversed = reversed * 10 + digit;
            System.out.printf("    digit = %d, reversed = %d * 10 + %d = %d%n",
                digit, oldReversed, digit, reversed);
            temp /= 10;
        }

        System.out.println("\n  More examples:");
        long[] examples = {12345, -678, 1200, 0};
        for (long num : examples) {
            System.out.printf("    reverse(%d) = %d%n", num, reverseNumber(num));
        }
        System.out.println();
    }

    // ── 4. Palindrome Check ───────────────────────────────────────────

    static boolean isPalindrome(long n) {
        if (n < 0) return false;
        return n == reverseNumber(n);
    }

    static void demoPalindrome() {
        System.out.println("=== Part 4: Palindrome Numbers ===");
        System.out.println("A number is a palindrome if it reads the same forwards and backwards.\n");

        long[] examples = {121, 12321, 1001, 123, -121, 10, 0, 1, 11};
        for (long num : examples) {
            String result = isPalindrome(num) ? "YES" : "no";
            System.out.printf("  %6d -> %s%n", num, result);
        }
        System.out.println("\n  Key insight: negative numbers are NEVER palindromes (the minus sign).\n");
    }

    // ── 5. Armstrong Numbers ──────────────────────────────────────────

    static boolean isArmstrong(long n) {
        if (n < 0) return false;
        int numDigits = countDigits(n);
        long temp = n;
        long sum = 0;
        while (temp > 0) {
            long digit = temp % 10;
            sum += (long) Math.pow(digit, numDigits);
            temp /= 10;
        }
        return sum == n;
    }

    static void demoArmstrong() {
        System.out.println("=== Part 5: Armstrong Numbers ===");
        System.out.println("A k-digit number is Armstrong if the sum of each digit^k equals itself.\n");

        // Show the math for 153
        System.out.println("  Example: Is 153 an Armstrong number?");
        System.out.println("    153 has 3 digits");
        System.out.println("    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153  -> YES!\n");

        // Show the math for 370
        System.out.println("  Example: Is 370 an Armstrong number?");
        System.out.println("    370 has 3 digits");
        System.out.println("    3^3 + 7^3 + 0^3 = 27 + 343 + 0 = 370  -> YES!\n");

        System.out.println("  All Armstrong numbers up to 10000:");
        System.out.print("    ");
        for (long i = 0; i <= 10000; i++) {
            if (isArmstrong(i)) {
                System.out.print(i + " ");
            }
        }
        System.out.println("\n");

        System.out.println("  Fun fact: there are only 88 Armstrong numbers in total!");
        System.out.println("  The largest is 115,132,219,018,763,992,565,095,597,973,971,522,401\n");
    }

    // ── Main ─────────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("Chapter 7: Digit Explorer — Number Wizardry");
        System.out.println("============================================\n");

        demoExtractDigits();
        demoCountDigits();
        demoReverse();
        demoPalindrome();
        demoArmstrong();

        System.out.println("KEY TAKEAWAY:");
        System.out.println("  The mod-10 / divide-10 pattern is the foundation of digit problems.");
        System.out.println("  Master it and you can count, reverse, check palindromes, and more!");
    }
}
