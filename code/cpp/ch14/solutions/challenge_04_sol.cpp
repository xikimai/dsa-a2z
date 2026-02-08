#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

long long solve(vector<int> arr) {
    sort(arr.begin(), arr.end());
    int n = arr.size();
    if (n <= 1) return 0;
    vector<long long> prefix(n + 1, 0);
    for (int i = 0; i < n; i++) prefix[i+1] = prefix[i] + arr[i];
    long long minCost = LLONG_MAX;
    for (int i = 0; i < n; i++) {
        long long leftCost = (long long)i * arr[i] - prefix[i];
        long long rightCost = (prefix[n] - prefix[i+1]) - (long long)(n-i-1) * arr[i];
        minCost = min(minCost, leftCost + rightCost);
    }
    return minCost;
}

int main() {
    int n; cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << solve(arr) << endl;
    return 0;
}
