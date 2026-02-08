/*
 * Warmup 4: Move Zeros to End
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * PROBLEM: Move all zeros to end, maintaining order of non-zero elements.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return arr;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<int> result = solve(arr);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
