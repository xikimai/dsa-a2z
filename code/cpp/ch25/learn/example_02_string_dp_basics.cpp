/*
 * Example 02: String DP Basics — LCS and Edit Distance
 * ======================================================
 * Chapter 25: Dynamic Programming III — Subsequences & Knapsack
 *
 * Demonstrates LCS and Edit Distance with space optimization.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int lcs(const string& a, const string& b) {
    int m = a.size(), n = b.size();
    vector<int> prev(n + 1, 0);
    for (int i = 1; i <= m; i++) {
        vector<int> curr(n + 1, 0);
        for (int j = 1; j <= n; j++) {
            if (a[i-1] == b[j-1]) curr[j] = prev[j-1] + 1;
            else curr[j] = max(prev[j], curr[j-1]);
        }
        prev = curr;
    }
    return prev[n];
}

int editDistance(const string& a, const string& b) {
    int m = a.size(), n = b.size();
    vector<int> prev(n + 1);
    for (int j = 0; j <= n; j++) prev[j] = j;
    for (int i = 1; i <= m; i++) {
        vector<int> curr(n + 1);
        curr[0] = i;
        for (int j = 1; j <= n; j++) {
            if (a[i-1] == b[j-1]) curr[j] = prev[j-1];
            else curr[j] = 1 + min({prev[j], curr[j-1], prev[j-1]});
        }
        prev = curr;
    }
    return prev[n];
}

int main() {
    cout << "LCS('abcde', 'ace') = " << lcs("abcde", "ace") << endl;
    cout << "Edit Distance('horse', 'ros') = " << editDistance("horse", "ros") << endl;
    return 0;
}
