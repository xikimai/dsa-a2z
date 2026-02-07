/*
 * Example 02: Fast Sorts -- Merge Sort & Quick Sort
 * ==================================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * This file demonstrates two O(n log n) sorting algorithms:
 *   Part 1: Merge Sort -- divide, sort halves, merge
 *   Part 2: Quick Sort -- pick pivot, partition, recurse
 *   Part 3: Timing comparison of all sorts
 *
 * Build & run:
 *   g++ -std=c++17 -o example_02 code/cpp/ch08/learn/example_02_fast_sorts.cpp && ./example_02
 */

#include <algorithm>
#include <chrono>
#include <iomanip>
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
// 1. Merge Sort
// =====================================================================
// Idea: Split the array in half, sort each half, then merge.
// Time:  O(n log n) always
// Space: O(n) for the temporary merge buffer

void merge(vector<int>& arr, int left, int mid, int right, int depth) {
    vector<int> L(arr.begin() + left, arr.begin() + mid + 1);
    vector<int> R(arr.begin() + mid + 1, arr.begin() + right + 1);

    int i = 0, j = 0, k = left;
    while (i < (int)L.size() && j < (int)R.size()) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < (int)L.size()) arr[k++] = L[i++];
    while (j < (int)R.size()) arr[k++] = R[j++];

    // Visualize the merge
    string indent(depth * 2, ' ');
    cout << "  " << indent << "merge [" << left << ".." << mid << "] + ["
         << mid + 1 << ".." << right << "] -> ";
    for (int x = left; x <= right; x++) cout << arr[x] << " ";
    cout << endl;
}

void merge_sort(vector<int>& arr, int left, int right, int depth) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    merge_sort(arr, left, mid, depth + 1);
    merge_sort(arr, mid + 1, right, depth + 1);
    merge(arr, left, mid, right, depth);
}

void demo_merge_sort() {
    cout << "=== PART 1: Merge Sort ===" << endl;

    vector<int> arr = {38, 27, 43, 3, 9, 82, 10};
    print_vec("Original:", arr);
    cout << endl;

    merge_sort(arr, 0, (int)arr.size() - 1, 0);
    cout << endl;
    print_vec("Sorted:  ", arr);
    cout << endl;
}

// =====================================================================
// 2. Quick Sort (Lomuto partition)
// =====================================================================
// Idea: Pick a pivot, partition the array so everything < pivot
//       is on the left and everything > pivot is on the right.
//       Recurse on each side.
// Time:  O(n log n) average, O(n^2) worst
// Space: O(log n) average (recursion stack)

int partition(vector<int>& arr, int low, int high, int depth) {
    int pivot = arr[high];  // Lomuto: use last element as pivot
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);

    string indent(depth * 2, ' ');
    cout << "  " << indent << "pivot=" << pivot << ", partition ["
         << low << ".." << high << "] -> pos " << i + 1 << ": ";
    for (int x = low; x <= high; x++) cout << arr[x] << " ";
    cout << endl;

    return i + 1;
}

void quick_sort(vector<int>& arr, int low, int high, int depth) {
    if (low >= high) return;
    int pi = partition(arr, low, high, depth);
    quick_sort(arr, low, pi - 1, depth + 1);
    quick_sort(arr, pi + 1, high, depth + 1);
}

void demo_quick_sort() {
    cout << "=== PART 2: Quick Sort (Lomuto Partition) ===" << endl;

    vector<int> arr = {10, 7, 8, 9, 1, 5};
    print_vec("Original:", arr);
    cout << endl;

    quick_sort(arr, 0, (int)arr.size() - 1, 0);
    cout << endl;
    print_vec("Sorted:  ", arr);
    cout << endl;
}

// =====================================================================
// 3. Timing Comparison
// =====================================================================

// Silent versions for timing (no cout)
void merge_silent(vector<int>& arr, int l, int m, int r) {
    vector<int> L(arr.begin() + l, arr.begin() + m + 1);
    vector<int> R(arr.begin() + m + 1, arr.begin() + r + 1);
    int i = 0, j = 0, k = l;
    while (i < (int)L.size() && j < (int)R.size()) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < (int)L.size()) arr[k++] = L[i++];
    while (j < (int)R.size()) arr[k++] = R[j++];
}

void merge_sort_silent(vector<int>& arr, int l, int r) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    merge_sort_silent(arr, l, m);
    merge_sort_silent(arr, m + 1, r);
    merge_silent(arr, l, m, r);
}

void selection_sort_silent(vector<int>& arr) {
    int n = (int)arr.size();
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++)
            if (arr[j] < arr[min_idx]) min_idx = j;
        swap(arr[i], arr[min_idx]);
    }
}

void demo_timing() {
    cout << "=== PART 3: Timing Comparison ===" << endl;

    int sizes[] = {1000, 5000, 10000};
    for (int n : sizes) {
        // Generate random array
        vector<int> base(n);
        for (int i = 0; i < n; i++) base[i] = rand() % 100000;

        // Selection sort
        {
            vector<int> arr = base;
            auto start = chrono::high_resolution_clock::now();
            selection_sort_silent(arr);
            auto end = chrono::high_resolution_clock::now();
            double t = chrono::duration<double>(end - start).count();
            cout << "  n=" << setw(5) << n
                 << "  Selection: " << fixed << setprecision(6) << t << "s";
        }

        // Merge sort
        {
            vector<int> arr = base;
            auto start = chrono::high_resolution_clock::now();
            merge_sort_silent(arr, 0, (int)arr.size() - 1);
            auto end = chrono::high_resolution_clock::now();
            double t = chrono::duration<double>(end - start).count();
            cout << "  Merge: " << fixed << setprecision(6) << t << "s";
        }

        // std::sort
        {
            vector<int> arr = base;
            auto start = chrono::high_resolution_clock::now();
            sort(arr.begin(), arr.end());
            auto end = chrono::high_resolution_clock::now();
            double t = chrono::duration<double>(end - start).count();
            cout << "  std::sort: " << fixed << setprecision(6) << t << "s";
        }

        cout << endl;
    }
    cout << endl;
}

// =====================================================================
// main -- run all demos
// =====================================================================
int main() {
    cout << "Chapter 8: Fast Sorts" << endl;
    cout << "=====================" << endl << endl;

    demo_merge_sort();
    demo_quick_sort();
    demo_timing();

    cout << "Key takeaway: O(n^2) sorts are fine for small data," << endl;
    cout << "but merge sort and quick sort scale to millions of elements." << endl;
    cout << "In contests, just use sort() -- it's introsort (quicksort + heapsort)." << endl;
    return 0;
}
