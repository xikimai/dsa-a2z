/*
 * Solution -- Warmup 4: Sum of 1 to N
 * =====================================
 * Chapter 6: How Fast Is Your Code?
 *
 * APPROACH:
 *   Compute the same sum three ways:
 *     1. loop:    O(n) accumulation
 *     2. formula: O(1) using n*(n+1)/2
 *     3. nested:  O(n^2) nested loops
 *
 * TIME COMPLEXITY:  O(n^2) due to the nested approach
 * SPACE COMPLEXITY: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(int n) {
    // Method 1: loop
    int loop_sum = 0;
    for (int i = 1; i <= n; i++) {
        loop_sum += i;
    }

    // Method 2: formula
    int formula_sum = n * (n + 1) / 2;

    // Method 3: nested loops
    int nested_sum = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            nested_sum += 1;
        }
    }

    return {loop_sum, formula_sum, nested_sum};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> result = solve(n);
    cout << result[0] << " " << result[1] << " " << result[2] << endl;
    return 0;
}
