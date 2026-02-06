/*
 * Solution for Warmup 05: Sum 1 to N
 * ====================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use a for loop to accumulate the sum from 1 to n.
 * (There's a formula n*(n+1)/2, but the point here is to practice loops.)
 *
 * TIME COMPLEXITY:  O(n) — loop runs n times
 * SPACE COMPLEXITY: O(1) — just one accumulator variable
 */

#include <iostream>
using namespace std;

int solve(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
