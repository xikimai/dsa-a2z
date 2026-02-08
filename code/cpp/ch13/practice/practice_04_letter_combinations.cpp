/*
 * Practice 4: Letter Combinations of a Phone Number
 * ====================================
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * PROBLEM:
 *   Given a string of digits (2-9), return all possible letter
 *   combinations using the phone keypad mapping.
 *
 * EXAMPLES:
 *   solve("23") -> {"ad","ae","af","bd","be","bf","cd","ce","cf"}
 *   solve("")   -> {}
 *
 * CONSTRAINTS:
 *   - 0 <= digits.size() <= 4
 */

#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

vector<string> solve(string digits) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    string digits;
    getline(cin, digits);
    vector<string> result = solve(digits);
    for (auto& combo : result) cout << combo << endl;
    return 0;
}
