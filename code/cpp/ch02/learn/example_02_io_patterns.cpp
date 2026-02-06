/*
 * Example 02: Input/Output Patterns
 * ===================================
 * Chapter 2: Your First Programs — Speaking Three Languages
 *
 * This file shows you the common ways to read input and print output
 * in C++. These patterns show up in every competitive programming problem.
 *
 * Build and run:
 *   g++ -std=c++17 -o example_02 example_02_io_patterns.cpp && ./example_02
 *
 * NOTE: This example is interactive — it asks you to type things in!
 */

#include <iostream>
#include <string>
#include <iomanip>  // for setprecision, setw, fixed
using namespace std;

int main() {
    // ── 1. Basic output with cout ────────────────────────────────────────
    cout << "=== Basic Output ===" << endl;
    cout << "Hello, world!" << endl;           // endl = newline + flush
    cout << "Hello, world!\n";                 // \n = newline (slightly faster)
    cout << "You can " << "chain " << "multiple " << "things." << endl;
    cout << "Mix types: " << 42 << " and " << 3.14 << " and " << 'A' << endl;
    cout << endl;

    // ── 2. Reading a single value with cin ───────────────────────────────
    cout << "=== Reading with cin ===" << endl;
    cout << "Enter your age: ";
    int age;
    cin >> age;
    cout << "You are " << age << " years old." << endl;
    cout << endl;

    // ── 3. Reading multiple values on one line ───────────────────────────
    cout << "=== Reading multiple values ===" << endl;
    cout << "Enter two numbers (space-separated): ";
    int a, b;
    cin >> a >> b;
    cout << "You entered: " << a << " and " << b << endl;
    cout << "Sum: " << a + b << endl;
    cout << endl;

    // ── 4. Reading a string with cin (single word) ───────────────────────
    cout << "=== Reading a word ===" << endl;
    cout << "Enter your first name: ";
    string firstName;
    cin >> firstName;  // reads until whitespace
    cout << "Hello, " << firstName << "!" << endl;
    cout << endl;

    // ── 5. Reading a full line with getline ──────────────────────────────
    // IMPORTANT: After using cin >>, there's a leftover newline in the
    // input buffer. You must call cin.ignore() before getline().
    cout << "=== Reading a full line ===" << endl;
    cout << "Enter your full name: ";
    cin.ignore();  // discard the leftover newline from previous cin >>
    string fullName;
    getline(cin, fullName);  // reads entire line including spaces
    cout << "Hello, " << fullName << "!" << endl;
    cout << endl;

    // ── 6. Formatted output with iomanip ─────────────────────────────────
    cout << "=== Formatted Output ===" << endl;

    // Fixed decimal places:
    double pi = 3.14159265358979;
    cout << "Default:     " << pi << endl;
    cout << "fixed, 2dp:  " << fixed << setprecision(2) << pi << endl;
    cout << "fixed, 6dp:  " << fixed << setprecision(6) << pi << endl;

    // Reset to default formatting:
    cout << defaultfloat;

    // Right-aligned with setw (set width):
    cout << endl << "Right-aligned numbers:" << endl;
    cout << setw(8) << 1 << endl;
    cout << setw(8) << 42 << endl;
    cout << setw(8) << 1000 << endl;
    cout << setw(8) << 99999 << endl;
    cout << endl;

    // ── 7. Printing booleans as words ────────────────────────────────────
    cout << "=== Boolean output ===" << endl;
    bool flag = true;
    cout << "Default:  " << flag << endl;         // prints 1
    cout << "As word:  " << boolalpha << flag << endl;  // prints true
    cout << noboolalpha;  // reset
    cout << endl;

    // ── 8. Common competitive programming I/O pattern ────────────────────
    // In contests, you typically read from stdin and write to stdout.
    // The pattern is always the same:
    //
    //   int n;
    //   cin >> n;
    //   // process n
    //   cout << answer << endl;
    //
    // For faster I/O in contests, add this at the start of main():
    //   ios_base::sync_with_stdio(false);
    //   cin.tie(NULL);
    //
    // We don't use it here because this is a learning example, but you'll
    // see it in contest code.

    cout << "=== I/O Tips ===" << endl;
    cout << "Tip 1: Use cin >> for single values or space-separated values." << endl;
    cout << "Tip 2: Use getline(cin, str) for full lines with spaces." << endl;
    cout << "Tip 3: Call cin.ignore() before getline if you used cin >> before." << endl;
    cout << "Tip 4: endl flushes the buffer; '\\n' is faster for large output." << endl;
    cout << endl;

    cout << "Done! You've learned C++ I/O patterns." << endl;
    return 0;
}
