#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> prices) {
    if (prices.size() < 2) return 0;
    int minPrice = prices[0], maxProfit = 0;
    for (int i = 1; i < (int)prices.size(); i++) {
        maxProfit = max(maxProfit, prices[i] - minPrice);
        minPrice = min(minPrice, prices[i]);
    }
    return maxProfit;
}

int main() {
    int n; cin >> n;
    vector<int> prices(n); for (int i = 0; i < n; i++) cin >> prices[i];
    cout << solve(prices) << endl;
    return 0;
}
