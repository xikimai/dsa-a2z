/*
 * Challenge 3: GCD Pair Sum
 * =========================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * PROBLEM:
 *   Given a vector of positive integers, return the sum of
 *   gcd(nums[i], nums[j]) for all pairs where i < j.
 *
 * EXAMPLES:
 *   solve([2, 4, 6])     -> 6   (gcd(2,4)=2 + gcd(2,6)=2 + gcd(4,6)=2)
 *   solve([3, 6, 9])     -> 9   (gcd(3,6)=3 + gcd(3,9)=3 + gcd(6,9)=3)
 *   solve([12, 18, 24])  -> 24  (gcd(12,18)=6 + gcd(12,24)=12 + gcd(18,24)=6)
 *   solve([7])            -> 0   (no pairs)
 *   solve([2, 3, 5, 7])  -> 6   (all gcds are 1, 6 pairs)
 *
 * CONSTRAINTS:
 *   1 <= nums.size() <= 1000
 *   1 <= nums[i] <= 10^9
 *
 * INSTRUCTIONS:
 *   Replace "return 0;" with your solution.
 *   Hint: Use the Euclidean GCD for each pair. O(n^2 * log(max)) is fine.
 */

#include <iostream>
#include <vector>
using namespace std;

long long solve(vector<int>& nums) {
    // TODO: Replace this with your solution
    return 0;
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
