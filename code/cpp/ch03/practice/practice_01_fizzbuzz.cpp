/*
 * Practice 01: FizzBuzz
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given a positive integer n, return a vector of strings for numbers 1 to n:
 *   - If the number is divisible by both 3 and 5, use "FizzBuzz"
 *   - If the number is divisible by 3 only, use "Fizz"
 *   - If the number is divisible by 5 only, use "Buzz"
 *   - Otherwise, use the number as a string
 *
 * INPUT FORMAT
 * ------------
 * A single line containing a positive integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print n lines, each being the FizzBuzz value for that number.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= n <= 10000
 *
 * EXAMPLES
 * --------
 * Input:  5
 * Output:
 *   1
 *   2
 *   Fizz
 *   4
 *   Buzz
 *
 * Input:  15
 * Output:
 *   1
 *   2
 *   Fizz
 *   ...
 *   14
 *   FizzBuzz
 *
 * INSTRUCTIONS
 * ------------
 * Replace the body of solve() with your solution.
 * The main() function handles I/O -- don't change it.
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

/**
 * Return a vector of FizzBuzz strings for numbers 1 through n.
 */
vector<string> solve(int n) {
    // TODO: Replace this with your solution
    return {};
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
