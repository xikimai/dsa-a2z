/*
 * Solution -- Challenge 3: Sort by Frequency
 * ============================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * APPROACH: Count frequencies with unordered_map, then sort with
 *           a custom comparator: higher frequency first, then
 *           smaller value first for ties.
 * TIME:  O(n log n)
 * SPACE: O(n) for the frequency map
 */

#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr) {
    unordered_map<int, int> freq;
    for (int x : arr) freq[x]++;

    sort(arr.begin(), arr.end(), [&freq](int a, int b) {
        if (freq[a] != freq[b]) return freq[a] > freq[b];
        return a < b;
    });
    return arr;
}

// -- Do not change anything below this line --------------------------
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
