/*
 * Tests for Chapter 9: Finding Needles -- The Power of Searching
 * Build: g++ -std=c++17 -o /tmp/test_ch09 code/cpp/ch09/tests/test_ch09.cpp && /tmp/test_ch09
 */

#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named to avoid collisions)
// =====================================================================

// --- W1: Linear Search ---
int solve_linear_search(vector<int> arr, int target) {
    for (int i = 0; i < (int)arr.size(); i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}

// --- W2: Binary Search ---
int solve_binary_search(vector<int> arr, int target) {
    int lo = 0, hi = (int)arr.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}

// --- W3: First Occurrence ---
int solve_first_occurrence(vector<int> arr, int target) {
    int lo = 0, hi = (int)arr.size() - 1;
    int result = -1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) {
            result = mid;
            hi = mid - 1;
        } else if (arr[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return result;
}

// --- W4: Last Occurrence ---
int solve_last_occurrence(vector<int> arr, int target) {
    int lo = 0, hi = (int)arr.size() - 1;
    int result = -1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) {
            result = mid;
            lo = mid + 1;
        } else if (arr[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return result;
}

// --- W5: Count Occurrences ---
int solve_count_occurrences(vector<int> arr, int target) {
    int first = solve_first_occurrence(arr, target);
    if (first == -1) return 0;
    int last = solve_last_occurrence(arr, target);
    return last - first + 1;
}

// --- P1: Lower Bound ---
int solve_lower_bound(vector<int> arr, int target) {
    int lo = 0, hi = (int)arr.size();
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] >= target) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    return lo;
}

// --- P2: Upper Bound ---
int solve_upper_bound(vector<int> arr, int target) {
    int lo = 0, hi = (int)arr.size();
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] > target) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    return lo;
}

// --- P3: Floor and Ceil ---
vector<int> solve_floor_ceil(vector<int> arr, int target) {
    int n = (int)arr.size();
    int floor_val = -1, ceil_val = -1;

    {
        int lo = 0, hi = n - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] <= target) {
                floor_val = arr[mid];
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
    }

    {
        int lo = 0, hi = n - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] >= target) {
                ceil_val = arr[mid];
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
    }

    return {floor_val, ceil_val};
}

// --- P4: Search in Rotated Sorted Array ---
int solve_search_rotated(vector<int> arr, int target) {
    int lo = 0, hi = (int)arr.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) return mid;

        if (arr[lo] <= arr[mid]) {
            if (target >= arr[lo] && target < arr[mid]) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        } else {
            if (target > arr[mid] && target <= arr[hi]) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
    }
    return -1;
}

// --- P5: Find Minimum in Rotated Sorted Array ---
int solve_min_rotated(vector<int> arr) {
    int lo = 0, hi = (int)arr.size() - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] > arr[hi]) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return arr[lo];
}

// --- C1: Find Peak Element ---
int solve_peak_linear(vector<int> arr) {
    int n = (int)arr.size();
    if (n == 1) return 0;
    for (int i = 0; i < n; i++) {
        bool leftOk = (i == 0) || (arr[i] > arr[i - 1]);
        bool rightOk = (i == n - 1) || (arr[i] > arr[i + 1]);
        if (leftOk && rightOk) return i;
    }
    return 0;
}

int solve_peak_binary(vector<int> arr) {
    int lo = 0, hi = (int)arr.size() - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] < arr[mid + 1]) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return lo;
}

int solve_peak(vector<int> arr) {
    return solve_peak_binary(arr);
}

// --- C2: Single Element in Sorted Array ---
int solve_single_element(vector<int> arr) {
    int n = (int)arr.size();
    if (n == 1) return arr[0];

    int lo = 0, hi = n - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (mid % 2 == 1) mid--;

        if (arr[mid] == arr[mid + 1]) {
            lo = mid + 2;
        } else {
            hi = mid;
        }
    }
    return arr[lo];
}

// --- C3: Search in Rotated Sorted Array II (with duplicates) ---
bool solve_rotated_search_ii(vector<int> arr, int target) {
    int lo = 0, hi = (int)arr.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) return true;

        if (arr[lo] == arr[mid] && arr[mid] == arr[hi]) {
            lo++;
            hi--;
            continue;
        }

        if (arr[lo] <= arr[mid]) {
            if (target >= arr[lo] && target < arr[mid]) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        } else {
            if (target > arr[mid] && target <= arr[hi]) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
    }
    return false;
}

