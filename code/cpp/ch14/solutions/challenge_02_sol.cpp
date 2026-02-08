#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

long long solve_brute(vector<int> arr) {
    if (arr.empty()) return 0;
    long long mx = arr[0]; int n = arr.size();
    for (int l = 0; l < n; l++)
        for (int r = l; r < n; r++) {
            long long t = 0;
            for (int k = l; k <= r; k++) t += arr[k];
            mx = max(mx, t);
        }
    return mx;
}

long long solve_prefix(vector<int> arr) {
    if (arr.empty()) return 0;
    int n = arr.size();
    vector<long long> prefix(n+1, 0);
    for (int i = 0; i < n; i++) prefix[i+1] = prefix[i] + arr[i];
    long long mx = arr[0];
    for (int l = 0; l < n; l++)
        for (int r = l; r < n; r++)
            mx = max(mx, prefix[r+1] - prefix[l]);
    return mx;
}

long long solve_kadane(vector<int> arr) {
    if (arr.empty()) return 0;
    long long cur = arr[0], mx = arr[0];
    for (int i = 1; i < (int)arr.size(); i++) {
        cur = max(cur + arr[i], (long long)arr[i]);
        mx = max(mx, cur);
    }
    return mx;
}

int main() {
    int n; cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << "brute=" << solve_brute(arr) << " prefix=" << solve_prefix(arr)
         << " kadane=" << solve_kadane(arr) << endl;
    return 0;
}
