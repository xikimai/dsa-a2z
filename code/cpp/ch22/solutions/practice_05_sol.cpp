/*
 * Solution for Practice 5: Remove All Adjacent Duplicates in String
 * Chapter 22: Stacks & Queues — Order Matters
 * APPROACH: Stack — push chars, pop when top matches current.
 * TIME: O(n), SPACE: O(n)
 */
#include <iostream>
#include <string>
using namespace std;

string solve(string s) {
    string stack; // use string as stack for easy conversion
    for (char ch : s) {
        if (!stack.empty() && stack.back() == ch) {
            stack.pop_back();
        } else {
            stack.push_back(ch);
        }
    }
    return stack;
}

int main() {
    string s;
    cin >> s;
    cout << solve(s) << endl;
    return 0;
}
