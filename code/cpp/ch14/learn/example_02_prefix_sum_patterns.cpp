/*
 * Example 02: Prefix Sum Patterns — 2D Prefix Sums and Kadane's
 * ==============================================================
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * Demonstrates:
 *   Part 1: 2D prefix sum construction and rectangle queries
 *   Part 2: Kadane's algorithm step-by-step trace
 *   Part 3: Prefix sum + hash map for subarray sum equals K
 */

#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int main() {
    // ── Part 1: 2D Prefix Sums ──
    cout << "=== Part 1: 2D Prefix Sums ===" << endl;
    vector<vector<int>> matrix = {{1,2,3},{4,5,6},{7,8,9}};
    int rows = matrix.size(), cols = matrix[0].size();

    vector<vector<long long>> prefix(rows+1, vector<long long>(cols+1, 0));
    for (int i = 1; i <= rows; i++)
        for (int j = 1; j <= cols; j++)
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + matrix[i-1][j-1];

    cout << "  Matrix:" << endl;
    for (auto& row : matrix) {
        cout << "    [";
        for (int j = 0; j < (int)row.size(); j++) cout << row[j] << (j < (int)row.size()-1 ? ", " : "");
        cout << "]" << endl;
    }

    long long sum = prefix[3][3] - prefix[1][3] - prefix[3][1] + prefix[1][1];
    cout << "  rect_sum(1,1 to 2,2) = " << sum << "  (verify: 5+6+8+9=28)" << endl << endl;

    // ── Part 2: Kadane's Trace ──
    cout << "=== Part 2: Kadane's Algorithm Trace ===" << endl;
    vector<int> arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << "  Input: [";
    for (int i = 0; i < (int)arr.size(); i++) cout << arr[i] << (i < (int)arr.size()-1 ? ", " : "");
    cout << "]" << endl;

    long long currentSum = arr[0], maxSum = arr[0];
    cout << "  i=0: current=" << currentSum << " max=" << maxSum << endl;
    for (int i = 1; i < (int)arr.size(); i++) {
        string action = (currentSum + arr[i] >= arr[i]) ? "extend" : "RESTART";
        currentSum = max(currentSum + arr[i], (long long)arr[i]);
        maxSum = max(maxSum, currentSum);
        cout << "  i=" << i << ": arr=" << arr[i] << " current=" << currentSum
             << " max=" << maxSum << " (" << action << ")" << endl;
    }
    cout << "  Answer: " << maxSum << endl << endl;

    // ── Part 3: Prefix Sum + Hash Map ──
    cout << "=== Part 3: Prefix Sum + Hash Map ===" << endl;
    vector<int> arr2 = {1, 2, 3, -2, 5};
    int k = 3;
    cout << "  arr=[1,2,3,-2,5], k=3" << endl;

    unordered_map<long long, int> prefixCount;
    prefixCount[0] = 1;
    long long runSum = 0;
    int count = 0;

    for (int i = 0; i < (int)arr2.size(); i++) {
        runSum += arr2[i];
        long long complement = runSum - k;
        int found = prefixCount.count(complement) ? prefixCount[complement] : 0;
        count += found;
        cout << "  i=" << i << " sum=" << runSum << " need=" << complement;
        if (found > 0) cout << " FOUND!";
        cout << " count=" << count << endl;
        prefixCount[runSum]++;
    }
    cout << "  Total subarrays with sum=" << k << ": " << count << endl;

    return 0;
}
