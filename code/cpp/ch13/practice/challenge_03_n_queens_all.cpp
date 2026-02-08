/*
 * Challenge 3: N-Queens All Solutions
 * ====================================
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * PROBLEM:
 *   Return all distinct N-Queens solutions. Each solution is a
 *   vector of strings where 'Q' marks a queen and '.' marks empty.
 *   Sort solutions lexicographically.
 *
 * CONSTRAINTS:
 *   - 1 <= n <= 9
 */

#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

vector<vector<string>> solve(int n) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<vector<string>> result = solve(n);
    for (auto& sol : result) {
        for (auto& row : sol) cout << row << endl;
        cout << endl;
    }
    return 0;
}
