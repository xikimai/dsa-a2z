#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

long long solve(vector<int> arr) {
    if (arr.empty()) return 0;
    long long currentSum = arr[0], maxSum = arr[0];
    for (int i = 1; i < (int)arr.size(); i++) {
        currentSum = max(currentSum + arr[i], (long long)arr[i]);
        maxSum = max(maxSum, currentSum);
    }
    return maxSum;
}

int main() {
    int n; cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << solve(arr) << endl;
    return 0;
}
