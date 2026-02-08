/*
 * Solution for Practice 3: Decode Ways
 * Chapter 23: Dynamic Programming I — The Foundation
 */

#include <algorithm>
#include <climits>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(string s) {
    if (s.empty() || s[0] == '0') return 0;
    int n = s.size();
    int prev2 = 1, prev1 = 1;
    for (int i = 2; i <= n; i++) {
        int c = 0;
        if (s[i-1] != '0') c += prev1;
        int td = stoi(s.substr(i-2, 2));
        if (td >= 10 && td <= 26) c += prev2;
        prev2 = prev1; prev1 = c;
    }
    return prev1;
}

int main() {
    return 0;
}
