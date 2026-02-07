/*
 * Example 02: Rotated Arrays -- Rotation, Min, Search, Peak
 * ===========================================================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * This file demonstrates:
 *   Part 1: What is a rotated sorted array?
 *   Part 2: Finding the minimum in a rotated array (trace)
 *   Part 3: Searching in a rotated array (trace)
 *   Part 4: Finding a peak element (trace)
 *
 * Build & run:
 *   g++ -std=c++17 -o example_02 code/cpp/ch09/learn/example_02_rotated_arrays.cpp && ./example_02
 */

#include <iostream>
#include <vector>
using namespace std;

// Helper: print a vector with an optional label
void print_vec(const string& label, const vector<int>& v) {
    cout << "  " << label << " [";
    for (int i = 0; i < (int)v.size(); i++) {
        if (i > 0) cout << ", ";
        cout << v[i];
    }
    cout << "]" << endl;
}

// =====================================================================
// 1. What is a rotated sorted array?
// =====================================================================

void demo_rotation() {
    cout << "=== PART 1: Rotated Sorted Arrays ===" << endl;

    vector<int> original = {0, 1, 2, 3, 4, 5, 6, 7};
    print_vec("Original sorted: ", original);
    cout << endl;

    // Show rotations
    for (int k = 0; k <= 4; k++) {
        vector<int> rotated(original.size());
        int n = (int)original.size();
        for (int i = 0; i < n; i++) {
            rotated[i] = original[(i + k) % n];
        }
        cout << "  Rotated by " << k << ": [";
        for (int i = 0; i < n; i++) {
            if (i > 0) cout << ", ";
            cout << rotated[i];
        }
        cout << "]" << endl;
    }

    cout << endl;
    cout << "  Notice: A rotated sorted array has TWO sorted halves." << endl;
    cout << "  The 'pivot' is where the larger half ends and smaller begins." << endl;
    cout << endl;
}

// =====================================================================
// 2. Finding minimum in a rotated sorted array (trace)
// =====================================================================

void demo_find_min() {
    cout << "=== PART 2: Find Minimum in Rotated Array ===" << endl;

    vector<int> arr = {4, 5, 6, 7, 0, 1, 2};
    print_vec("Array: ", arr);
    cout << endl;

    int lo = 0, hi = (int)arr.size() - 1;
    int step = 0;

    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        step++;
        cout << "  Step " << step << ": lo=" << lo << " hi=" << hi
             << " mid=" << mid << " arr[mid]=" << arr[mid]
             << " arr[hi]=" << arr[hi];

        if (arr[mid] > arr[hi]) {
            // Minimum is in the right half
            cout << "  -> arr[mid] > arr[hi], go RIGHT" << endl;
            lo = mid + 1;
        } else {
            // Minimum is in the left half (including mid)
            cout << "  -> arr[mid] <= arr[hi], go LEFT (keep mid)" << endl;
            hi = mid;
        }
    }

    cout << "  Minimum found: arr[" << lo << "] = " << arr[lo] << endl;
    cout << endl;

    cout << "  Key insight: Compare arr[mid] with arr[hi]." << endl;
    cout << "  If arr[mid] > arr[hi], the min must be on the right." << endl;
    cout << "  Otherwise, the min is on the left (including mid)." << endl;
    cout << endl;
}

// =====================================================================
// 3. Searching in a rotated sorted array (trace)
// =====================================================================

void demo_search_rotated() {
    cout << "=== PART 3: Search in Rotated Array ===" << endl;

    vector<int> arr = {4, 5, 6, 7, 0, 1, 2};
    int target = 0;
    print_vec("Array: ", arr);
    cout << "  Target: " << target << endl;
    cout << endl;

    int lo = 0, hi = (int)arr.size() - 1;
    int step = 0;

    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        step++;
        cout << "  Step " << step << ": lo=" << lo << " hi=" << hi
             << " mid=" << mid << " arr[mid]=" << arr[mid];

        if (arr[mid] == target) {
            cout << "  <-- FOUND at index " << mid << endl;
            break;
        }

        // Determine which half is sorted
        if (arr[lo] <= arr[mid]) {
            // Left half is sorted
            cout << "  left half sorted [" << arr[lo] << ".." << arr[mid] << "]";
            if (target >= arr[lo] && target < arr[mid]) {
                cout << " -> target in left" << endl;
                hi = mid - 1;
            } else {
                cout << " -> target in right" << endl;
                lo = mid + 1;
            }
        } else {
            // Right half is sorted
            cout << "  right half sorted [" << arr[mid] << ".." << arr[hi] << "]";
            if (target > arr[mid] && target <= arr[hi]) {
                cout << " -> target in right" << endl;
                lo = mid + 1;
            } else {
                cout << " -> target in left" << endl;
                hi = mid - 1;
            }
        }
    }
    cout << endl;
}

// =====================================================================
// 4. Finding a peak element (trace)
// =====================================================================

void demo_find_peak() {
    cout << "=== PART 4: Find Peak Element ===" << endl;

    vector<int> arr = {1, 2, 1, 3, 5, 6, 4};
    print_vec("Array: ", arr);
    cout << endl;

    cout << "  A 'peak' is any element greater than its neighbors." << endl;
    cout << "  arr[-1] and arr[n] are treated as -infinity." << endl;
    cout << endl;

    int lo = 0, hi = (int)arr.size() - 1;
    int step = 0;

    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        step++;
        cout << "  Step " << step << ": lo=" << lo << " hi=" << hi
             << " mid=" << mid << " arr[mid]=" << arr[mid]
             << " arr[mid+1]=" << arr[mid + 1];

        if (arr[mid] < arr[mid + 1]) {
            cout << "  -> rising, peak is to the RIGHT" << endl;
            lo = mid + 1;
        } else {
            cout << "  -> falling, peak is to the LEFT (or here)" << endl;
            hi = mid;
        }
    }

    cout << "  Peak found: arr[" << lo << "] = " << arr[lo] << endl;
    cout << endl;

    cout << "  Key insight: If arr[mid] < arr[mid+1], we're on a rising slope," << endl;
    cout << "  so a peak must exist to the right. Otherwise, to the left." << endl;
    cout << "  This guarantees O(log n) -- we always find SOME peak." << endl;
    cout << endl;
}

// =====================================================================
// main -- run all demos
// =====================================================================
int main() {
    cout << "Chapter 9: Rotated Arrays and Peak Finding" << endl;
    cout << "===========================================" << endl << endl;

    demo_rotation();
    demo_find_min();
    demo_search_rotated();
    demo_find_peak();

    cout << "Key takeaways:" << endl;
    cout << "  - Rotated arrays have two sorted halves" << endl;
    cout << "  - Find min: compare arr[mid] with arr[hi]" << endl;
    cout << "  - Search rotated: figure out which half is sorted first" << endl;
    cout << "  - Peak finding: follow the rising slope" << endl;
    cout << "  - ALL of these run in O(log n)!" << endl;
    return 0;
}
