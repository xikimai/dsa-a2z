/*
 * Practice 1: Calculator
 * ======================
 * Chapter 4: Functions
 *
 * PROBLEM:
 *   Build a calculator using helper functions. Write separate functions for
 *   add, subtract, multiply, and divide. Then write a solve() function that
 *   dispatches to the correct helper based on the operator string.
 *
 *   Also write a solve_valid() function that returns whether the operation
 *   is valid (since C++ can't return null for int).
 *
 * EXAMPLES:
 *   solve(10, "add", 5)       -> 15       solve_valid(...) -> true
 *   solve(10, "subtract", 3)  -> 7        solve_valid(...) -> true
 *   solve(10, "multiply", 4)  -> 40       solve_valid(...) -> true
 *   solve(10, "divide", 3)    -> 3        solve_valid(...) -> true  (integer division)
 *   solve(10, "divide", 0)    -> 0        solve_valid(...) -> false (divide by zero)
 *   solve(10, "modulo", 3)    -> 0        solve_valid(...) -> false (invalid operator)
 *
 * CONSTRAINTS:
 *   - Valid operators: "add", "subtract", "multiply", "divide"
 *   - Division is integer division (truncated toward zero)
 *   - For invalid operator or divide-by-zero, solve returns 0, solve_valid returns false
 */

#include <iostream>
#include <string>
using namespace std;

// TODO: Write helper functions: add, subtract, multiply, divide

/**
 * Returns true if the operation is valid, false otherwise.
 */
bool solve_valid(int a, string op, int b) {
    // TODO: Replace this with your solution
    return false;
}

/**
 * Performs the calculation. Returns 0 for invalid operations.
 */
int solve(int a, string op, int b) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int a, b;
    string op;
    cin >> a >> op >> b;
    if (solve_valid(a, op, b)) {
        cout << solve(a, op, b) << endl;
    } else {
        cout << "Invalid operation" << endl;
    }
    return 0;
}
