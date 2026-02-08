/*
 * Tests for Chapter 17: Heaps & Priority Queues — The VIP Line
 * Build: g++ -std=c++17 -o /tmp/test_ch17 code/cpp/ch17/tests/test_ch17.cpp && /tmp/test_ch17
 */

#include <algorithm>
#include <cassert>
#include <cmath>
#include <deque>
#include <functional>
#include <iostream>
#include <queue>
#include <string>
#include <tuple>
#include <unordered_map>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named with ref_ prefix)
// =====================================================================

// --- W1: Kth Largest Element ---
int ref_kth_largest(vector<int> nums, int k) {
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int x : nums) {
        pq.push(x);
        if ((int)pq.size() > k) pq.pop();
    }
    return pq.top();
}

// --- W2: Heap Sort ---
vector<int> ref_heap_sort(vector<int> arr) {
    priority_queue<int, vector<int>, greater<int>> pq(arr.begin(), arr.end());
    vector<int> result;
    while (!pq.empty()) {
        result.push_back(pq.top());
        pq.pop();
    }
    return result;
}

// --- W3: Last Stone Weight ---
int ref_last_stone_weight(vector<int> stones) {
    priority_queue<int> pq(stones.begin(), stones.end());
    while (pq.size() > 1) {
        int a = pq.top(); pq.pop();
        int b = pq.top(); pq.pop();
        if (a != b) pq.push(a - b);
    }
    return pq.empty() ? 0 : pq.top();
}

// --- W4: Check if Array is a Min-Heap ---
bool ref_is_heap(vector<int> arr) {
    int n = arr.size();
    for (int i = 0; i < n / 2; i++) {
        int l = 2 * i + 1, r = 2 * i + 2;
        if (l < n && arr[i] > arr[l]) return false;
        if (r < n && arr[i] > arr[r]) return false;
    }
    return true;
}

// --- P1: Top K Frequent Elements ---
vector<int> ref_top_k_frequent(vector<int> nums, int k) {
    unordered_map<int, int> freq;
    for (int x : nums) freq[x]++;
    auto cmp = [](const pair<int,int>& a, const pair<int,int>& b) {
        return a.first > b.first;
    };
    priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(cmp)> pq(cmp);
    for (auto& [val, cnt] : freq) {
        pq.push({cnt, val});
        if ((int)pq.size() > k) pq.pop();
    }
    vector<int> result;
    while (!pq.empty()) { result.push_back(pq.top().second); pq.pop(); }
    sort(result.begin(), result.end());
    return result;
}

// --- P2: Merge K Sorted Arrays ---
vector<int> ref_merge_k_sorted(vector<vector<int>> arrays) {
    auto cmp = [](const tuple<int,int,int>& a, const tuple<int,int,int>& b) {
        return get<0>(a) > get<0>(b);
    };
    priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, decltype(cmp)> pq(cmp);
    for (int i = 0; i < (int)arrays.size(); i++) {
        if (!arrays[i].empty()) pq.push({arrays[i][0], i, 0});
    }
    vector<int> result;
    while (!pq.empty()) {
        auto [val, ai, ei] = pq.top(); pq.pop();
        result.push_back(val);
        if (ei + 1 < (int)arrays[ai].size()) pq.push({arrays[ai][ei+1], ai, ei+1});
    }
    return result;
}

// --- P3: Kth Smallest in Sorted Matrix ---
int ref_kth_smallest_matrix(vector<vector<int>> matrix, int k) {
    auto cmp = [](const tuple<int,int,int>& a, const tuple<int,int,int>& b) {
        return get<0>(a) > get<0>(b);
    };
    priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, decltype(cmp)> pq(cmp);
    for (int r = 0; r < (int)matrix.size(); r++) pq.push({matrix[r][0], r, 0});
    int val = 0;
    for (int i = 0; i < k; i++) {
        auto [v, r, c] = pq.top(); pq.pop(); val = v;
        if (c + 1 < (int)matrix[r].size()) pq.push({matrix[r][c+1], r, c+1});
    }
    return val;
}

