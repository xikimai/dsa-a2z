/*
 * Example 01: Binary Search -- Visual Walkthrough
 * =================================================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * This file demonstrates:
 *   Part 1: Linear search step count
 *   Part 2: Binary search step count
 *   Part 3: Side-by-side comparison
 *   Part 4: Binary search trace (showing lo, hi, mid each step)
 *
 * Build & run:
 *   g++ -std=c++17 -o example_01 code/cpp/ch09/learn/example_01_binary_search_visual.cpp && ./example_01
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
// 1. Linear Search -- count every step
// =====================================================================
// Idea: Check each element one by one from left to right.
// Time:  O(n)
// Space: O(1)

void demo_linear_search() {
    cout << "=== PART 1: Linear Search ===" << endl;

    vector<int> arr = {2, 5, 8, 12, 16, 23, 38, 42, 56, 72, 91};
    int target = 42;
    print_vec("Array: ", arr);
    cout << "  Target: " << target << endl;
    cout << endl;

    int steps = 0;
    int found_idx = -1;
    for (int i = 0; i < (int)arr.size(); i++) {
        steps++;
        cout << "  Step " << steps << ": check arr[" << i << "] = " << arr[i];
        if (arr[i] == target) {
            cout << "  <-- FOUND!" << endl;
            found_idx = i;
            break;
        }
        cout << endl;
    }

    cout << "  Result: index " << found_idx << " in " << steps << " steps" << endl;
    cout << endl;
}

// =====================================================================
// 2. Binary Search -- count every step
// =====================================================================
// Idea: Cut the search space in half each time.
//       Only works on SORTED arrays.
// Time:  O(log n)
// Space: O(1)

void demo_binary_search() {
    cout << "=== PART 2: Binary Search ===" << endl;

    vector<int> arr = {2, 5, 8, 12, 16, 23, 38, 42, 56, 72, 91};
    int target = 42;
    print_vec("Array: ", arr);
    cout << "  Target: " << target << endl;
    cout << endl;

    int lo = 0, hi = (int)arr.size() - 1;
    int steps = 0;
    int found_idx = -1;

    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        steps++;
        cout << "  Step " << steps << ": lo=" << lo << " hi=" << hi
             << " mid=" << mid << " arr[mid]=" << arr[mid];
        if (arr[mid] == target) {
            cout << "  <-- FOUND!" << endl;
            found_idx = mid;
            break;
        } else if (arr[mid] < target) {
            cout << "  -> go RIGHT" << endl;
            lo = mid + 1;
        } else {
            cout << "  -> go LEFT" << endl;
            hi = mid - 1;
        }
    }

    cout << "  Result: index " << found_idx << " in " << steps << " steps" << endl;
    cout << endl;
}

// =====================================================================
// 3. Side-by-Side Comparison -- how steps grow with n
// =====================================================================

int linear_search_count(const vector<int>& arr, int target) {
    int steps = 0;
    for (int i = 0; i < (int)arr.size(); i++) {
        steps++;
        if (arr[i] == target) return steps;
    }
    return steps;
}

int binary_search_count(const vector<int>& arr, int target) {
    int lo = 0, hi = (int)arr.size() - 1;
    int steps = 0;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        steps++;
        if (arr[mid] == target) return steps;
        else if (arr[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return steps;
}

void demo_comparison() {
    cout << "=== PART 3: Step Count Comparison ===" << endl;
    cout << "  Searching for the LAST element (worst case for linear):" << endl;
    cout << endl;

    vector<int> sizes = {10, 100, 1000, 10000, 100000};
    cout << "  n         Linear   Binary" << endl;
    cout << "  --------- ------   ------" << endl;

    for (int n : sizes) {
        // Build sorted array 1..n, search for n (last element)
        vector<int> arr(n);
        for (int i = 0; i < n; i++) arr[i] = i + 1;
        int target = n;

        int lin_steps = linear_search_count(arr, target);
        int bin_steps = binary_search_count(arr, target);

        cout << "  ";
        // Pad n to 9 chars
        string ns = to_string(n);
        cout << ns;
        for (int i = (int)ns.size(); i < 9; i++) cout << " ";
        cout << " ";
        // Pad linear to 6 chars
        string ls = to_string(lin_steps);
        cout << ls;
        for (int i = (int)ls.size(); i < 6; i++) cout << " ";
        cout << " ";
        cout << bin_steps << endl;
    }

    cout << endl;
    cout << "  Binary search is EXPONENTIALLY faster!" << endl;
    cout << "  Doubling n only adds 1 more step to binary search." << endl;
    cout << endl;
}

// =====================================================================
// 4. Binary Search Detailed Trace
// =====================================================================

void demo_trace() {
    cout << "=== PART 4: Binary Search Trace ===" << endl;

    vector<int> arr = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
    int target = 13;
    print_vec("Array: ", arr);
    cout << "  Target: " << target << endl;
    cout << endl;

    int lo = 0, hi = (int)arr.size() - 1;
    int step = 0;

    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        step++;

        // Print the array with markers
        cout << "  Step " << step << ":" << endl;
        cout << "    Values: ";
        for (int i = 0; i < (int)arr.size(); i++) {
            cout << arr[i] << " ";
        }
        cout << endl;

        // Print markers
        cout << "    Marks:  ";
        for (int i = 0; i < (int)arr.size(); i++) {
            if (i == mid) cout << "^ ";
            else if (i == lo) cout << "L ";
            else if (i == hi) cout << "H ";
            else {
                // Pad based on digit count
                int digits = (arr[i] >= 10) ? 2 : 1;
                for (int d = 0; d < digits; d++) cout << " ";
                cout << " ";
            }
        }
        cout << endl;

        cout << "    lo=" << lo << " hi=" << hi << " mid=" << mid
             << " arr[mid]=" << arr[mid];

        if (arr[mid] == target) {
            cout << " == target -> FOUND at index " << mid << endl;
            break;
        } else if (arr[mid] < target) {
            cout << " < target -> search right half" << endl;
            lo = mid + 1;
        } else {
            cout << " > target -> search left half" << endl;
            hi = mid - 1;
        }
        cout << endl;
    }
    cout << endl;
}

// =====================================================================
// main -- run all demos
// =====================================================================
int main() {
    cout << "Chapter 9: Binary Search -- Visual Walkthrough" << endl;
    cout << "===============================================" << endl << endl;

    demo_linear_search();
    demo_binary_search();
    demo_comparison();
    demo_trace();

    cout << "Key takeaways:" << endl;
    cout << "  - Linear search: O(n) -- checks every element" << endl;
    cout << "  - Binary search: O(log n) -- halves the search space each step" << endl;
    cout << "  - Binary search REQUIRES a sorted array" << endl;
    cout << "  - Use int mid = lo + (hi - lo) / 2 to avoid overflow" << endl;
    return 0;
}
