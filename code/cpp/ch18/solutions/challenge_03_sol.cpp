#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> arrivals, vector<int> departures) {
    if (arrivals.empty()) return 0;
    sort(arrivals.begin(), arrivals.end());
    sort(departures.begin(), departures.end());
    int plat = 0, maxPlat = 0;
    int i = 0, j = 0, n = arrivals.size();
    while (i < n) {
        if (arrivals[i] <= departures[j]) {
            plat++; maxPlat = max(maxPlat, plat); i++;
        } else {
            plat--; j++;
        }
    }
    return maxPlat;
}

int main() {
    int n; cin >> n;
    vector<int> arr(n), dep(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 0; i < n; i++) cin >> dep[i];
    cout << solve(arr, dep) << endl;
    return 0;
}
