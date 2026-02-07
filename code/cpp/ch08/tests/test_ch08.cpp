/*
 * Tests for Chapter 8: The Art of Sorting -- Putting Things in Order
 * Build: g++ -std=c++17 -o /tmp/test_ch08 code/cpp/ch08/tests/test_ch08.cpp && /tmp/test_ch08
 */

#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named to avoid collisions)
// =====================================================================

// --- W1: Selection Sort ---
vector<int> solve_selection_sort(vector<int> arr) {
    int n = (int)arr.size();
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) min_idx = j;
        }
        swap(arr[i], arr[min_idx]);
    }
    return arr;
}

// --- W2: Bubble Sort ---
vector<int> solve_bubble_sort(vector<int> arr) {
    int n = (int)arr.size();
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
    return arr;
}

// --- W3: Insertion Sort ---
vector<int> solve_insertion_sort(vector<int> arr) {
    int n = (int)arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    return arr;
}

// --- W4: Check If Sorted ---
bool solve_check_sorted(vector<int> arr) {
    for (int i = 0; i + 1 < (int)arr.size(); i++) {
        if (arr[i] > arr[i + 1]) return false;
    }
    return true;
}

// --- W5: Sort by Absolute Value ---
vector<int> solve_sort_by_abs(vector<int> arr) {
    sort(arr.begin(), arr.end(), [](int a, int b) {
        return abs(a) < abs(b);
    });
    return arr;
}

// --- P1: Merge Sort ---
void merge_p1(vector<int>& arr, int left, int mid, int right) {
    vector<int> L(arr.begin() + left, arr.begin() + mid + 1);
    vector<int> R(arr.begin() + mid + 1, arr.begin() + right + 1);
    int i = 0, j = 0, k = left;
    while (i < (int)L.size() && j < (int)R.size()) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < (int)L.size()) arr[k++] = L[i++];
    while (j < (int)R.size()) arr[k++] = R[j++];
}

void merge_sort_p1(vector<int>& arr, int left, int right) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    merge_sort_p1(arr, left, mid);
    merge_sort_p1(arr, mid + 1, right);
    merge_p1(arr, left, mid, right);
}

vector<int> solve_merge_sort(vector<int> arr) {
    if (arr.empty()) return arr;
    merge_sort_p1(arr, 0, (int)arr.size() - 1);
    return arr;
}

// --- P2: Quick Sort ---
int partition_p2(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quick_sort_p2(vector<int>& arr, int low, int high) {
    if (low >= high) return;
    int pi = partition_p2(arr, low, high);
    quick_sort_p2(arr, low, pi - 1);
    quick_sort_p2(arr, pi + 1, high);
}

vector<int> solve_quick_sort(vector<int> arr) {
    if (arr.empty()) return arr;
    quick_sort_p2(arr, 0, (int)arr.size() - 1);
    return arr;
}

// --- P3: Dutch National Flag ---
vector<int> solve_dutch_flag(vector<int> arr) {
    int low = 0, mid = 0, high = (int)arr.size() - 1;
    while (mid <= high) {
        if (arr[mid] == 0) {
            swap(arr[low], arr[mid]);
            low++;
            mid++;
        } else if (arr[mid] == 1) {
            mid++;
        } else {
            swap(arr[mid], arr[high]);
            high--;
        }
    }
    return arr;
}

// --- P4: Custom Comparator ---
vector<string> solve_custom_comp(vector<string> words) {
    sort(words.begin(), words.end(), [](const string& a, const string& b) {
        if (a.size() != b.size()) return a.size() < b.size();
        return a < b;
    });
    return words;
}

// --- P5: Merge Two Sorted ---
vector<int> solve_merge_two(vector<int> arr1, vector<int> arr2) {
    vector<int> result;
    int i = 0, j = 0;
    while (i < (int)arr1.size() && j < (int)arr2.size()) {
        if (arr1[i] <= arr2[j]) result.push_back(arr1[i++]);
        else result.push_back(arr2[j++]);
    }
    while (i < (int)arr1.size()) result.push_back(arr1[i++]);
    while (j < (int)arr2.size()) result.push_back(arr2[j++]);
    return result;
}

// --- C1: Sort Three Ways ---
vector<int> solve_c1_bubble(vector<int> arr) {
    int n = (int)arr.size();
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
    return arr;
}

void merge_c1(vector<int>& arr, int left, int mid, int right) {
    vector<int> L(arr.begin() + left, arr.begin() + mid + 1);
    vector<int> R(arr.begin() + mid + 1, arr.begin() + right + 1);
    int i = 0, j = 0, k = left;
    while (i < (int)L.size() && j < (int)R.size()) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < (int)L.size()) arr[k++] = L[i++];
    while (j < (int)R.size()) arr[k++] = R[j++];
}

