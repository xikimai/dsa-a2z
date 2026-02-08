/*
 * Example 01: Two-Pointer Basics
 * ===============================
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * Demonstrates converging two pointers and same-direction pointers.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Part 1: Converging two pointers — pair sum
    cout << "=== Part 1: Converging Two Pointers ===" << endl;
    vector<int> arr = {1, 3, 5, 8, 12, 15, 20};
    int target = 13;

    int left = 0, right = (int)arr.size() - 1;
    while (left < right) {
        int sum = arr[left] + arr[right];
        cout << "  arr[" << left << "]=" << arr[left]
             << " + arr[" << right << "]=" << arr[right]
             << " = " << sum;
        if (sum == target) {
            cout << "  FOUND!" << endl;
            break;
        } else if (sum < target) {
            cout << "  < " << target << " -> move left right" << endl;
            left++;
        } else {
            cout << "  > " << target << " -> move right left" << endl;
            right--;
        }
    }

    // Part 2: Same-direction pointers — move zeros
    cout << "\n=== Part 2: Same-Direction Pointers ===" << endl;
    vector<int> zeros = {0, 1, 0, 3, 12, 0, 5};
    cout << "Input: ";
    for (int x : zeros) cout << x << " ";
    cout << endl;

    int slow = 0;
    for (int fast = 0; fast < (int)zeros.size(); fast++) {
        if (zeros[fast] != 0) {
            swap(zeros[slow], zeros[fast]);
            slow++;
        }
    }

    cout << "Result: ";
    for (int x : zeros) cout << x << " ";
    cout << endl << "All zeros moved to the end!" << endl;

    return 0;
}
