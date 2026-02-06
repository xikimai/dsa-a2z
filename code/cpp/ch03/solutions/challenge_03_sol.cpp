/*
 * Solution for Challenge 03: Collatz Sequence
 * =============================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Start with n. While n != 1:
 *   - If n is even, n = n / 2
 *   - If n is odd, n = 3 * n + 1
 * Record each value (including the starting value and the final 1).
 *
 * The Collatz conjecture says this always reaches 1, but nobody has
 * proven it! It's one of the great unsolved problems in mathematics.
 *
 * TIME COMPLEXITY:  O(?) — unknown! No one has proven an upper bound
 * SPACE COMPLEXITY: O(k) — where k is the length of the sequence
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(int n) {
    vector<int> sequence;
    sequence.push_back(n);
    while (n != 1) {
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
        sequence.push_back(n);
    }
    return sequence;
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