void merge_sort_c1(vector<int>& arr, int left, int right) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    merge_sort_c1(arr, left, mid);
    merge_sort_c1(arr, mid + 1, right);
    merge_c1(arr, left, mid, right);
}

vector<int> solve_c1_merge(vector<int> arr) {
    if (arr.empty()) return arr;
    merge_sort_c1(arr, 0, (int)arr.size() - 1);
    return arr;
}

vector<int> solve_c1_builtin(vector<int> arr) {
    sort(arr.begin(), arr.end());
    return arr;
}

// --- C2: Count Inversions ---
long long merge_count_c2(vector<int>& arr, int left, int mid, int right) {
    vector<int> L(arr.begin() + left, arr.begin() + mid + 1);
    vector<int> R(arr.begin() + mid + 1, arr.begin() + right + 1);
    long long inversions = 0;
    int i = 0, j = 0, k = left;
    while (i < (int)L.size() && j < (int)R.size()) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            inversions += (int)L.size() - i;
            arr[k++] = R[j++];
        }
    }
    while (i < (int)L.size()) arr[k++] = L[i++];
    while (j < (int)R.size()) arr[k++] = R[j++];
    return inversions;
}

long long merge_sort_count_c2(vector<int>& arr, int left, int right) {
    if (left >= right) return 0;
    int mid = left + (right - left) / 2;
    long long count = 0;
    count += merge_sort_count_c2(arr, left, mid);
    count += merge_sort_count_c2(arr, mid + 1, right);
    count += merge_count_c2(arr, left, mid, right);
    return count;
}

long long solve_count_inversions(vector<int> arr) {
    if (arr.size() <= 1) return 0LL;
    return merge_sort_count_c2(arr, 0, (int)arr.size() - 1);
}

// --- C3: Sort by Frequency ---
vector<int> solve_sort_by_freq(vector<int> arr) {
    unordered_map<int, int> freq;
    for (int x : arr) freq[x]++;
    sort(arr.begin(), arr.end(), [&freq](int a, int b) {
        if (freq[a] != freq[b]) return freq[a] > freq[b];
        return a < b;
    });
    return arr;
}

// =====================================================================
// Test functions
// =====================================================================

void test_warmup_01_selection_sort() {
    assert(solve_selection_sort({64,25,12,22,11}) == (vector<int>{11,12,22,25,64}));
    assert(solve_selection_sort({1,2,3,4,5}) == (vector<int>{1,2,3,4,5}));
    assert(solve_selection_sort({5,4,3,2,1}) == (vector<int>{1,2,3,4,5}));
    assert(solve_selection_sort({1}) == (vector<int>{1}));
    assert(solve_selection_sort({3,3,1,1,2}) == (vector<int>{1,1,2,3,3}));
    cout << "  test_warmup_01_selection_sort......... PASS" << endl;
}

void test_warmup_02_bubble_sort() {
    assert(solve_bubble_sort({64,34,25,12,22,11,90}) == (vector<int>{11,12,22,25,34,64,90}));
    assert(solve_bubble_sort({1,2,3,4}) == (vector<int>{1,2,3,4}));
    assert(solve_bubble_sort({2,1}) == (vector<int>{1,2}));
    assert(solve_bubble_sort({}) == (vector<int>{}));
    assert(solve_bubble_sort({5,5,5}) == (vector<int>{5,5,5}));
    cout << "  test_warmup_02_bubble_sort............ PASS" << endl;
}

