/*
 * Example 01: Digit Explorer
 * ==========================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * This file demonstrates fundamental digit operations:
 *   Part 1: Extracting digits (mod-10 / div-10 pattern)
 *   Part 2: Counting digits
 *   Part 3: Reversing a number
 *   Part 4: Palindrome check
 *   Part 5: Armstrong numbers
 *
 * Build & run:
 *   g++ -std=c++17 -o example_01 code/cpp/ch07/learn/example_01_digit_explorer.cpp && ./example_01
 */

#include <cmath>
#include <iostream>
using namespace std;

// =====================================================================
// 1. Extracting digits -- the mod-10 / div-10 pattern
// =====================================================================
// n % 10 gives you the LAST digit.
// n / 10 chops off the last digit.
// Keep going until n is 0.

void demo_extract_digits() {
    cout << "=== PART 1: Extracting Digits ===" << endl;

    long long n = 92736;
    cout << "  Number: " << n << endl;
    cout << "  Digits (right to left): ";

    long long temp = n;
    while (temp > 0) {
        cout << temp % 10 << " ";
        temp /= 10;
    }
    cout << endl;

    // If you want them left-to-right, collect first, then reverse
    cout << "  Digits (left to right):  ";
    int digits[20];
    int count = 0;
    temp = n;
    while (temp > 0) {
        digits[count++] = (int)(temp % 10);
        temp /= 10;
    }
    for (int i = count - 1; i >= 0; i--) {
        cout << digits[i] << " ";
    }
    cout << endl << endl;
}

// =====================================================================
// 2. Counting digits
// =====================================================================
// How many digits does a number have?
// Method 1: Keep dividing by 10 and count.
// Method 2: Use log10 (but watch out for 0!).

void demo_count_digits() {
    cout << "=== PART 2: Counting Digits ===" << endl;

    long long numbers[] = {0, 7, 42, 12345, 1000000000LL};

    for (long long n : numbers) {
        // Method 1: Loop
        int count = 0;
        long long temp = (n == 0) ? 1 : abs(n);  // 0 has 1 digit
        if (n == 0) count = 1;
        else {
            temp = abs(n);
            while (temp > 0) { count++; temp /= 10; }
        }

        // Method 2: log10 (only works for positive numbers)
        int log_count = (n == 0) ? 1 : (int)log10(abs(n)) + 1;

        cout << "  n = " << n
             << "  |  loop count = " << count
             << "  |  log10 count = " << log_count << endl;
    }
    cout << endl;
}

// =====================================================================
// 3. Reversing a number
// =====================================================================
// Build the reversed number digit by digit:
//   reversed = reversed * 10 + last_digit

void demo_reverse() {
    cout << "=== PART 3: Reversing a Number ===" << endl;

    long long numbers[] = {12345, 1200, -789, 5, 0};

    for (long long n : numbers) {
        long long sign = (n < 0) ? -1 : 1;
        long long temp = abs(n);
        long long reversed = 0;

        while (temp > 0) {
            reversed = reversed * 10 + temp % 10;
            temp /= 10;
        }
        reversed *= sign;

        cout << "  " << n << " reversed = " << reversed << endl;
    }
    cout << endl;
}

// =====================================================================
// 4. Palindrome check
// =====================================================================
// A number is a palindrome if it reads the same forwards and backwards.
// Negative numbers are NOT palindromes (the minus sign doesn't mirror).

void demo_palindrome() {
    cout << "=== PART 4: Palindrome Check ===" << endl;

    long long numbers[] = {121, 1234321, 10, -121, 0, 1001, 12321};

    for (long long n : numbers) {
        bool is_palindrome = false;

        if (n < 0) {
            is_palindrome = false;
        } else {
            long long temp = n;
            long long reversed = 0;
            while (temp > 0) {
                reversed = reversed * 10 + temp % 10;
                temp /= 10;
            }
            is_palindrome = (reversed == n);
        }

        cout << "  " << n << " -> "
             << (is_palindrome ? "PALINDROME" : "not palindrome") << endl;
    }
    cout << endl;
}

// =====================================================================
// 5. Armstrong numbers
// =====================================================================
// A number is an Armstrong number (narcissistic number) if the sum of
// its digits each raised to the power of the number of digits equals
// the number itself.
//
// Example: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153  (Yes!)
//          9474 = 9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474

void demo_armstrong() {
    cout << "=== PART 5: Armstrong Numbers ===" << endl;

    cout << "  Armstrong numbers up to 10000:" << endl << "  ";

    for (long long n = 0; n <= 10000; n++) {
        // Count digits
        int numDigits = 0;
        long long temp = n;
        if (n == 0) numDigits = 1;
        else while (temp > 0) { numDigits++; temp /= 10; }

        // Sum of digits^numDigits
        temp = n;
        long long sum = 0;
        while (temp > 0) {
            long long d = temp % 10;
            sum += (long long)pow(d, numDigits);
            temp /= 10;
        }

        if (sum == n) {
            cout << n << " ";
        }
    }
    cout << endl << endl;
}

// =====================================================================
// main -- run all demos
// =====================================================================
int main() {
    cout << "Chapter 7: Digit Explorer" << endl;
    cout << "=========================" << endl << endl;

    demo_extract_digits();
    demo_count_digits();
    demo_reverse();
    demo_palindrome();
    demo_armstrong();

    cout << "The mod-10/div-10 pattern is one of the most useful tricks" << endl;
    cout << "in competitive programming. Master it, and digits are easy!" << endl;
    return 0;
}
