/*
 * Solution for Warmup 4: Check if i-th Bit Is Set
 * TIME: O(1)   SPACE: O(1)
 */
#include <iostream>
using namespace std;

bool solve(int n, int i) {
    return (n >> i) & 1;
}

int main() {
    int n, i;
    cin >> n >> i;
    cout << (solve(n, i) ? "true" : "false") << endl;
    return 0;
}