void test_warmup_03_insertion_sort() {
    assert(solve_insertion_sort({12,11,13,5,6}) == (vector<int>{5,6,11,12,13}));
    assert(solve_insertion_sort({1,2,3}) == (vector<int>{1,2,3}));
    assert(solve_insertion_sort({3,2,1}) == (vector<int>{1,2,3}));
    assert(solve_insertion_sort({7}) == (vector<int>{7}));
    assert(solve_insertion_sort({4,2,4,1,2}) == (vector<int>{1,2,2,4,4}));
    cout << "  test_warmup_03_insertion_sort......... PASS" << endl;
}

void test_warmup_04_check_if_sorted() {
    assert(solve_check_sorted({1,2,3,4,5}) == true);
    assert(solve_check_sorted({1,3,2,4,5}) == false);
    assert(solve_check_sorted({}) == true);
    assert(solve_check_sorted({7}) == true);
    assert(solve_check_sorted({1,1,1}) == true);
    cout << "  test_warmup_04_check_if_sorted....... PASS" << endl;
}

void test_warmup_05_sort_by_absolute() {
    assert(solve_sort_by_abs({3,-1,2,-5,4}) == (vector<int>{-1,2,3,4,-5}));
    assert(solve_sort_by_abs({-10,7,-3,1}) == (vector<int>{1,-3,7,-10}));
    assert(solve_sort_by_abs({0,-5,3,-1,8}) == (vector<int>{0,-1,3,-5,8}));
    assert(solve_sort_by_abs({1,2,3}) == (vector<int>{1,2,3}));
    assert(solve_sort_by_abs({-1}) == (vector<int>{-1}));
    cout << "  test_warmup_05_sort_by_absolute...... PASS" << endl;
}

void test_practice_01_merge_sort() {
    assert(solve_merge_sort({38,27,43,3,9,82,10}) == (vector<int>{3,9,10,27,38,43,82}));
    assert(solve_merge_sort({5,4,3,2,1}) == (vector<int>{1,2,3,4,5}));
    assert(solve_merge_sort({1}) == (vector<int>{1}));
    assert(solve_merge_sort({}) == (vector<int>{}));
    assert(solve_merge_sort({3,3,1,1,2}) == (vector<int>{1,1,2,3,3}));
    cout << "  test_practice_01_merge_sort.......... PASS" << endl;
}

void test_practice_02_quick_sort() {
    assert(solve_quick_sort({10,7,8,9,1,5}) == (vector<int>{1,5,7,8,9,10}));
    assert(solve_quick_sort({3,2,1}) == (vector<int>{1,2,3}));
    assert(solve_quick_sort({1}) == (vector<int>{1}));
    assert(solve_quick_sort({}) == (vector<int>{}));
    assert(solve_quick_sort({5,5,5,5}) == (vector<int>{5,5,5,5}));
    cout << "  test_practice_02_quick_sort.......... PASS" << endl;
}

void test_practice_03_dutch_national_flag() {
    assert(solve_dutch_flag({2,0,2,1,1,0}) == (vector<int>{0,0,1,1,2,2}));
    assert(solve_dutch_flag({2,0,1}) == (vector<int>{0,1,2}));
    assert(solve_dutch_flag({0,0,0}) == (vector<int>{0,0,0}));
    assert(solve_dutch_flag({}) == (vector<int>{}));
    assert(solve_dutch_flag({1}) == (vector<int>{1}));
    cout << "  test_practice_03_dutch_national_flag. PASS" << endl;
}

void test_practice_04_custom_comparator() {
    assert(solve_custom_comp({"banana","apple","kiwi","cherry","fig"}) == (vector<string>{"fig","kiwi","apple","banana","cherry"}));
    assert(solve_custom_comp({"cat","bat","ant"}) == (vector<string>{"ant","bat","cat"}));
    assert(solve_custom_comp({"a","bb","ccc","dd","e"}) == (vector<string>{"a","e","bb","dd","ccc"}));
    cout << "  test_practice_04_custom_comparator... PASS" << endl;
}

