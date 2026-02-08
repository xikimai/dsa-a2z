#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<long long> solve(vector<int> arr) {
    int n = arr.size();
    vector<long long> prefix(n + 1, 0);
    for (int i = 1; i <= n; i++) prefix[i] = prefix[i-1] + arr[i-1];
    return prefix;
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
