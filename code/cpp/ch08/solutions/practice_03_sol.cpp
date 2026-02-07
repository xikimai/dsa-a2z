/*
 * Solution -- Practice 3: Dutch National Flag
 * =============================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * APPROACH: Three pointers (low, mid, high).
 *   - 0s go to [0..low-1], 1s to [low..high], 2s to [high+1..n-1]
 *   - If arr[mid]==0: swap with low, advance both
 *   - If arr[mid]==1: just advance mid
 *   - If arr[mid]==2: swap with high, shrink high
 * TIME:  O(n)
 * SPACE: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr) {
    int low = 0, mid = 0, high = (int)arr.size() - 1;
    while (mid <= high) {
        if (arr[mid] == 0) {
            swap(arr[low], arr[mid]);
            low++;
            mid++;
        } else if (arr[mid] == 1) {
            mid++;
        } else {
            swap(arr[mid], arr[high]);
            high--;
        }
    }
    return arr;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<int> result = solve(arr);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
