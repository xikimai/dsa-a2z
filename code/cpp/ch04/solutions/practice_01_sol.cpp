/*
 * Solution — Practice 1: Calculator
 * ==================================
 * Chapter 4: Functions
 *
 * APPROACH:
 *   Define helper functions for each arithmetic operation.
 *   The solve_valid() function checks if the operation is recognized
 *   and not a divide-by-zero case.
 *   The solve() function dispatches to the correct helper.
 *
 * TIME COMPLEXITY:  O(1)
 * SPACE COMPLEXITY: O(1)
 */

#include <iostream>
#include <string>
using namespace std;

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int multiply(int a, int b) {
    return a * b;
}

int divide(int a, int b) {
    return a / b;  // integer division
}

bool solve_valid(int a, string op, int b) {
    if (op == "add" || op == "subtract" || op == "multiply") {
        return true;
    }
    if (op == "divide" && b != 0) {
        return true;
    }
    return false;
}

int solve(int a, string op, int b) {
    if (!solve_valid(a, op, b)) {
        return 0;
    }
    if (op == "add") return add(a, b);
    if (op == "subtract") return subtract(a, b);
    if (op == "multiply") return multiply(a, b);
    if (op == "divide") return divide(a, b);
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
