/*
 * Solution for Practice 4: Letter Combinations of a Phone Number
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * APPROACH: Backtrack through digits, appending mapped letters.
 * TIME:  O(4^n)
 * SPACE: O(n)
 */

#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

vector<string> solve(string digits) {
    if (digits.empty()) return {};

    unordered_map<char, string> mapping = {
        {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"},
        {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}
    };

    vector<string> result;

    function<void(int, string)> backtrack = [&](int index, string current) {
        if (index == (int)digits.size()) {
            result.push_back(current);
            return;
        }
        for (char letter : mapping[digits[index]]) {
            backtrack(index + 1, current + letter);
        }
    };

    backtrack(0, "");
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    string digits;
    getline(cin, digits);
    vector<string> result = solve(digits);
    for (auto& combo : result) cout << combo << endl;
    return 0;
}
