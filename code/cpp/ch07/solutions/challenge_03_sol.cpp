/*
 * Solution -- Challenge 3: GCD Pair Sum
 * =======================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * APPROACH: Brute force all n*(n-1)/2 pairs. Compute GCD of each pair
 *           using the Euclidean algorithm. Sum all GCDs.
 * TIME:  O(n^2 * log(max_val))
 * SPACE: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

long long solve(vector<int>& nums) {
    auto gcd = [](long long a, long long b) -> long long {
        while (b != 0) {
            long long t = b;
            b = a % b;
            a = t;
        }
        return a;
    };

    long long total = 0;
    int n = (int)nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            total += gcd(nums[i], nums[j]);
        }
    }
    return total;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    cout << solve(nums) << endl;
    return 0;
}
