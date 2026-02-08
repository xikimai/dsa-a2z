#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<long long> solve(vector<int> arr) {
    int n = arr.size();
    vector<long long> result(n, 1);
    long long left = 1;
    for (int i = 0; i < n; i++) { result[i] = left; left *= arr[i]; }
    long long right = 1;
    for (int i = n-1; i >= 0; i--) { result[i] *= right; right *= arr[i]; }
    return result;
}

int main() {
    int n; cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    auto result = solve(arr);
    for (int i = 0; i < (int)result.size(); i++)
        cout << result[i] << (i < (int)result.size()-1 ? " " : "\n");
    return 0;
}