// --- P4: Find Median from Data Stream ---
vector<double> ref_find_median(vector<int> nums) {
    priority_queue<int> maxH;
    priority_queue<int, vector<int>, greater<int>> minH;
    vector<double> medians;
    for (int num : nums) {
        maxH.push(num);
        if (!minH.empty() && maxH.top() > minH.top()) {
            int v = maxH.top(); maxH.pop(); minH.push(v);
        }
        if ((int)maxH.size() > (int)minH.size() + 1) {
            int v = maxH.top(); maxH.pop(); minH.push(v);
        } else if ((int)minH.size() > (int)maxH.size()) {
            int v = minH.top(); minH.pop(); maxH.push(v);
        }
        if (maxH.size() > minH.size()) medians.push_back((double)maxH.top());
        else medians.push_back((maxH.top() + minH.top()) / 2.0);
    }
    return medians;
}

// --- P5: K Closest Points to Origin ---
vector<vector<int>> ref_k_closest(vector<vector<int>> points, int k) {
    auto cmp = [](const tuple<int,int,int>& a, const tuple<int,int,int>& b) {
        return get<0>(a) < get<0>(b);
    };
    priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, decltype(cmp)> pq(cmp);
    for (auto& p : points) {
        int d = p[0]*p[0] + p[1]*p[1];
        pq.push({d, p[0], p[1]});
        if ((int)pq.size() > k) pq.pop();
    }
    vector<vector<int>> result;
    while (!pq.empty()) {
        auto [d, x, y] = pq.top(); pq.pop();
        result.push_back({x, y});
    }
    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0]*a[0]+a[1]*a[1] < b[0]*b[0]+b[1]*b[1];
    });
    return result;
}

// --- C1: Reorganize String ---
string ref_reorganize(string s) {
    int freq[26] = {};
    for (char c : s) freq[c - 'a']++;
    int maxC = *max_element(freq, freq + 26);
    if (maxC > ((int)s.size() + 1) / 2) return "";
    priority_queue<pair<int,int>> pq;
    for (int i = 0; i < 26; i++) if (freq[i] > 0) pq.push({freq[i], i});
    string result;
    pair<int,int> prev = {0, -1};
    while (!pq.empty()) {
        auto [cnt, ch] = pq.top(); pq.pop();
        result += (char)(ch + 'a');
        if (prev.first > 0) pq.push(prev);
        prev = {cnt - 1, ch};
    }
    return result;
}

// --- C2: Task Scheduler ---
int ref_task_scheduler(vector<char> tasks, int n) {
    int freq[26] = {};
    for (char t : tasks) freq[t - 'A']++;
    priority_queue<int> pq;
    for (int f : freq) if (f > 0) pq.push(f);
    int time = 0;
    while (!pq.empty()) {
        int cycle = n + 1;
        vector<int> temp;
        int done = 0;
        for (int i = 0; i < cycle; i++) {
            if (!pq.empty()) {
                int c = pq.top(); pq.pop();
                if (c > 1) temp.push_back(c - 1);
                done++;
            }
        }
        for (int t : temp) pq.push(t);
        time += pq.empty() ? done : cycle;
    }
    return time;
}

// --- C3: Sliding Window Maximum ---
vector<int> ref_sliding_window_max(vector<int> nums, int k) {
    deque<int> dq;
    vector<int> result;
    for (int i = 0; i < (int)nums.size(); i++) {
        while (!dq.empty() && nums[dq.back()] <= nums[i]) dq.pop_back();
        dq.push_back(i);
        if (dq.front() <= i - k) dq.pop_front();
        if (i >= k - 1) result.push_back(nums[dq.front()]);
    }
    return result;
}

// =====================================================================
// Test framework
// =====================================================================

int tests_passed = 0;
int tests_total = 0;

void check(bool condition, const string& name) {
    tests_total++;
    if (condition) {
        tests_passed++;
    } else {
        cout << "  FAIL: " << name << endl;
    }
}

