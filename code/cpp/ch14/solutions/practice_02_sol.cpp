#include <algorithm>
#include <climits>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int solve(vector<int> arr, int k) {
    unordered_map<long long, int> prefixCount;
    prefixCount[0] = 1;
    long long currentSum = 0;
    int count = 0;
    for (int x : arr) {
        currentSum += x;
        long long complement = currentSum - k;
        if (prefixCount.count(complement)) count += prefixCount[complement];
        prefixCount[currentSum]++;
    }
    return count;
}

int main() {
    int n, k;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cin >> k;
    cout << solve(arr, k) << endl;
    return 0;
}
