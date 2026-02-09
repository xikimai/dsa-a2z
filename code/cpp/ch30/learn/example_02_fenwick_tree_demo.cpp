/*
 * Example 02: Fenwick Tree (BIT) Demo
 * Chapter 30: Segment Trees & Range Queries
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<int> bit;
int n;

void update(int i, int delta) {
    for (; i <= n; i += i & (-i)) bit[i] += delta;
}

int prefixSum(int i) {
    int sum = 0;
    for (; i > 0; i -= i & (-i)) sum += bit[i];
    return sum;
}

int rangeSum(int l, int r) {
    return prefixSum(r) - prefixSum(l - 1);
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    n = arr.size();
    bit.assign(n + 1, 0);
    for (int i = 0; i < n; i++) update(i + 1, arr[i]);

    cout << "Fenwick Tree Demo" << endl;
    cout << "Prefix(3) = " << prefixSum(3) << endl; // 6
    cout << "Range(2,4) = " << rangeSum(2, 4) << endl; // 9
    update(3, 5);
    cout << "After adding 5 to index 3:" << endl;
    cout << "Prefix(3) = " << prefixSum(3) << endl; // 11
    return 0;
}
