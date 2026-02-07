/*
 * Solution -- Practice 2: GCD and LCM
 * =====================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * APPROACH: Euclidean algorithm for GCD. LCM = a / gcd * b (divide first
 *           to avoid overflow). If either is 0, LCM is 0.
 * TIME:  O(log(min(a, b)))
 * SPACE: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

vector<long long> solve(long long a, long long b) {
    // Euclidean GCD
    long long x = a, y = b;
    while (y != 0) {
        long long temp = y;
        y = x % y;
        x = temp;
    }
    long long g = x;

    // LCM: divide first to avoid overflow
    long long lcm = (g == 0) ? 0 : a / g * b;

    return {g, lcm};
}

// -- Do not change anything below this line --------------------------
int main() {
    long long a, b;
    cin >> a >> b;
    vector<long long> result = solve(a, b);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}
