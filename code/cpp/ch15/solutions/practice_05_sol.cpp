/* Solution: Practice 5 — Dutch National Flag (Ch 15) */
#include <algorithm>
#include <vector>
using namespace std;
vector<int> solve(vector<int> arr) {
    if (arr.size() <= 1) return arr;
    int low = 0, mid = 0, high = (int)arr.size() - 1;
    while (mid <= high) {
        if (arr[mid] == 0) {
            swap(arr[low], arr[mid]);
            low++; mid++;
        } else if (arr[mid] == 1) {
            mid++;
        } else {
            swap(arr[mid], arr[high]);
            high--;
        }
    }
    return arr;
}
