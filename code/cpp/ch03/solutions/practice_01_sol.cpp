/*
 * Solution for Practice 01: FizzBuzz
 * ====================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Loop from 1 to n. For each number, check divisibility:
 *   1. Check "both 3 and 5" FIRST (divisible by 15), otherwise
 *      "Fizz" would match before "FizzBuzz" ever could.
 *   2. Then check 3, then 5, then default to the number itself.
 *
 * TIME COMPLEXITY:  O(n) — one pass through all numbers
 * SPACE COMPLEXITY: O(n) — for the result vector
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> solve(int n) {
    vector<string> result;
    for (int i = 1; i <= n; i++) {
        if (i % 15 == 0) {
            result.push_back("FizzBuzz");
        } else if (i % 3 == 0) {
            result.push_back("Fizz");
        } else if (i % 5 == 0) {
            result.push_back("Buzz");
        } else {
            result.push_back(to_string(i));
        }
    }
    return result;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    vector<string> result = solve(n);
    for (const string& line : result) {
        cout << line << endl;
    }
    return 0;
}
