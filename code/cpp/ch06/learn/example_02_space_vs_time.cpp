/*
 * Example 02: Space vs. Time
 * ==========================
 * Chapter 6: How Fast Is Your Code?
 *
 * This file solves "Contains Duplicate" three different ways and times
 * each approach to show the space-time tradeoff in action.
 *   Part 1: O(n^2) brute force, O(1) extra space
 *   Part 2: O(n log n) sort-first, O(n) space for copy
 *   Part 3: O(n) hash set, O(n) extra space
 *   Part 4: Timing comparison with different array sizes
 *
 * Build & run:
 *   g++ -std=c++17 -o example_02 code/cpp/ch06/learn/example_02_space_vs_time.cpp && ./example_02
 */

#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <unordered_set>
#include <vector>
using namespace std;

// =====================================================================
// PART 1: O(n^2) brute force, O(1) extra space
// =====================================================================
// Check every pair.  Simple, but slow for large arrays.

bool contains_duplicate_brute(vector<int>& nums) {
    int n = (int)nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (nums[i] == nums[j]) return true;
        }
    }
    return false;
}

// =====================================================================
// PART 2: O(n log n) sort-first, O(n) space for the copy
// =====================================================================
// Sort the array, then duplicates must be adjacent.

bool contains_duplicate_sort(vector<int>& nums) {
    vector<int> sorted_nums = nums;
    sort(sorted_nums.begin(), sorted_nums.end());
    for (int i = 1; i < (int)sorted_nums.size(); i++) {
        if (sorted_nums[i] == sorted_nums[i - 1]) return true;
    }
    return false;
}

// =====================================================================
// PART 3: O(n) hash set, O(n) extra space
// =====================================================================
// Use a set to remember what we've seen.  Fast but uses memory.

bool contains_duplicate_hash(vector<int>& nums) {
    unordered_set<int> seen;
    for (int x : nums) {
        if (seen.count(x)) return true;
        seen.insert(x);
    }
    return false;
}

// =====================================================================
// PART 4: Timing comparison
// =====================================================================

int main() {
    cout << "=== Contains Duplicate: Three Approaches ===" << endl;
    cout << endl;

    // Quick correctness check
    vector<int> test_dup = {1, 2, 3, 4, 2};
    vector<int> test_no_dup = {1, 2, 3, 4, 5};
    cout << "Correctness check:" << endl;
    cout << "  [1,2,3,4,2] has dup?  brute=" << (contains_duplicate_brute(test_dup) ? "true" : "false")
         << "  sort=" << (contains_duplicate_sort(test_dup) ? "true" : "false")
         << "  hash=" << (contains_duplicate_hash(test_dup) ? "true" : "false") << endl;
    cout << "  [1,2,3,4,5] has dup?  brute=" << (contains_duplicate_brute(test_no_dup) ? "true" : "false")
         << "  sort=" << (contains_duplicate_sort(test_no_dup) ? "true" : "false")
         << "  hash=" << (contains_duplicate_hash(test_no_dup) ? "true" : "false") << endl;
    cout << endl;

    // Timing with increasing sizes (arrays with NO duplicates = worst case for brute)
    int sizes[] = {1000, 10000, 50000};

    cout << setw(8) << "Size"
         << setw(16) << "Brute O(n^2)"
         << setw(16) << "Sort O(n lg n)"
         << setw(16) << "Hash O(n)" << endl;
    cout << string(56, '-') << endl;

    mt19937 rng(42);  // Fixed seed for reproducibility

    for (int size : sizes) {
        // Create an array of unique values and shuffle
        vector<int> arr(size);
        for (int i = 0; i < size; i++) arr[i] = i;
        shuffle(arr.begin(), arr.end(), rng);

        // Brute force
        auto start = chrono::high_resolution_clock::now();
        contains_duplicate_brute(arr);
        auto end = chrono::high_resolution_clock::now();
        double t_brute = chrono::duration<double>(end - start).count();

        // Sort
        start = chrono::high_resolution_clock::now();
        contains_duplicate_sort(arr);
        end = chrono::high_resolution_clock::now();
        double t_sort = chrono::duration<double>(end - start).count();

        // Hash
        start = chrono::high_resolution_clock::now();
        contains_duplicate_hash(arr);
        end = chrono::high_resolution_clock::now();
        double t_hash = chrono::duration<double>(end - start).count();

        cout << setw(8) << size
             << setw(15) << fixed << setprecision(6) << t_brute << "s"
             << setw(15) << fixed << setprecision(6) << t_sort << "s"
             << setw(15) << fixed << setprecision(6) << t_hash << "s" << endl;
    }

    cout << endl;
    cout << "Key takeaway: O(n^2) gets MUCH slower as n grows, while O(n)" << endl;
    cout << "barely changes.  The hash set uses more memory, but it's worth it!" << endl;
    return 0;
}