void test_practice_05_merge_two_sorted() {
    assert(solve_merge_two({1,3,5}, {2,4,6}) == (vector<int>{1,2,3,4,5,6}));
    assert(solve_merge_two({1,2,3}, {}) == (vector<int>{1,2,3}));
    assert(solve_merge_two({}, {4,5,6}) == (vector<int>{4,5,6}));
    assert(solve_merge_two({1,1,1}, {1,1,1}) == (vector<int>{1,1,1,1,1,1}));
    assert(solve_merge_two({1,5,9}, {2,3,7,10}) == (vector<int>{1,2,3,5,7,9,10}));
    cout << "  test_practice_05_merge_two_sorted.... PASS" << endl;
}

void test_challenge_01_sort_three_ways() {
    // Bubble
    assert(solve_c1_bubble({5,3,8,1,2}) == (vector<int>{1,2,3,5,8}));
    assert(solve_c1_bubble({}) == (vector<int>{}));
    assert(solve_c1_bubble({1}) == (vector<int>{1}));

    // Merge
    assert(solve_c1_merge({5,3,8,1,2}) == (vector<int>{1,2,3,5,8}));
    assert(solve_c1_merge({}) == (vector<int>{}));
    assert(solve_c1_merge({1}) == (vector<int>{1}));

    // Builtin
    assert(solve_c1_builtin({5,3,8,1,2}) == (vector<int>{1,2,3,5,8}));
    assert(solve_c1_builtin({}) == (vector<int>{}));
    assert(solve_c1_builtin({1}) == (vector<int>{1}));

    // All three produce the same output
    vector<int> input = {9,1,5,3,7,2,8,4,6};
    assert(solve_c1_bubble(input) == solve_c1_merge(input));
    assert(solve_c1_merge(input) == solve_c1_builtin(input));

    cout << "  test_challenge_01_sort_three_ways.... PASS" << endl;
}

void test_challenge_02_count_inversions() {
    assert(solve_count_inversions({2,4,1,3,5}) == 3);
    assert(solve_count_inversions({1,2,3,4,5}) == 0);
    assert(solve_count_inversions({5,4,3,2,1}) == 10);
    assert(solve_count_inversions({1}) == 0);
    assert(solve_count_inversions({}) == 0);
    assert(solve_count_inversions({1,1,1}) == 0);
    cout << "  test_challenge_02_count_inversions... PASS" << endl;
}

void test_challenge_03_sort_by_frequency() {
    assert(solve_sort_by_freq({1,1,2,2,2,3}) == (vector<int>{2,2,2,1,1,3}));
    assert(solve_sort_by_freq({4,4,4,5,5,6}) == (vector<int>{4,4,4,5,5,6}));
    assert(solve_sort_by_freq({1,2,3}) == (vector<int>{1,2,3}));
    assert(solve_sort_by_freq({5}) == (vector<int>{5}));
    assert(solve_sort_by_freq({3,3,1,1,2,2}) == (vector<int>{1,1,2,2,3,3}));
    cout << "  test_challenge_03_sort_by_frequency.. PASS" << endl;
}

// =====================================================================
// Main -- run all tests
// =====================================================================
int main() {
    cout << "Testing Chapter 8..." << endl;
    cout << endl;

    cout << "--- Warmup Problems ---" << endl;
    test_warmup_01_selection_sort();
    test_warmup_02_bubble_sort();
    test_warmup_03_insertion_sort();
    test_warmup_04_check_if_sorted();
    test_warmup_05_sort_by_absolute();
    cout << endl;

    cout << "--- Practice Problems ---" << endl;
    test_practice_01_merge_sort();
    test_practice_02_quick_sort();
    test_practice_03_dutch_national_flag();
    test_practice_04_custom_comparator();
    test_practice_05_merge_two_sorted();
    cout << endl;

    cout << "--- Challenge Problems ---" << endl;
    test_challenge_01_sort_three_ways();
    test_challenge_02_count_inversions();
    test_challenge_03_sort_by_frequency();
    cout << endl;

    cout << "All tests passed!" << endl;
    return 0;
}