bool doubles_equal(const vector<double>& a, const vector<double>& b) {
    if (a.size() != b.size()) return false;
    for (int i = 0; i < (int)a.size(); i++) {
        if (abs(a[i] - b[i]) > 0.01) return false;
    }
    return true;
}

bool is_valid_reorganize(const string& original, const string& result) {
    if (result.empty()) {
        // Check if impossible
        int freq[26] = {};
        for (char c : original) freq[c - 'a']++;
        int maxF = *max_element(freq, freq + 26);
        return maxF > ((int)original.size() + 1) / 2;
    }
    // Check same chars
    string a = original, b = result;
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    if (a != b) return false;
    // Check no adjacent same
    for (int i = 1; i < (int)result.size(); i++) {
        if (result[i] == result[i-1]) return false;
    }
    return true;
}

// =====================================================================
// Test functions
// =====================================================================

void test_w1_kth_largest() {
    cout << "Testing W1: Kth Largest Element..." << endl;
    check(ref_kth_largest({3,2,1,5,6,4}, 2) == 5, "W1: basic");
    check(ref_kth_largest({3,2,3,1,2,4,5,5,6}, 4) == 4, "W1: duplicates");
    check(ref_kth_largest({1}, 1) == 1, "W1: single");
    check(ref_kth_largest({7,6,5,4,3,2,1}, 7) == 1, "W1: k=n");
    check(ref_kth_largest({5,5,5,5}, 2) == 5, "W1: all same");
    check(ref_kth_largest({-1,-2,-3,-4,-5}, 2) == -2, "W1: negative");
    check(ref_kth_largest({3,-2,7,1,0,-5}, 3) == 1, "W1: mixed");
}

void test_w2_heap_sort() {
    cout << "Testing W2: Heap Sort..." << endl;
    check(ref_heap_sort({5,3,8,1,2}) == vector<int>{1,2,3,5,8}, "W2: basic");
    check(ref_heap_sort({1,2,3,4,5}) == vector<int>{1,2,3,4,5}, "W2: sorted");
    check(ref_heap_sort({5,4,3,2,1}) == vector<int>{1,2,3,4,5}, "W2: reverse");
    check(ref_heap_sort({1}) == vector<int>{1}, "W2: single");
    check(ref_heap_sort({}) == vector<int>{}, "W2: empty");
    check(ref_heap_sort({3,1,3,1,2}) == vector<int>{1,1,2,3,3}, "W2: dups");
    check(ref_heap_sort({-3,-1,-2,0,2,1}) == vector<int>{-3,-2,-1,0,1,2}, "W2: negative");
}

void test_w3_last_stone_weight() {
    cout << "Testing W3: Last Stone Weight..." << endl;
    check(ref_last_stone_weight({2,7,4,1,8,1}) == 1, "W3: basic");
    check(ref_last_stone_weight({1}) == 1, "W3: single");
    check(ref_last_stone_weight({3,3}) == 0, "W3: equal");
    check(ref_last_stone_weight({3,7}) == 4, "W3: two diff");
    check(ref_last_stone_weight({5,5,5,5}) == 0, "W3: all equal");
    check(ref_last_stone_weight({10,4,2,10}) == 2, "W3: descending");
}

void test_w4_is_heap() {
    cout << "Testing W4: Check if Array is a Min-Heap..." << endl;
    check(ref_is_heap({1,3,2,7,6,5,4}) == true, "W4: valid");
    check(ref_is_heap({1,2,3,4,5,6,7}) == true, "W4: sorted");
    check(ref_is_heap({7,3,2,1,6,5,4}) == false, "W4: invalid");
    check(ref_is_heap({5}) == true, "W4: single");
    check(ref_is_heap({}) == true, "W4: empty");
    check(ref_is_heap({1,2}) == true, "W4: two valid");
    check(ref_is_heap({2,1}) == false, "W4: two invalid");
    check(ref_is_heap({1,2,3,4,5,6,7,8,9,10}) == true, "W4: large valid");
}

