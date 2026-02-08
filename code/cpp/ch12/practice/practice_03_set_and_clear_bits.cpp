/*
 * Practice 3: Set and Clear Bits
 * Chapter 12: Bit Manipulation — The Language of Computers
 *
 * PROBLEM: Implement solve_set(n,i) and solve_clear(n,i).
 * EXAMPLES: solve_set(42,0)=43, solve_clear(42,1)=40
 * CONSTRAINTS: 0 <= n <= 10^9, 0 <= i <= 30
 */

#include <iostream>
#include <string>
using namespace std;

int solve_set(int n, int i) {
    // TODO: Replace this with your solution
    return 0;
}

int solve_clear(int n, int i) {
    // TODO: Replace this with your solution
    return 0;
}

int main() {
    string op;
    int n, i;
    cin >> op >> n >> i;
    if (op == "set") cout << solve_set(n, i) << endl;
    else cout << solve_clear(n, i) << endl;
    return 0;
}
