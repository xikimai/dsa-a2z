/*
 * Example 01: Recursion Basics -- Visual Walkthrough
 * ====================================================
 * Chapter 10: The Magic of Recursion
 *
 * This file demonstrates:
 *   Part 1: Factorial trace with indentation showing call depth
 *   Part 2: Fibonacci call counter showing redundant calls
 *   Part 3: Reverse string recursion trace
 *   Part 4: Iteration vs recursion comparison
 *
 * Build & run:
 *   g++ -std=c++17 -o example_01 code/cpp/ch10/learn/example_01_recursion_basics.cpp && ./example_01
 */

#include <iostream>
#include <string>
using namespace std;

// =====================================================================
// 1. Factorial Step-by-Step Trace
// =====================================================================
// Idea: Show each recursive call and return with indentation.
//       The deeper the call, the more indent -- so you can SEE the stack.

long long factorial_traced(int n, int depth = 0) {
    string indent(depth * 2, ' ');
    cout << indent << "factorial(" << n << ") called" << endl;
    if (n == 0) {
        cout << indent << "factorial(0) returns 1  (base case)" << endl;
        return 1;
    }
    long long result = (long long)n * factorial_traced(n - 1, depth + 1);
    cout << indent << "factorial(" << n << ") returns " << result << endl;
    return result;
}

void demo_factorial_trace() {
    cout << "=== PART 1: Factorial -- Step-by-Step Trace ===" << endl;
    cout << endl;
    cout << "  Computing factorial(5):" << endl;
    cout << endl;
    long long result = factorial_traced(5);
    cout << endl;
    cout << "  Final answer: 5! = " << result << endl;
    cout << endl;
    cout << "  Notice how the calls go DOWN (deeper) before coming back UP." << endl;
    cout << "  Each level waits for the one below to finish -- that's recursion!" << endl;
    cout << endl;
}

// =====================================================================
// 2. Fibonacci Call Counter -- Exposing Redundant Calls
// =====================================================================
// Idea: Count how many function calls fib(n) makes.
//       You'll see the count EXPLODES because we recompute the same values.

int fib_counted(int n, int& counter) {
    counter++;
    if (n <= 1) return n;
    return fib_counted(n - 1, counter) + fib_counted(n - 2, counter);
}

void demo_fibonacci_calls() {
    cout << "=== PART 2: Fibonacci -- Redundant Calls Exposed ===" << endl;
    cout << endl;

    for (int n = 2; n <= 10; n++) {
        int counter = 0;
        int result = fib_counted(n, counter);
        cout << "  fib(";
        if (n < 10) cout << " ";
        cout << n << ") = ";
        // Pad result
        string rs = to_string(result);
        for (int i = (int)rs.size(); i < 4; i++) cout << " ";
        cout << rs << "   total calls: ";
        string cs = to_string(counter);
        for (int i = (int)cs.size(); i < 5; i++) cout << " ";
        cout << cs << endl;
    }

    cout << endl;
    cout << "  Look how fast the call count grows!" << endl;
    cout << "  fib(10) needs 177 calls, but only 11 unique values (fib(0)..fib(10))." << endl;
    cout << "  All those extra calls are REDUNDANT. We'll fix this with memoization!" << endl;
    cout << endl;
}

// =====================================================================
// 3. Reverse String Recursion Trace
// =====================================================================
// Idea: Peel off the first character, recurse on the rest, then append.

string reverse_traced(const string& s, int depth = 0) {
    string indent(depth * 2, ' ');
    cout << indent << "reverse(\"" << s << "\")" << endl;
    if (s.size() <= 1) {
        cout << indent << "-> base case, return \"" << s << "\"" << endl;
        return s;
    }
    string rest = s.substr(1);
    string result = reverse_traced(rest, depth + 1) + s[0];
    cout << indent << "-> reverse(\"" << rest << "\") + \"" << s[0]
         << "\" = \"" << result << "\"" << endl;
    return result;
}

void demo_reverse_string() {
    cout << "=== PART 3: Reverse String -- Recursion Trace ===" << endl;
    cout << endl;
    cout << "  Reversing \"hello\":" << endl;
    cout << endl;
    string result = reverse_traced("hello");
    cout << endl;
    cout << "  Final answer: \"" << result << "\"" << endl;
    cout << endl;
    cout << "  Each call peels off the first character and appends it at the end." << endl;
    cout << "  The string shrinks by 1 each time until we hit the base case." << endl;
    cout << endl;
}

// =====================================================================
// 4. Recursion vs Iteration Comparison
// =====================================================================
// Idea: The same problem solved both ways -- same answer, different style.

long long factorial_recursive(int n) {
    if (n == 0) return 1;
    return (long long)n * factorial_recursive(n - 1);
}

long long factorial_iterative(int n) {
    long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

void demo_comparison() {
    cout << "=== PART 4: Recursion vs Iteration -- Factorial Comparison ===" << endl;
    cout << endl;

    cout << "  Recursive code:" << endl;
    cout << "    long long factorial(int n) {" << endl;
    cout << "        if (n == 0) return 1;" << endl;
    cout << "        return (long long)n * factorial(n - 1);" << endl;
    cout << "    }" << endl;
    cout << endl;
    cout << "  Iterative code:" << endl;
    cout << "    long long factorial(int n) {" << endl;
    cout << "        long long result = 1;" << endl;
    cout << "        for (int i = 2; i <= n; i++) result *= i;" << endl;
    cout << "        return result;" << endl;
    cout << "    }" << endl;
    cout << endl;

    cout << "     n    Recursive     Iterative    Match?" << endl;
    cout << "  ----  -----------  ------------  --------" << endl;

    int test_vals[] = {0, 1, 5, 10, 15, 20};
    for (int n : test_vals) {
        long long r = factorial_recursive(n);
        long long it = factorial_iterative(n);
        string match = (r == it) ? "Yes" : "NO!";
        cout << "  ";
        string ns = to_string(n);
        for (int i = (int)ns.size(); i < 4; i++) cout << " ";
        cout << ns << "  ";
        string rs = to_string(r);
        for (int i = (int)rs.size(); i < 11; i++) cout << " ";
        cout << rs << "  ";
        string is = to_string(it);
        for (int i = (int)is.size(); i < 12; i++) cout << " ";
        cout << is << "  ";
        for (int i = (int)match.size(); i < 8; i++) cout << " ";
        cout << match << endl;
    }

    cout << endl;
    cout << "  Both give the same answer! Recursion is elegant," << endl;
    cout << "  but iteration can be faster (no function-call overhead)." << endl;
    cout << "  Choose what makes your code clearest." << endl;
    cout << endl;
}

// =====================================================================
// main -- run all demos
// =====================================================================
int main() {
    cout << "Chapter 10: Recursion Basics -- Visual Walkthrough" << endl;
    cout << "===================================================" << endl << endl;

    demo_factorial_trace();
    demo_fibonacci_calls();
    demo_reverse_string();
    demo_comparison();

    cout << "Key takeaways:" << endl;
    cout << "  - Every recursion needs a BASE CASE (when to stop)" << endl;
    cout << "  - Every recursion needs a RECURSIVE STEP (making the problem smaller)" << endl;
    cout << "  - Naive Fibonacci makes redundant calls -- memoization fixes that" << endl;
    cout << "  - Recursion and iteration can solve the same problems" << endl;
    return 0;
}
