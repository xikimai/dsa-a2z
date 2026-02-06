/*
 * Solution for Warmup 04: Count Down
 * ====================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use a for loop counting from n down to 1, pushing each value
 * into a vector.
 *
 * TIME COMPLEXITY:  O(n) — loop runs n times
 * SPACE COMPLEXITY: O(n) — for the result vector
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(int n) {
    vector<int> result;
    for (int i = n; i >= 1; i--) {
        result.push_back(i);
    }
    return result;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    vector<int> result = solve(n);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
