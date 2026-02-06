/*
 * Solution — Practice 2: Password Strength
 * =========================================
 * Chapter 4: Functions
 *
 * APPROACH:
 *   Write two helper functions that scan the string for specific
 *   character types. Then combine length check + helpers for the
 *   three-tier classification.
 *
 * TIME COMPLEXITY:  O(n) where n = password.length()
 * SPACE COMPLEXITY: O(1)
 */

#include <iostream>
#include <string>
using namespace std;

bool has_digit(string s) {
    for (char c : s) {
        if (c >= '0' && c <= '9') return true;
    }
    return false;
}

bool has_upper(string s) {
    for (char c : s) {
        if (c >= 'A' && c <= 'Z') return true;
    }
    return false;
}

string solve(string password) {
    if ((int)password.length() < 8) {
        return "weak";
    }
    if (has_digit(password) && has_upper(password)) {
        return "strong";
    }
    return "medium";
}

// -- Do not change anything below this line --------------------------
int main() {
    string password;
    getline(cin, password);
    cout << solve(password) << endl;
    return 0;
}
