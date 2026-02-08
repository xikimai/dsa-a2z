/*
 * Solution for Warmup 3: Check Power of Two
 * TIME: O(1)   SPACE: O(1)
 */
#include <iostream>
using namespace std;

bool solve(int n) {
    return n > 0 && (n & (n - 1)) == 0;
}

int main() {
    int n;
    cin >> n;
    cout << (solve(n) ? "true" : "false") << endl;
    return 0;
}