// =====================================================================
// is_peak helper for C1 validation
// =====================================================================
bool is_peak(const vector<int>& arr, int idx) {
    if (idx < 0 || idx >= (int)arr.size()) return false;
    if (arr.size() == 1) return true;
    bool leftOk = (idx == 0) || (arr[idx] > arr[idx - 1]);
    bool rightOk = (idx == (int)arr.size() - 1) || (arr[idx] > arr[idx + 1]);
    return leftOk && rightOk;
}

// =====================================================================
// Test functions
// =====================================================================

void test_warmup_01_linear_search() {
    assert(solve_linear_search({1,3,5,7,9}, 5) == 2);
    assert(solve_linear_search({1,3,5,7,9}, 4) == -1);
    assert(solve_linear_search({2,2,2,2}, 2) == 0);
    assert(solve_linear_search({}, 1) == -1);
    assert(solve_linear_search({7}, 7) == 0);
    cout << "  test_warmup_01_linear_search......... PASS" << endl;
}

void test_warmup_02_binary_search() {
    assert(solve_binary_search({1,3,5,7,9,11}, 7) == 3);
    assert(solve_binary_search({1,3,5,7,9,11}, 4) == -1);
    assert(solve_binary_search({2,4,6,8,10}, 2) == 0);
    assert(solve_binary_search({2,4,6,8,10}, 10) == 4);
    assert(solve_binary_search({}, 5) == -1);
    assert(solve_binary_search({1}, 1) == 0);
    cout << "  test_warmup_02_binary_search......... PASS" << endl;
}

void test_warmup_03_first_occurrence() {
    assert(solve_first_occurrence({1,2,2,2,3,4}, 2) == 1);
    assert(solve_first_occurrence({1,1,1,1,1}, 1) == 0);
    assert(solve_first_occurrence({1,3,5,7}, 5) == 2);
    assert(solve_first_occurrence({1,3,5,7}, 4) == -1);
    assert(solve_first_occurrence({}, 1) == -1);
    cout << "  test_warmup_03_first_occurrence...... PASS" << endl;
}

void test_warmup_04_last_occurrence() {
    assert(solve_last_occurrence({1,2,2,2,3,4}, 2) == 3);
    assert(solve_last_occurrence({1,1,1,1,1}, 1) == 4);
    assert(solve_last_occurrence({1,3,5,7}, 5) == 2);
    assert(solve_last_occurrence({1,3,5,7}, 4) == -1);
    assert(solve_last_occurrence({}, 1) == -1);
    cout << "  test_warmup_04_last_occurrence....... PASS" << endl;
}

void test_warmup_05_count_occurrences() {
    assert(solve_count_occurrences({1,2,2,2,3,4}, 2) == 3);
    assert(solve_count_occurrences({1,1,1,1,1}, 1) == 5);
    assert(solve_count_occurrences({1,3,5,7}, 5) == 1);
    assert(solve_count_occurrences({1,3,5,7}, 4) == 0);
    assert(solve_count_occurrences({}, 1) == 0);
    cout << "  test_warmup_05_count_occurrences..... PASS" << endl;
}

void test_practice_01_lower_bound() {
    assert(solve_lower_bound({1,3,5,7,9}, 5) == 2);
    assert(solve_lower_bound({1,3,5,7,9}, 4) == 2);
    assert(solve_lower_bound({1,3,5,7,9}, 1) == 0);
    assert(solve_lower_bound({1,3,5,7,9}, 10) == 5);
    assert(solve_lower_bound({2,2,2,2}, 2) == 0);
    assert(solve_lower_bound({}, 5) == 0);
    cout << "  test_practice_01_lower_bound......... PASS" << endl;
}

void test_practice_02_upper_bound() {
    assert(solve_upper_bound({1,3,5,7,9}, 5) == 3);
    assert(solve_upper_bound({1,3,5,7,9}, 4) == 2);
    assert(solve_upper_bound({1,3,5,7,9}, 0) == 0);
    assert(solve_upper_bound({1,3,5,7,9}, 9) == 5);
    assert(solve_upper_bound({2,2,2,2}, 2) == 4);
    assert(solve_upper_bound({}, 5) == 0);
    cout << "  test_practice_02_upper_bound......... PASS" << endl;
}

void test_practice_03_floor_and_ceil() {
    assert(solve_floor_ceil({1,3,5,7,9}, 5) == (vector<int>{5,5}));
    assert(solve_floor_ceil({1,3,5,7,9}, 4) == (vector<int>{3,5}));
    assert(solve_floor_ceil({1,3,5,7,9}, 0) == (vector<int>{-1,1}));
    assert(solve_floor_ceil({1,3,5,7,9}, 10) == (vector<int>{9,-1}));
    assert(solve_floor_ceil({1}, 1) == (vector<int>{1,1}));
    cout << "  test_practice_03_floor_and_ceil...... PASS" << endl;
}

