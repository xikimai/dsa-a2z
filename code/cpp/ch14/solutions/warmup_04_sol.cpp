#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

bool solve(vector<int> arr1, vector<int> arr2) {
    if (arr1.size() > arr2.size()) return false;
    for (int i = 0; i < (int)arr1.size(); i++) if (arr1[i] != arr2[i]) return false;
    return true;
}

int main() {
    int n1, n2;
    cin >> n1;
    vector<int> arr1(n1);
    for (int i = 0; i < n1; i++) cin >> arr1[i];
    cin >> n2;
    vector<int> arr2(n2);
    for (int i = 0; i < n2; i++) cin >> arr2[i];
    cout << (solve(arr1, arr2) ? "true" : "false") << endl;
    return 0;
}
