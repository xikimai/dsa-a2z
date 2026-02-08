#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> greed, vector<int> cookies) {
    sort(greed.begin(), greed.end());
    sort(cookies.begin(), cookies.end());
    int child = 0, cookie = 0;
    while (child < (int)greed.size() && cookie < (int)cookies.size()) {
        if (cookies[cookie] >= greed[child]) child++;
        cookie++;
    }
    return child;
}

int main() {
    int n, m; cin >> n;
    vector<int> greed(n); for (int i = 0; i < n; i++) cin >> greed[i];
    cin >> m;
    vector<int> cookies(m); for (int i = 0; i < m; i++) cin >> cookies[i];
    cout << solve(greed, cookies) << endl;
    return 0;
}