void test_p1_top_k_frequent() {
    cout << "Testing P1: Top K Frequent Elements..." << endl;
    check(ref_top_k_frequent({1,1,1,2,2,3}, 2) == vector<int>{1,2}, "P1: basic");
    check(ref_top_k_frequent({1}, 1) == vector<int>{1}, "P1: single");
    check(ref_top_k_frequent({5,5,5,5}, 1) == vector<int>{5}, "P1: all same");
    check(ref_top_k_frequent({4,1,-1,2,-1,2,3}, 2) == vector<int>{-1,2}, "P1: larger");
}

void test_p2_merge_k_sorted() {
    cout << "Testing P2: Merge K Sorted Arrays..." << endl;
    check(ref_merge_k_sorted({{1,4,7},{2,5,8},{3,6,9}}) ==
          vector<int>{1,2,3,4,5,6,7,8,9}, "P2: three arrays");
    check(ref_merge_k_sorted({{1,3,5},{2,4,6}}) ==
          vector<int>{1,2,3,4,5,6}, "P2: two arrays");
    check(ref_merge_k_sorted({{},{1}}) == vector<int>{1}, "P2: with empty");
    check(ref_merge_k_sorted({{},{}}) == vector<int>{}, "P2: all empty");
    check(ref_merge_k_sorted({{1,2,3}}) == vector<int>{1,2,3}, "P2: single");
    check(ref_merge_k_sorted({}) == vector<int>{}, "P2: no arrays");
    check(ref_merge_k_sorted({{1,3,5},{1,2,6},{2,4,8}}) ==
          vector<int>{1,1,2,2,3,4,5,6,8}, "P2: overlapping");
}

void test_p3_kth_smallest_matrix() {
    cout << "Testing P3: Kth Smallest in Sorted Matrix..." << endl;
    check(ref_kth_smallest_matrix({{1,5,9},{10,11,13},{12,13,15}}, 8) == 13, "P3: k=8");
    check(ref_kth_smallest_matrix({{-5}}, 1) == -5, "P3: single");
    check(ref_kth_smallest_matrix({{1,2},{3,4}}, 1) == 1, "P3: first");
    check(ref_kth_smallest_matrix({{1,2},{3,4}}, 4) == 4, "P3: last");
    check(ref_kth_smallest_matrix({{1,5,9},{10,11,13},{12,13,15}}, 5) == 11, "P3: k=5");
    check(ref_kth_smallest_matrix({{-5,-4},{-3,-2}}, 3) == -3, "P3: negative");
}

void test_p4_find_median() {
    cout << "Testing P4: Find Median from Data Stream..." << endl;
    check(doubles_equal(ref_find_median({5,15,1,3}), {5.0,10.0,5.0,4.0}), "P4: basic");
    check(doubles_equal(ref_find_median({2,3,4}), {2.0,2.5,3.0}), "P4: ascending");
    check(doubles_equal(ref_find_median({1}), {1.0}), "P4: single");
    check(doubles_equal(ref_find_median({1,2}), {1.0,1.5}), "P4: two");
    check(doubles_equal(ref_find_median({5,4,3,2,1}), {5.0,4.5,4.0,3.5,3.0}), "P4: desc");
    check(doubles_equal(ref_find_median({7,7,7,7}), {7.0,7.0,7.0,7.0}), "P4: same");
    check(doubles_equal(ref_find_median({-1,-2,-3}), {-1.0,-1.5,-2.0}), "P4: negative");
}

void test_p5_k_closest() {
    cout << "Testing P5: K Closest Points to Origin..." << endl;
    check(ref_k_closest({{1,3},{-2,2}}, 1) == vector<vector<int>>{{-2,2}}, "P5: basic");
    check(ref_k_closest({{3,3},{5,-1},{-2,4}}, 2) ==
          vector<vector<int>>{{3,3},{-2,4}}, "P5: two closest");
    {
        auto r = ref_k_closest({{1,0},{0,1}}, 2);
        check((int)r.size() == 2, "P5: all points");
    }
    check(ref_k_closest({{0,1}}, 1) == vector<vector<int>>{{0,1}}, "P5: single");
    check(ref_k_closest({{0,0},{1,1}}, 1) == vector<vector<int>>{{0,0}}, "P5: origin");
    {
        auto r = ref_k_closest({{1,2},{3,4},{0,1}}, 3);
        check((int)r.size() == 3 && r[0] == vector<int>{0,1}, "P5: k=n closest first");
    }
}

