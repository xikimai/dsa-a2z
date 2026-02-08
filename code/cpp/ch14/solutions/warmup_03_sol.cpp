#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<long long> solve(vector<int> arr) {
    if (arr.empty()) return {};
    vector<long long> result(arr.size());
    result[0] = arr[0];
    for (int i = 1; i < (int)arr.size(); i++) result[i] = result[i-1] + arr[i];
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
