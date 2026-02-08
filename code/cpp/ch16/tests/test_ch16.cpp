/*
 * Tests for Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 * Build: g++ -std=c++17 -o /tmp/test_ch16 code/cpp/ch16/tests/test_ch16.cpp && /tmp/test_ch16
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions
// =====================================================================

// W1: Square Root (Integer)
int ref_square_root(int n) {
    if (n <= 0) return 0;
    int lo = 1, hi = n;
    while (lo < hi) {
        int mid = lo + (hi - lo + 1) / 2;
        if (mid <= n / mid) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}

// W2: First and Last Position
vector<int> ref_first_last(vector<int> arr, int target) {
    if (arr.empty()) return {-1, -1};
    int first = -1, last = -1;
    int lo = 0, hi = (int)arr.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) { first = mid; hi = mid - 1; }
        else if (arr[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    if (first == -1) return {-1, -1};
    lo = first; hi = (int)arr.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) { last = mid; lo = mid + 1; }
        else if (arr[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return {first, last};
}

// W3: Search in Rotated Sorted Array
int ref_search_rotated(vector<int> arr, int target) {
    if (arr.empty()) return -1;
    int lo = 0, hi = (int)arr.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) return mid;
        if (arr[lo] <= arr[mid]) {
            if (arr[lo] <= target && target < arr[mid]) hi = mid - 1;
            else lo = mid + 1;
        } else {
            if (arr[mid] < target && target <= arr[hi]) lo = mid + 1;
            else hi = mid - 1;
        }
    }
    return -1;
}

// W4: Peak Element
int ref_peak_element(vector<int> arr) {
    if (arr.empty()) return -1;
    if (arr.size() == 1) return 0;
    int lo = 0, hi = (int)arr.size() - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] < arr[mid + 1]) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

bool is_peak(vector<int>& arr, int idx) {
    if (idx < 0 || idx >= (int)arr.size()) return false;
    bool left_ok = (idx == 0) || (arr[idx] > arr[idx - 1]);
    bool right_ok = (idx == (int)arr.size() - 1) || (arr[idx] > arr[idx + 1]);
    return left_ok && right_ok;
}

// P1: Koko Eating Bananas
int ref_koko(vector<int> piles, int h) {
    int lo = 1, hi = *max_element(piles.begin(), piles.end());
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        int hours = 0;
        for (int p : piles) hours += (p + mid - 1) / mid;
        if (hours <= h) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}

// P2: Ship Packages
int ref_ship(vector<int> weights, int d) {
    int lo = *max_element(weights.begin(), weights.end());
    int hi = accumulate(weights.begin(), weights.end(), 0);
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        int days = 1, load = 0;
        for (int w : weights) {
            if (load + w > mid) { days++; load = 0; }
            load += w;
        }
        if (days <= d) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}

// P3: Search in 2D Matrix
vector<int> ref_search_matrix(vector<vector<int>> matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) return {-1, -1};
    int rows = matrix.size(), cols = matrix[0].size();
    int lo = 0, hi = rows * cols - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        int val = matrix[mid / cols][mid % cols];
        if (val == target) return {mid / cols, mid % cols};
        else if (val < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return {-1, -1};
}

// P4: Row with Maximum 1s
int ref_max_ones_row(vector<vector<int>> matrix) {
    if (matrix.empty() || matrix[0].empty()) return -1;
    int bestRow = -1, bestCount = 0;
    int cols = matrix[0].size();
    for (int i = 0; i < (int)matrix.size(); i++) {
        int lo = 0, hi = cols;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (matrix[i][mid] == 1) hi = mid;
            else lo = mid + 1;
        }
        int count = cols - lo;
        if (count > bestCount) { bestCount = count; bestRow = i; }
    }
    return bestRow;
}

// P5: Minimum Pages
int ref_min_pages(vector<int> pages, int students) {
    if (students > (int)pages.size()) return -1;
    int lo = *max_element(pages.begin(), pages.end());
    int hi = accumulate(pages.begin(), pages.end(), 0);
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        int count = 1, current = 0;
        for (int p : pages) {
            if (current + p > mid) { count++; current = 0; }
            current += p;
        }
        if (count <= students) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}

// C1: Aggressive Cows
int ref_cows(vector<int> stalls, int cows) {
    sort(stalls.begin(), stalls.end());
    int lo = 1, hi = stalls.back() - stalls[0];
    while (lo < hi) {
        int mid = lo + (hi - lo + 1) / 2;
        int count = 1, last = stalls[0];
        bool ok = false;
        for (int i = 1; i < (int)stalls.size(); i++) {
            if (stalls[i] - last >= mid) {
                count++;
                last = stalls[i];
                if (count >= cows) { ok = true; break; }
            }
        }
        if (ok) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}

// C2: Painter's Partition
int ref_painter(vector<int> boards, int k) {
    int lo = *max_element(boards.begin(), boards.end());
    int hi = accumulate(boards.begin(), boards.end(), 0);
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        int painters = 1, current = 0;
        for (int b : boards) {
            if (current + b > mid) { painters++; current = 0; }
            current += b;
        }
        if (painters <= k) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}

// C3: Median of Two Sorted Arrays
double ref_median(vector<int> nums1, vector<int> nums2) {
    if (nums1.size() > nums2.size()) swap(nums1, nums2);
    int m = nums1.size(), n = nums2.size();
    int half = (m + n + 1) / 2;
    int lo = 0, hi = m;
    while (lo <= hi) {
        int i = lo + (hi - lo) / 2;
        int j = half - i;
        int left1 = (i > 0) ? nums1[i - 1] : INT_MIN;
        int left2 = (j > 0) ? nums2[j - 1] : INT_MIN;
        int right1 = (i < m) ? nums1[i] : INT_MAX;
        int right2 = (j < n) ? nums2[j] : INT_MAX;
        if (left1 <= right2 && left2 <= right1) {
            if ((m + n) % 2 == 1) return max(left1, left2);
            else return (max(left1, left2) + min(right1, right2)) / 2.0;
        } else if (left1 > right2) hi = i - 1;
        else lo = i + 1;
    }
    return 0.0;
}

// C4: Kth Element of Two Sorted Arrays
int ref_kth(vector<int> nums1, vector<int> nums2, int k) {
    if (nums1.size() > nums2.size()) return ref_kth(nums2, nums1, k);
    int m = nums1.size(), n = nums2.size();
    int lo = max(0, k - n), hi = min(k, m);
    while (lo <= hi) {
        int i = lo + (hi - lo) / 2;
        int j = k - i;
        int left1 = (i > 0) ? nums1[i - 1] : INT_MIN;
        int left2 = (j > 0) ? nums2[j - 1] : INT_MIN;
        int right1 = (i < m) ? nums1[i] : INT_MAX;
        int right2 = (j < n) ? nums2[j] : INT_MAX;
        if (left1 <= right2 && left2 <= right1) return max(left1, left2);
        else if (left1 > right2) hi = i - 1;
        else lo = i + 1;
    }
    return -1;
}

// =====================================================================
// Test framework
// =====================================================================

int tests_passed = 0;
int tests_total = 0;

void check(bool condition, const string& name) {
    tests_total++;
    if (condition) { tests_passed++; }
    else { cout << "  FAIL: " << name << endl; }
}

// =====================================================================
// Tests
// =====================================================================

void test_w1() {
    cout << "Testing W1: Square Root..." << endl;
    check(ref_square_root(16) == 4, "perfect 16");
    check(ref_square_root(8) == 2, "non-perfect 8");
    check(ref_square_root(0) == 0, "zero");
    check(ref_square_root(1) == 1, "one");
    check(ref_square_root(100) == 10, "100");
    check(ref_square_root(99) == 9, "99");
    check(ref_square_root(2) == 1, "two");
    check(ref_square_root(49) == 7, "49");
}

void test_w2() {
    cout << "Testing W2: First and Last Position..." << endl;
    check(ref_first_last({5,7,7,8,8,10}, 8) == vector<int>{3,4}, "basic");
    check(ref_first_last({5,7,7,8,8,10}, 6) == vector<int>{-1,-1}, "not found");
    check(ref_first_last({1,2,3,4,5}, 3) == vector<int>{2,2}, "single");
    check(ref_first_last({2,2,2,2}, 2) == vector<int>{0,3}, "all same");
    check(ref_first_last({}, 1) == vector<int>{-1,-1}, "empty");
    check(ref_first_last({5}, 5) == vector<int>{0,0}, "single found");
    check(ref_first_last({5}, 3) == vector<int>{-1,-1}, "single not found");
    check(ref_first_last({1,1,3,5,5}, 1) == vector<int>{0,1}, "boundary left");
    check(ref_first_last({1,1,3,5,5}, 5) == vector<int>{3,4}, "boundary right");
}

void test_w3() {
    cout << "Testing W3: Search in Rotated Sorted Array..." << endl;
    check(ref_search_rotated({4,5,6,7,0,1,2}, 0) == 4, "basic");
    check(ref_search_rotated({4,5,6,7,0,1,2}, 3) == -1, "not found");
    check(ref_search_rotated({1}, 1) == 0, "single");
    check(ref_search_rotated({1,2,3,4,5}, 3) == 2, "not rotated");
    check(ref_search_rotated({}, 5) == -1, "empty");
    check(ref_search_rotated({3,4,5,1,2}, 5) == 2, "at pivot");
    check(ref_search_rotated({2,1}, 1) == 1, "two elements");
    check(ref_search_rotated({4,5,6,7,0,1,2}, 4) == 0, "first element");
}

void test_w4() {
    cout << "Testing W4: Peak Element..." << endl;
    vector<int> a1 = {1,2,3,1};
    check(is_peak(a1, ref_peak_element(a1)), "basic");
    vector<int> a2 = {1,2,1,3,5,6,4};
    check(is_peak(a2, ref_peak_element(a2)), "multiple peaks");
    check(ref_peak_element({1}) == 0, "single");
    vector<int> a3 = {1,2,3,4,5};
    check(is_peak(a3, ref_peak_element(a3)), "ascending");
    vector<int> a4 = {5,4,3,2,1};
    check(is_peak(a4, ref_peak_element(a4)), "descending");
    vector<int> a5 = {1,2};
    check(is_peak(a5, ref_peak_element(a5)), "two asc");
    vector<int> a6 = {2,1};
    check(is_peak(a6, ref_peak_element(a6)), "two desc");
}

void test_p1() {
    cout << "Testing P1: Koko Eating Bananas..." << endl;
    check(ref_koko({3,6,7,11}, 8) == 4, "basic");
    check(ref_koko({30}, 3) == 10, "single pile");
    check(ref_koko({5,5,5,5}, 4) == 5, "equal piles");
    check(ref_koko({3,6,7,11}, 20) == 2, "generous time");
    check(ref_koko({30,11,23,4,20}, 5) == 30, "tight time");
    check(ref_koko({10,10,10}, 3) == 10, "exact fit");
    check(ref_koko({7}, 1) == 7, "one pile one hour");
}

void test_p2() {
    cout << "Testing P2: Ship Packages..." << endl;
    check(ref_ship({1,2,3,4,5,6,7,8,9,10}, 5) == 15, "basic");
    check(ref_ship({3,2,2,4,1,4}, 1) == 16, "one day");
    check(ref_ship({3,2,2,4,1,4}, 6) == 4, "many days");
    check(ref_ship({10}, 1) == 10, "single");
    check(ref_ship({5,5,5,5}, 2) == 10, "equal");
    check(ref_ship({1,2,3,1,1}, 4) == 3, "heavy last");
    check(ref_ship({3,2,2,4,1,4}, 3) == 6, "three days");
}

void test_p3() {
    cout << "Testing P3: Search in 2D Matrix..." << endl;
    check(ref_search_matrix({{1,3,5,7},{10,11,16,20},{23,30,34,60}}, 3) == vector<int>{0,1}, "basic");
    check(ref_search_matrix({{1,3,5,7},{10,11,16,20},{23,30,34,60}}, 13) == vector<int>{-1,-1}, "not found");
    check(ref_search_matrix({{1,3,5},{7,9,11}}, 1) == vector<int>{0,0}, "first");
    check(ref_search_matrix({{1,3,5},{7,9,11}}, 11) == vector<int>{1,2}, "last");
    check(ref_search_matrix({{5}}, 5) == vector<int>{0,0}, "single found");
    check(ref_search_matrix({{5}}, 3) == vector<int>{-1,-1}, "single not found");
    check(ref_search_matrix({}, 1) == vector<int>{-1,-1}, "empty");
}

void test_p4() {
    cout << "Testing P4: Row with Maximum 1s..." << endl;
    check(ref_max_ones_row({{0,0,0,1,1},{0,0,1,1,1},{0,0,0,0,1},{0,1,1,1,1},{0,0,0,0,0}}) == 3, "basic");
    check(ref_max_ones_row({{0,0,0},{0,0,0}}) == -1, "all zeros");
    check(ref_max_ones_row({{1,1,1},{1,1,1}}) == 0, "all ones");
    check(ref_max_ones_row({{0,1,1}}) == 0, "single row");
    check(ref_max_ones_row({{1}}) == 0, "single 1");
    check(ref_max_ones_row({{0}}) == -1, "single 0");
    check(ref_max_ones_row({{0,0,0},{0,0,1},{0,1,1}}) == 2, "last row wins");
}

void test_p5() {
    cout << "Testing P5: Minimum Pages..." << endl;
    check(ref_min_pages({12,34,67,90}, 2) == 113, "basic");
    check(ref_min_pages({10,20,30}, 1) == 60, "single student");
    check(ref_min_pages({10,20,30}, 3) == 30, "one each");
    check(ref_min_pages({25,25,25,25}, 2) == 50, "equal");
    check(ref_min_pages({10,20}, 3) == -1, "more students");
    check(ref_min_pages({5,5,5,100}, 2) == 100, "large last");
    check(ref_min_pages({50}, 1) == 50, "single book");
}

void test_c1() {
    cout << "Testing C1: Aggressive Cows..." << endl;
    check(ref_cows({1,2,8,4,9}, 3) == 3, "basic");
    check(ref_cows({1,2,4,8,9}, 2) == 8, "two cows");
    check(ref_cows({1,3,5}, 3) == 2, "all used");
    check(ref_cows({1,100}, 2) == 99, "large gap");
    check(ref_cows({1,5,9,13}, 4) == 4, "evenly spaced");
    check(ref_cows({10,1,5,7,3}, 3) == 4, "unsorted");
    check(ref_cows({1,2,3,4,5,6,7,8,9,10}, 2) == 9, "many stalls");
}

void test_c2() {
    cout << "Testing C2: Painter's Partition..." << endl;
    check(ref_painter({10,20,30,40}, 2) == 60, "basic");
    check(ref_painter({10,20,30}, 1) == 60, "single painter");
    check(ref_painter({10,20,30}, 3) == 30, "one each");
    check(ref_painter({25,25,25,25}, 2) == 50, "equal");
    check(ref_painter({10,20}, 5) == 20, "more painters");
    check(ref_painter({5,5,5,100}, 2) == 100, "large board");
    check(ref_painter({1,2,3,4,5}, 5) == 5, "many painters");
}

void test_c3() {
    cout << "Testing C3: Median of Two Sorted..." << endl;
    check(abs(ref_median({1,3}, {2}) - 2.0) < 1e-6, "odd total");
    check(abs(ref_median({1,2}, {3,4}) - 2.5) < 1e-6, "even total");
    check(abs(ref_median({}, {1}) - 1.0) < 1e-6, "one empty");
    check(abs(ref_median({2}, {}) - 2.0) < 1e-6, "other empty");
    check(abs(ref_median({1,1}, {1,1}) - 1.0) < 1e-6, "all same");
    check(abs(ref_median({1,2}, {3,4,5}) - 3.0) < 1e-6, "no overlap");
    check(abs(ref_median({1}, {2}) - 1.5) < 1e-6, "single each");
    check(abs(ref_median({1,3,5,7}, {2,4,6,8}) - 4.5) < 1e-6, "interleaved");
}

void test_c4() {
    cout << "Testing C4: Kth Element of Two Sorted..." << endl;
    check(ref_kth({2,3,6,7,9}, {1,4,8,10}, 5) == 6, "basic");
    check(ref_kth({1,3,5}, {2,4,6}, 1) == 1, "first");
    check(ref_kth({1,3}, {2,4}, 4) == 4, "last");
    check(ref_kth({}, {1,2,3}, 2) == 2, "one empty");
    check(ref_kth({5,10,15}, {}, 3) == 15, "other empty");
    check(ref_kth({1,2,3}, {10,20,30}, 3) == 3, "all from first");
    check(ref_kth({10,20,30}, {1,2,3}, 3) == 3, "all from second");
    check(ref_kth({3,5}, {1,7}, 1) == 1, "k=1");
}

int main() {
    test_w1();
    test_w2();
    test_w3();
    test_w4();
    test_p1();
    test_p2();
    test_p3();
    test_p4();
    test_p5();
    test_c1();
    test_c2();
    test_c3();
    test_c4();

    cout << endl;
    if (tests_passed == tests_total) {
        cout << "All " << tests_total << " tests passed!" << endl;
    } else {
        cout << tests_passed << " / " << tests_total << " tests passed." << endl;
    }
    return (tests_passed == tests_total) ? 0 : 1;
}
