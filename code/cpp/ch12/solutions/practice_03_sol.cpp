/*
 * Solution for Practice 3: Set and Clear Bits
 * TIME: O(1)   SPACE: O(1)
 */
#include <iostream>
#include <string>
using namespace std;

int solve_set(int n, int i) {
    return n | (1 << i);
}

int solve_clear(int n, int i) {
    return n & ~(1 << i);
}

int main() {
    string op;
    int n, i;
    cin >> op >> n >> i;
    if (op == "set") cout << solve_set(n, i) << endl;
    else cout << solve_clear(n, i) << endl;
    return 0;
}