void test_c1_reorganize() {
    cout << "Testing C1: Reorganize String..." << endl;
    check(is_valid_reorganize("aab", ref_reorganize("aab")), "C1: aab");
    check(is_valid_reorganize("aaab", ref_reorganize("aaab")), "C1: impossible");
    check(is_valid_reorganize("a", ref_reorganize("a")), "C1: single");
    check(is_valid_reorganize("ab", ref_reorganize("ab")), "C1: two chars");
    check(is_valid_reorganize("aaabbbccc", ref_reorganize("aaabbbccc")), "C1: longer");
    check(is_valid_reorganize("aaaa", ref_reorganize("aaaa")), "C1: all same");
    check(is_valid_reorganize("aabbc", ref_reorganize("aabbc")), "C1: just possible");
}

void test_c2_task_scheduler() {
    cout << "Testing C2: Task Scheduler..." << endl;
    check(ref_task_scheduler({'A','A','A','B','B','B'}, 2) == 8, "C2: basic");
    check(ref_task_scheduler({'A','A','A','B','B','B'}, 0) == 6, "C2: no cooldown");
    check(ref_task_scheduler({'A','A','A','A','A','A','B','C','D','E'}, 2) == 16, "C2: large cd");
    check(ref_task_scheduler({'A'}, 2) == 1, "C2: single");
    check(ref_task_scheduler({'A','B','C','D'}, 2) == 4, "C2: all diff");
    check(ref_task_scheduler({'A','A'}, 2) == 4, "C2: two same");
    check(ref_task_scheduler({'A','A','A','B','B','C'}, 0) == 6, "C2: zero cd many");
}

void test_c3_sliding_window_max() {
    cout << "Testing C3: Sliding Window Maximum..." << endl;
    check(ref_sliding_window_max({1,3,-1,-3,5,3,6,7}, 3) ==
          vector<int>{3,3,5,5,6,7}, "C3: basic");
    check(ref_sliding_window_max({1}, 1) == vector<int>{1}, "C3: single");
    check(ref_sliding_window_max({1,-1}, 2) == vector<int>{1}, "C3: k=n");
    check(ref_sliding_window_max({1,2,3,4,5}, 3) ==
          vector<int>{3,4,5}, "C3: ascending");
    check(ref_sliding_window_max({5,4,3,2,1}, 3) ==
          vector<int>{5,4,3}, "C3: descending");
    check(ref_sliding_window_max({2,2,2,2}, 2) ==
          vector<int>{2,2,2}, "C3: all same");
    check(ref_sliding_window_max({4,3,5,4,2}, 1) ==
          vector<int>{4,3,5,4,2}, "C3: window 1");
}

// =====================================================================
// Main
// =====================================================================

int main() {
    cout << "Chapter 17: Heaps & Priority Queues — The VIP Line" << endl;
    cout << "===================================================" << endl << endl;

    test_w1_kth_largest();
    test_w2_heap_sort();
    test_w3_last_stone_weight();
    test_w4_is_heap();
    test_p1_top_k_frequent();
    test_p2_merge_k_sorted();
    test_p3_kth_smallest_matrix();
    test_p4_find_median();
    test_p5_k_closest();
    test_c1_reorganize();
    test_c2_task_scheduler();
    test_c3_sliding_window_max();

    cout << endl;
    if (tests_passed == tests_total) {
        cout << "All " << tests_total << " tests passed!" << endl;
    } else {
        cout << tests_passed << " / " << tests_total << " tests passed." << endl;
    }
    return (tests_passed == tests_total) ? 0 : 1;
}
