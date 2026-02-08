/* Solution: Warmup 2 — Remove Duplicates from Sorted (Ch 15) */
#include <vector>
using namespace std;
vector<int> solve(vector<int> arr) {
    if (arr.size() <= 1) return arr;
    int slow = 0;
    for (int fast = 1; fast < (int)arr.size(); fast++) {
        if (arr[fast] != arr[slow]) {
            slow++;
            arr[slow] = arr[fast];
        }
    }
    return vector<int>(arr.begin(), arr.begin() + slow + 1);
}