void test_practice_04_search_rotated() {
    assert(solve_search_rotated({4,5,6,7,0,1,2}, 0) == 4);
    assert(solve_search_rotated({4,5,6,7,0,1,2}, 3) == -1);
    assert(solve_search_rotated({1}, 1) == 0);
    assert(solve_search_rotated({3,1,2}, 1) == 1);
    assert(solve_search_rotated({1,2,3,4,5}, 3) == 2);
    cout << "  test_practice_04_search_rotated...... PASS" << endl;
}

void test_practice_05_min_in_rotated() {
    assert(solve_min_rotated({3,4,5,1,2}) == 1);
    assert(solve_min_rotated({4,5,6,7,0,1,2}) == 0);
    assert(solve_min_rotated({1}) == 1);
    assert(solve_min_rotated({2,1}) == 1);
    assert(solve_min_rotated({1,2,3,4,5}) == 1);
    cout << "  test_practice_05_min_in_rotated...... PASS" << endl;
}

void test_challenge_01_find_peak() {
    // Test linear approach
    assert(is_peak({1,2,3,1}, solve_peak_linear({1,2,3,1})));
    assert(is_peak({1,2,1,3,5,6,4}, solve_peak_linear({1,2,1,3,5,6,4})));
    assert(is_peak({1}, solve_peak_linear({1})));
    assert(is_peak({3,2,1}, solve_peak_linear({3,2,1})));
    assert(is_peak({1,2,3}, solve_peak_linear({1,2,3})));
    assert(is_peak({5,10,20,15,7,3}, solve_peak_linear({5,10,20,15,7,3})));

    // Test binary approach
    assert(is_peak({1,2,3,1}, solve_peak_binary({1,2,3,1})));
    assert(is_peak({1,2,1,3,5,6,4}, solve_peak_binary({1,2,1,3,5,6,4})));
    assert(is_peak({1}, solve_peak_binary({1})));
    assert(is_peak({3,2,1}, solve_peak_binary({3,2,1})));
    assert(is_peak({1,2,3}, solve_peak_binary({1,2,3})));
    assert(is_peak({5,10,20,15,7,3}, solve_peak_binary({5,10,20,15,7,3})));

    // Test solve (wrapper)
    assert(is_peak({1,2,3,1}, solve_peak({1,2,3,1})));
    assert(is_peak({1,2,1,3,5,6,4}, solve_peak({1,2,1,3,5,6,4})));
    assert(is_peak({1}, solve_peak({1})));

    cout << "  test_challenge_01_find_peak.......... PASS" << endl;
}

void test_challenge_02_single_element() {
    assert(solve_single_element({1,1,2,3,3,4,4,8,8}) == 2);
    assert(solve_single_element({3,3,7,7,10,11,11}) == 10);
    assert(solve_single_element({1}) == 1);
    assert(solve_single_element({1,1,2}) == 2);
    assert(solve_single_element({1,2,2}) == 1);
    cout << "  test_challenge_02_single_element..... PASS" << endl;
}

void test_challenge_03_rotated_search_ii() {
    assert(solve_rotated_search_ii({2,5,6,0,0,1,2}, 0) == true);
    assert(solve_rotated_search_ii({2,5,6,0,0,1,2}, 3) == false);
    assert(solve_rotated_search_ii({1,0,1,1,1}, 0) == true);
    assert(solve_rotated_search_ii({1,1,1,1,1}, 2) == false);
    assert(solve_rotated_search_ii({1}, 1) == true);
    assert(solve_rotated_search_ii({1,3}, 3) == true);
    cout << "  test_challenge_03_rotated_search_ii.. PASS" << endl;
}

// =====================================================================
// Main -- run all tests
// =====================================================================
int main() {
    cout << "Testing Chapter 9..." << endl;
    cout << endl;

    cout << "--- Warmup Problems ---" << endl;
    test_warmup_01_linear_search();
    test_warmup_02_binary_search();
    test_warmup_03_first_occurrence();
    test_warmup_04_last_occurrence();
    test_warmup_05_count_occurrences();
    cout << endl;

    cout << "--- Practice Problems ---" << endl;
    test_practice_01_lower_bound();
    test_practice_02_upper_bound();
    test_practice_03_floor_and_ceil();
    test_practice_04_search_rotated();
    test_practice_05_min_in_rotated();
    cout << endl;

    cout << "--- Challenge Problems ---" << endl;
    test_challenge_01_find_peak();
    test_challenge_02_single_element();
    test_challenge_03_rotated_search_ii();
    cout << endl;

    cout << "All tests passed!" << endl;
    return 0;
}
