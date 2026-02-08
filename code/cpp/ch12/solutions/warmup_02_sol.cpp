/*
 * Solution for Warmup 2: Count Set Bits (Brian Kernighan's)
 * TIME: O(k) where k = set bits   SPACE: O(1)
 */
#include <iostream>
using namespace std;

int solve(int n) {
    int count = 0;
    while (n) {
        n &= (n - 1);
        count++;
    }
    return count;
}

int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
