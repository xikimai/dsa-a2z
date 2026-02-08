/*
 * Tests for Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 * Build: g++ -std=c++17 -o /tmp/test_ch15 code/cpp/ch15/tests/test_ch15.cpp && /tmp/test_ch15
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions
// =====================================================================

// W1: Pair Sum in Sorted Array
vector<int> ref_pair_sum(vector<int> arr, int target) {
    int left = 0, right = (int)arr.size() - 1;
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) return {arr[left], arr[right]};
        else if (sum < target) left++;
        else right--;
    }
    return {-1, -1};
}

// W2: Remove Duplicates from Sorted
vector<int> ref_remove_dupes(vector<int> arr) {
    if (arr.size() <= 1) return arr;
    int slow = 0;
    for (int fast = 1; fast < (int)arr.size(); fast++) {
        if (arr[fast] != arr[slow]) { slow++; arr[slow] = arr[fast]; }
    }
    return vector<int>(arr.begin(), arr.begin() + slow + 1);
}

// W3: Max Sum Fixed Window
int ref_max_sum_window(vector<int> arr, int k) {
    if ((int)arr.size() < k) return 0;
    int windowSum = 0;
    for (int i = 0; i < k; i++) windowSum += arr[i];
    int best = windowSum;
    for (int i = k; i < (int)arr.size(); i++) {
        windowSum += arr[i] - arr[i - k];
        best = max(best, windowSum);
    }
    return best;
}

// W4: Move Zeros
vector<int> ref_move_zeros(vector<int> arr) {
    int slow = 0;
    for (int fast = 0; fast < (int)arr.size(); fast++) {
        if (arr[fast] != 0) { swap(arr[slow], arr[fast]); slow++; }
    }
    return arr;
}

// P1: Container With Most Water
int ref_container(vector<int> h) {
    int left = 0, right = (int)h.size() - 1, best = 0;
    while (left < right) {
        best = max(best, (right - left) * min(h[left], h[right]));
        if (h[left] < h[right]) left++;
        else right--;
    }
    return best;
}

// P2: Longest Substring No Repeat
int ref_longest_substr(string s) {
    unordered_map<char, int> ci;
    int left = 0, best = 0;
    for (int right = 0; right < (int)s.size(); right++) {
        if (ci.count(s[right]) && ci[s[right]] >= left)
            left = ci[s[right]] + 1;
        ci[s[right]] = right;
        best = max(best, right - left + 1);
    }
    return best;
}

// P3: Minimum Window Substring
string ref_min_window(string s, string t) {
    if (s.empty() || t.empty()) return "";
    unordered_map<char, int> need;
    for (char c : t) need[c]++;
    int required = need.size(), formed = 0;
    unordered_map<char, int> window;
    int left = 0, bestLen = INT_MAX, bestStart = 0;
    for (int right = 0; right < (int)s.size(); right++) {
        window[s[right]]++;
        if (need.count(s[right]) && window[s[right]] == need[s[right]]) formed++;
        while (formed == required) {
            if (right - left + 1 < bestLen) { bestLen = right - left + 1; bestStart = left; }
            window[s[left]]--;
            if (need.count(s[left]) && window[s[left]] < need[s[left]]) formed--;
            left++;
        }
    }
    return bestLen == INT_MAX ? "" : s.substr(bestStart, bestLen);
}

// P4: Subarray Sum Equals K
int ref_subarray_sum(vector<int> arr, int k) {
    int left = 0, currentSum = 0, count = 0;
    for (int right = 0; right < (int)arr.size(); right++) {
        currentSum += arr[right];
        while (currentSum > k && left <= right) { currentSum -= arr[left]; left++; }
        if (currentSum == k) count++;
    }
    return count;
}

// P5: Dutch National Flag
vector<int> ref_dutch_flag(vector<int> arr) {
    if (arr.size() <= 1) return arr;
    int low = 0, mid = 0, high = (int)arr.size() - 1;
    while (mid <= high) {
        if (arr[mid] == 0) { swap(arr[low], arr[mid]); low++; mid++; }
        else if (arr[mid] == 1) { mid++; }
        else { swap(arr[mid], arr[high]); high--; }
    }
    return arr;
}

// C1: Three Sum
vector<vector<int>> ref_three_sum(vector<int> nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    int n = nums.size();
    for (int i = 0; i < n - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        if (nums[i] > 0) break;
        int target = -nums[i];
        int left = i + 1, right = n - 1;
        while (left < right) {
            int ts = nums[left] + nums[right];
            if (ts == target) {
                result.push_back({nums[i], nums[left], nums[right]});
                while (left < right && nums[left] == nums[left + 1]) left++;
                while (left < right && nums[right] == nums[right - 1]) right--;
                left++; right--;
            } else if (ts < target) left++;
            else right--;
        }
    }
    return result;
}

// C2: Trapping Rain Water
int ref_trap_water(vector<int> h) {
    if ((int)h.size() < 3) return 0;
    int left = 0, right = (int)h.size() - 1;
    int lm = h[left], rm = h[right], water = 0;
    while (left < right) {
        if (lm <= rm) { left++; lm = max(lm, h[left]); water += lm - h[left]; }
        else { right--; rm = max(rm, h[right]); water += rm - h[right]; }
    }
    return water;
}

// C3: Longest Repeating Character Replacement
int ref_char_replacement(string s, int k) {
    unordered_map<char, int> freq;
    int left = 0, maxFreq = 0, best = 0;
    for (int right = 0; right < (int)s.size(); right++) {
        freq[s[right]]++;
        maxFreq = max(maxFreq, freq[s[right]]);
        while ((right - left + 1) - maxFreq > k) { freq[s[left]]--; left++; }
        best = max(best, right - left + 1);
    }
    return best;
}

// C4: Fruit Into Baskets
int ref_fruit_baskets(vector<int> fruits) {
    unordered_map<int, int> freq;
    int left = 0, best = 0;
    for (int right = 0; right < (int)fruits.size(); right++) {
        freq[fruits[right]]++;
        while ((int)freq.size() > 2) {
            int lf = fruits[left]; freq[lf]--;
            if (freq[lf] == 0) freq.erase(lf);
            left++;
        }
        best = max(best, right - left + 1);
    }
    return best;
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
    cout << "Testing W1: Pair Sum in Sorted Array..." << endl;
    check(ref_pair_sum({1,3,5,8,12,15}, 13) == vector<int>{1,12}, "basic");
    check(ref_pair_sum({1,2,3,4,5}, 6) == vector<int>{1,5}, "first+last");
    check(ref_pair_sum({1,2,3,4,5}, 10) == vector<int>{-1,-1}, "no pair");
    check(ref_pair_sum({3,7}, 10) == vector<int>{3,7}, "two elements");
    check(ref_pair_sum({-5,-3,0,2,8}, -8) == vector<int>{-5,-3}, "negatives");
    check(ref_pair_sum({}, 5) == vector<int>{-1,-1}, "empty");
    check(ref_pair_sum({5}, 5) == vector<int>{-1,-1}, "single");
    check(ref_pair_sum({1,3,5,7,9}, 10) == vector<int>{1,9}, "smallest first");
}

void test_w2() {
    cout << "Testing W2: Remove Duplicates from Sorted..." << endl;
    check(ref_remove_dupes({1,1,2}) == vector<int>{1,2}, "basic");
    check(ref_remove_dupes({0,0,1,1,1,2,2,3,3,4}) == vector<int>{0,1,2,3,4}, "many");
    check(ref_remove_dupes({1,2,3}) == vector<int>{1,2,3}, "no dupes");
    check(ref_remove_dupes({5,5,5,5}) == vector<int>{5}, "all same");
    check(ref_remove_dupes({1}) == vector<int>{1}, "single");
    check(ref_remove_dupes({}) == vector<int>{}, "empty");
    check(ref_remove_dupes({-3,-3,-1,0,0,2}) == vector<int>{-3,-1,0,2}, "negatives");
}

void test_w3() {
    cout << "Testing W3: Max Sum Fixed Window..." << endl;
    check(ref_max_sum_window({2,1,5,1,3,2}, 3) == 9, "basic");
    check(ref_max_sum_window({1,2,3}, 3) == 6, "k==len");
    check(ref_max_sum_window({1,2}, 3) == 0, "k>len");
    check(ref_max_sum_window({5}, 1) == 5, "single");
    check(ref_max_sum_window({-1,-2,-3,-4}, 2) == -3, "all neg");
    check(ref_max_sum_window({4,-1,2,1,6,-5}, 3) == 9, "mixed");
    check(ref_max_sum_window({}, 1) == 0, "empty");
}

void test_w4() {
    cout << "Testing W4: Move Zeros..." << endl;
    check(ref_move_zeros({0,1,0,3,12}) == vector<int>{1,3,12,0,0}, "basic");
    check(ref_move_zeros({0}) == vector<int>{0}, "single zero");
    check(ref_move_zeros({1,2,3}) == vector<int>{1,2,3}, "no zeros");
    check(ref_move_zeros({0,0,0}) == vector<int>{0,0,0}, "all zeros");
    check(ref_move_zeros({0,0,1}) == vector<int>{1,0,0}, "zeros at start");
    check(ref_move_zeros({}) == vector<int>{}, "empty");
    check(ref_move_zeros({0,5,0,3,0,1}) == vector<int>{5,3,1,0,0,0}, "mixed");
}

void test_p1() {
    cout << "Testing P1: Container With Most Water..." << endl;
    check(ref_container({1,8,6,2,5,4,8,3,7}) == 49, "basic");
    check(ref_container({1,1}) == 1, "two elements");
    check(ref_container({4,3,2,1}) == 4, "decreasing");
    check(ref_container({1,2,3,4}) == 4, "increasing");
    check(ref_container({5,5,5,5}) == 15, "equal");
    check(ref_container({10,1,1,1,10}) == 40, "tall ends");
}

void test_p2() {
    cout << "Testing P2: Longest Substring No Repeat..." << endl;
    check(ref_longest_substr("abcabcbb") == 3, "basic");
    check(ref_longest_substr("bbbbb") == 1, "all same");
    check(ref_longest_substr("pwwkew") == 3, "alternating");
    check(ref_longest_substr("") == 0, "empty");
    check(ref_longest_substr("a") == 1, "single");
    check(ref_longest_substr("abcdef") == 6, "all unique");
    check(ref_longest_substr("ab cd") == 5, "with space");
}

void test_p3() {
    cout << "Testing P3: Minimum Window Substring..." << endl;
    check(ref_min_window("ADOBECODEBANC", "ABC") == "BANC", "basic");
    check(ref_min_window("a", "a") == "a", "exact");
    check(ref_min_window("a", "aa") == "", "no window");
    check(ref_min_window("ab", "abc") == "", "t longer");
    check(ref_min_window("abc", "abc") == "abc", "entire string");
    check(ref_min_window("AABC", "AAB") == "AAB", "dupes in t");
    check(ref_min_window("", "a") == "", "empty s");
}

void test_p4() {
    cout << "Testing P4: Subarray Sum Equals K..." << endl;
    check(ref_subarray_sum({1,1,1}, 2) == 2, "basic");
    check(ref_subarray_sum({1,2,3}, 3) == 2, "exact");
    check(ref_subarray_sum({5}, 5) == 1, "single match");
    check(ref_subarray_sum({1,2,3}, 10) == 0, "no match");
    check(ref_subarray_sum({1,1,1,1,1}, 3) == 3, "all ones");
    check(ref_subarray_sum({2,3,1,2,4,3}, 7) == 2, "larger");
}

void test_p5() {
    cout << "Testing P5: Dutch National Flag..." << endl;
    check(ref_dutch_flag({2,0,2,1,1,0}) == vector<int>{0,0,1,1,2,2}, "basic");
    check(ref_dutch_flag({2,0,1}) == vector<int>{0,1,2}, "three");
    check(ref_dutch_flag({0,0,1,1,2,2}) == vector<int>{0,0,1,1,2,2}, "already sorted");
    check(ref_dutch_flag({2,2,1,1,0,0}) == vector<int>{0,0,1,1,2,2}, "reverse");
    check(ref_dutch_flag({1,1,1}) == vector<int>{1,1,1}, "all same");
    check(ref_dutch_flag({0}) == vector<int>{0}, "single");
    check(ref_dutch_flag({}) == vector<int>{}, "empty");
    check(ref_dutch_flag({2,0,2,0}) == vector<int>{0,0,2,2}, "no ones");
}

void test_c1() {
    cout << "Testing C1: Three Sum..." << endl;
    vector<vector<int>> expected1 = {{-1,-1,2},{-1,0,1}};
    check(ref_three_sum({-1,0,1,2,-1,-4}) == expected1, "basic");
    check(ref_three_sum({0,1,1}).empty(), "no triplet");
    vector<vector<int>> expected3 = {{0,0,0}};
    check(ref_three_sum({0,0,0}) == expected3, "all zeros");
    check(ref_three_sum({0,0,0,0}) == expected3, "four zeros");
    check(ref_three_sum({1,2,3}).empty(), "no result");
    check((int)ref_three_sum({-2,-1,0,1,2,3}).size() == 3, "multiple triplets count");
}

void test_c2() {
    cout << "Testing C2: Trapping Rain Water..." << endl;
    check(ref_trap_water({0,1,0,2,1,0,1,3,2,1,2,1}) == 6, "basic");
    check(ref_trap_water({4,2,0,3,2,5}) == 9, "v shape");
    check(ref_trap_water({3,3,3}) == 0, "flat");
    check(ref_trap_water({1,2,3,4}) == 0, "ascending");
    check(ref_trap_water({4,3,2,1}) == 0, "descending");
    check(ref_trap_water({}) == 0, "empty");
    check(ref_trap_water({1,2}) == 0, "two elements");
    check(ref_trap_water({5}) == 0, "single");
}

void test_c3() {
    cout << "Testing C3: Longest Repeating Char Replacement..." << endl;
    check(ref_char_replacement("ABAB", 2) == 4, "basic");
    check(ref_char_replacement("AABABBA", 1) == 4, "limited");
    check(ref_char_replacement("AAAA", 0) == 4, "no replacement");
    check(ref_char_replacement("ABCDE", 2) == 3, "all different");
    check(ref_char_replacement("A", 0) == 1, "single");
    check(ref_char_replacement("AB", 2) == 2, "k==len");
    check(ref_char_replacement("AAABBC", 2) == 5, "long run");
}

void test_c4() {
    cout << "Testing C4: Fruit Into Baskets..." << endl;
    check(ref_fruit_baskets({1,2,1}) == 3, "basic");
    check(ref_fruit_baskets({0,1,2,2}) == 3, "three types");
    check(ref_fruit_baskets({1,2,3,2,2}) == 4, "longer");
    check(ref_fruit_baskets({1,1,1,1}) == 4, "single type");
    check(ref_fruit_baskets({1,2,1,2,1}) == 5, "alternating");
    check(ref_fruit_baskets({5}) == 1, "single");
    check(ref_fruit_baskets({1,2}) == 2, "two");
    check(ref_fruit_baskets({3,3,3,1,2,1,1,2,3,3,4}) == 5, "many types");
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
