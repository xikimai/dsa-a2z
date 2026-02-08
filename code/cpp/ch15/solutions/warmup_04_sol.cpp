/* Solution: Warmup 4 — Move Zeros to End (Ch 15) */
#include <algorithm>
#include <vector>
using namespace std;
vector<int> solve(vector<int> arr) {
    int slow = 0;
    for (int fast = 0; fast < (int)arr.size(); fast++) {
        if (arr[fast] != 0) {
            swap(arr[slow], arr[fast]);
            slow++;
        }
    }
    return arr;
}
