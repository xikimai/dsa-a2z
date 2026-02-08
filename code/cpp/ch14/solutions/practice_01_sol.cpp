#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> arr) {
    int n = arr.size();
    vector<long long> prefix(n + 1, 0);
    for (int i = 0; i < n; i++) prefix[i+1] = prefix[i] + arr[i];
    long long total = prefix[n];
    for (int i = 0; i < n; i++) {
        if (prefix[i] == total - prefix[i+1]) return i;
    }
    return -1;
}

int main() {
    int n; cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << solve(arr) << endl;
    return 0;
}
