/*
 * Solution -- Warmup 4: Check Palindrome
 * =========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Base case: length 0 or 1 is always a palindrome.
 *           If first != last, return false.
 *           Otherwise recurse on the middle substring.
 * TIME:  O(n^2) due to substring creation
 * SPACE: O(n^2) due to substring copies on call stack
 */

#include <iostream>
#include <string>
using namespace std;

bool solve(string s) {
    if (s.size() <= 1) return true;
    if (s.front() != s.back()) return false;
    return solve(s.substr(1, s.size() - 2));
}

// -- Do not change anything below this line --------------------------
int main() {
    string s;
    getline(cin, s);
    cout << (solve(s) ? "true" : "false") << endl;
    return 0;
}
