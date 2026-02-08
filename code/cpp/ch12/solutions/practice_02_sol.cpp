/*
 * Solution for Practice 2: Toggle i-th Bit
 * TIME: O(1)   SPACE: O(1)
 */
#include <iostream>
using namespace std;

int solve(int n, int i) {
    return n ^ (1 << i);
}

int main() {
    int n, i;
    cin >> n >> i;
    cout << solve(n, i) << endl;
    return 0;
}
