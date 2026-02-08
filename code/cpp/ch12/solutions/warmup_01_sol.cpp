/*
 * Solution for Warmup 1: Binary Representation
 * TIME: O(log n)   SPACE: O(log n)
 */
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

string solve(int n) {
    if (n == 0) return "0";
    string bits;
    while (n > 0) {
        bits += char('0' + n % 2);
        n /= 2;
    }
    reverse(bits.begin(), bits.end());
    return bits;
}

int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
