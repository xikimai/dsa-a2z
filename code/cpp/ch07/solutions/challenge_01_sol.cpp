/*
 * Solution -- Challenge 1: GCD Three Ways
 * =========================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * Three GCD implementations:
 *   1. solve_subtract -- Repeated subtraction. O(max(a,b)) worst case.
 *   2. solve_euclidean -- Euclidean algorithm. O(log(min(a,b))).
 *   3. solve_extended -- Extended Euclidean. Returns {gcd, x, y}
 *      such that a*x + b*y = gcd. O(log(min(a,b))).
 *
 * TIME:  O(log(min(a,b))) for Euclidean and Extended
 * SPACE: O(1) for subtract and euclidean, O(log(min(a,b))) for extended (recursion)
 */

#include <iostream>
#include <vector>
using namespace std;

long long solve_subtract(long long a, long long b) {
    if (a == 0) return b;
    if (b == 0) return a;
    while (a != b) {
        if (a > b) a -= b;
        else b -= a;
    }
    return a;
}

long long solve_euclidean(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

vector<long long> solve_extended(long long a, long long b) {
    if (b == 0) return {a, 1, 0};
    auto r = solve_extended(b, a % b);
    long long x = r[2];
    long long y = r[1] - (a / b) * r[2];
    return {r[0], x, y};
}

long long solve(long long a, long long b) {
    return solve_euclidean(a, b);
}

// -- Do not change anything below this line --------------------------
int main() {
    long long a, b;
    cin >> a >> b;
    cout << "subtract:  " << solve_subtract(a, b) << endl;
    cout << "euclidean: " << solve_euclidean(a, b) << endl;
    vector<long long> ext = solve_extended(a, b);
    cout << "extended:  gcd=" << ext[0]
         << " x=" << ext[1] << " y=" << ext[2] << endl;
    return 0;
}
