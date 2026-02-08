/*
 * Tests for Chapter 11: Hashing — The Secret Decoder Ring
 * Build: g++ -std=c++17 -o /tmp/test_ch11 code/cpp/ch11/tests/test_ch11.cpp && /tmp/test_ch11
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named with ref_ prefix)
// =====================================================================

// --- W1: Frequency Count ---
vector<vector<int>> ref_frequency_count(vector<int> arr) {
    unordered_map<int, int> freq;
    for (int x : arr) freq[x]++;
    vector<vector<int>> result;
    for (auto& [val, cnt] : freq) {
        result.push_back({val, cnt});
    }
    sort(result.begin(), result.end());
    return result;
}

// --- W2: Highest and Lowest Frequency ---
vector<int> ref_highest_lowest_freq(vector<int> arr) {
    unordered_map<int, int> freq;
    for (int x : arr) freq[x]++;
    int high_elem = 0, high_cnt = 0;
    int low_elem = 0, low_cnt = INT_MAX;
    for (auto& [val, cnt] : freq) {
        if (cnt > high_cnt) { high_cnt = cnt; high_elem = val; }
        if (cnt < low_cnt) { low_cnt = cnt; low_elem = val; }
    }
    return {high_elem, low_elem};
}

// --- W3: First Non-Repeating Character ---
string ref_first_non_repeating(string s) {
    unordered_map<char, int> freq;
    for (char c : s) freq[c]++;
    for (char c : s) {
        if (freq[c] == 1) return string(1, c);
    }
    return "_";
}

// --- W4: Valid Anagram ---
bool ref_valid_anagram(string s1, string s2) {
    if (s1.size() != s2.size()) return false;
    unordered_map<char, int> freq;
    for (char c : s1) freq[c]++;
    for (char c : s2) freq[c]--;
    for (auto& [ch, cnt] : freq) {
        if (cnt != 0) return false;
    }
    return true;
}

// --- W5: Intersection of Two Arrays ---
vector<int> ref_intersection(vector<int> a, vector<int> b) {
    unordered_set<int> set_a(a.begin(), a.end());
    unordered_set<int> found;
    for (int x : b) {
        if (set_a.count(x)) found.insert(x);
    }
    vector<int> result(found.begin(), found.end());
    sort(result.begin(), result.end());
    return result;
}

// --- P1: Group Anagrams ---
vector<vector<string>> ref_group_anagrams(vector<string> strs) {
    unordered_map<string, vector<string>> groups;
    for (const string& s : strs) {
        string key = s;
        sort(key.begin(), key.end());
        groups[key].push_back(s);
    }
    vector<vector<string>> result;
    for (auto& [key, group] : groups) {
        sort(group.begin(), group.end());
        result.push_back(group);
    }
    sort(result.begin(), result.end());
    return result;
}

// --- P2: Missing Number ---
int ref_missing_number(vector<int> nums) {
    unordered_set<int> seen(nums.begin(), nums.end());
    int n = nums.size();
    for (int i = 0; i <= n; i++) {
        if (!seen.count(i)) return i;
    }
    return -1;
}

// --- P3: Longest Subarray with Sum K ---
int ref_longest_subarray_sum_k(vector<int> arr, int k) {
    unordered_map<long long, int> first_seen;
    first_seen[0] = -1;
    long long prefix_sum = 0;
    int max_len = 0;
    for (int i = 0; i < (int)arr.size(); i++) {
        prefix_sum += arr[i];
        long long need = prefix_sum - k;
        if (first_seen.count(need)) {
            max_len = max(max_len, i - first_seen[need]);
        }
        if (!first_seen.count(prefix_sum)) {
            first_seen[prefix_sum] = i;
        }
    }
    return max_len;
}

// --- P4: Count Subarrays with Sum K ---
int ref_count_subarrays_sum_k(vector<int> arr, int k) {
    unordered_map<long long, int> prefix_count;
    prefix_count[0] = 1;
    long long prefix_sum = 0;
    int count = 0;
    for (int x : arr) {
        prefix_sum += x;
        long long need = prefix_sum - k;
        if (prefix_count.count(need)) {
            count += prefix_count[need];
        }
        prefix_count[prefix_sum]++;
    }
    return count;
}

// --- P5: Sort Characters by Frequency ---
string ref_sort_chars_by_freq(string s) {
    unordered_map<char, int> freq;
    for (char c : s) freq[c]++;
    vector<pair<char, int>> chars;
    for (auto& [ch, cnt] : freq) {
        chars.push_back({ch, cnt});
    }
    sort(chars.begin(), chars.end(), [](const pair<char,int>& a, const pair<char,int>& b) {
        if (a.second != b.second) return a.second > b.second;
        return a.first < b.first;
    });
    string result;
    for (auto& [ch, cnt] : chars) {
        result += string(cnt, ch);
    }
    return result;
}

// --- C1: Missing Number Four Ways ---
int ref_missing_sort(vector<int> nums) {
    sort(nums.begin(), nums.end());
    for (int i = 0; i < (int)nums.size(); i++) {
        if (nums[i] != i) return i;
    }
    return (int)nums.size();
}

int ref_missing_xor(vector<int> nums) {
    int n = nums.size();
    int result = n;
    for (int i = 0; i < n; i++) {
        result ^= i ^ nums[i];
    }
    return result;
}

int ref_missing_math(vector<int> nums) {
    int n = nums.size();
    long long expected = (long long)n * (n + 1) / 2;
    long long actual = 0;
    for (int x : nums) actual += x;
    return (int)(expected - actual);
}

int ref_missing_hash(vector<int> nums) {
    unordered_set<int> seen(nums.begin(), nums.end());
    int n = nums.size();
    for (int i = 0; i <= n; i++) {
        if (!seen.count(i)) return i;
    }
    return -1;
}

// --- C2: Longest Consecutive Sequence ---
int ref_longest_consecutive(vector<int> nums) {
    if (nums.empty()) return 0;
    unordered_set<int> s(nums.begin(), nums.end());
    int best = 0;
    for (int num : s) {
        if (!s.count(num - 1)) {
            int current = num;
            int length = 1;
            while (s.count(current + 1)) {
                current++;
                length++;
            }
            best = max(best, length);
        }
    }
    return best;
}

// --- C3: Repeating and Missing Number ---
vector<int> ref_repeating_missing(vector<int> nums) {
    int n = nums.size();
    unordered_map<int, int> freq;
    for (int x : nums) freq[x]++;
    int repeating = 0, missing = 0;
    for (int i = 1; i <= n; i++) {
        if (freq[i] == 2) repeating = i;
        if (freq[i] == 0) missing = i;
    }
    return {repeating, missing};
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

// =====================================================================
// Test functions
// =====================================================================

void test_w1_frequency_count() {
    cout << "Testing W1: Frequency Count..." << endl;
    check(ref_frequency_count({1,2,2,3,3,3}) == vector<vector<int>>{{1,1},{2,2},{3,3}},
          "basic frequency count");
    check(ref_frequency_count({5}) == vector<vector<int>>{{5,1}},
          "single element");
    check(ref_frequency_count({}) == vector<vector<int>>{},
          "empty array");
    check(ref_frequency_count({3,1,2,1}) == vector<vector<int>>{{1,2},{2,1},{3,1}},
          "unsorted input");
    check(ref_frequency_count({4,4,4,4}) == vector<vector<int>>{{4,4}},
          "all same elements");
}

void test_w2_highest_lowest_freq() {
    cout << "Testing W2: Highest and Lowest Frequency..." << endl;
    check(ref_highest_lowest_freq({1,2,2,3,3,3}) == vector<int>{3,1},
          "basic high/low freq");
    check(ref_highest_lowest_freq({10,10,10,20,20,30}) == vector<int>{10,30},
          "three different frequencies");
    check(ref_highest_lowest_freq({5}) == vector<int>{5,5},
          "single element (same high and low)");
    check(ref_highest_lowest_freq({1,1,2,2,2,2,3,3,3}) == vector<int>{2,1},
          "multiple frequencies");
    check(ref_highest_lowest_freq({7,7,8,8,8,9,9,9,9}) == vector<int>{9,7},
          "increasing frequencies");
}

void test_w3_first_non_repeating() {
    cout << "Testing W3: First Non-Repeating Character..." << endl;
    check(ref_first_non_repeating("aabbcdd") == "c",
          "middle non-repeating");
    check(ref_first_non_repeating("aabb") == "_",
          "no non-repeating");
    check(ref_first_non_repeating("abcabc") == "_",
          "all repeat");
    check(ref_first_non_repeating("aabbc") == "c",
          "last char non-repeating");
    check(ref_first_non_repeating("a") == "a",
          "single character");
    check(ref_first_non_repeating("") == "_",
          "empty string");
}

void test_w4_valid_anagram() {
    cout << "Testing W4: Valid Anagram..." << endl;
    check(ref_valid_anagram("listen", "silent") == true,
          "classic anagram");
    check(ref_valid_anagram("hello", "world") == false,
          "not an anagram");
    check(ref_valid_anagram("", "") == true,
          "empty strings");
    check(ref_valid_anagram("a", "a") == true,
          "single char match");
    check(ref_valid_anagram("ab", "ba") == true,
          "two char anagram");
    check(ref_valid_anagram("abc", "abd") == false,
          "different characters");
    check(ref_valid_anagram("aab", "aba") == true,
          "repeated chars anagram");
}

void test_w5_intersection() {
    cout << "Testing W5: Intersection of Two Arrays..." << endl;
    check(ref_intersection({1,2,2,1}, {2,2}) == vector<int>{2},
          "basic intersection");
    check(ref_intersection({4,9,5}, {9,4,9,8,4}) == vector<int>{4,9},
          "multiple common elements");
    check(ref_intersection({1,2,3}, {4,5,6}) == vector<int>{},
          "no intersection");
    check(ref_intersection({}, {1,2}) == vector<int>{},
          "empty first array");
    check(ref_intersection({1,1,1}, {1}) == vector<int>{1},
          "duplicates collapse to one");
}

void test_p1_group_anagrams() {
    cout << "Testing P1: Group Anagrams..." << endl;
    check(ref_group_anagrams({"eat","tea","tan","ate","nat","bat"}) ==
          vector<vector<string>>{{"ate","eat","tea"},{"bat"},{"nat","tan"}},
          "classic anagram groups");
    check(ref_group_anagrams({""}) == vector<vector<string>>{{""}},
          "single empty string");
    check(ref_group_anagrams({"a"}) == vector<vector<string>>{{"a"}},
          "single char");
    check(ref_group_anagrams({"abc","bca","cab","xyz","zxy"}) ==
          vector<vector<string>>{{"abc","bca","cab"},{"xyz","zxy"}},
          "two groups");
    check(ref_group_anagrams({}) == vector<vector<string>>{},
          "empty input");
}

void test_p2_missing_number() {
    cout << "Testing P2: Missing Number..." << endl;
    check(ref_missing_number({3,0,1}) == 2, "missing 2");
    check(ref_missing_number({0,1}) == 2, "missing at end");
    check(ref_missing_number({9,6,4,2,3,5,7,0,1}) == 8, "missing 8");
    check(ref_missing_number({0}) == 1, "missing 1");
    check(ref_missing_number({1}) == 0, "missing 0");
}

void test_p3_longest_subarray_sum_k() {
    cout << "Testing P3: Longest Subarray with Sum K..." << endl;
    check(ref_longest_subarray_sum_k({1,2,3,1,1,1,1}, 3) == 3,
          "basic longest subarray");
    check(ref_longest_subarray_sum_k({-1,1,1}, 1) == 3,
          "negative numbers");
    check(ref_longest_subarray_sum_k({1,2,3}, 10) == 0,
          "no valid subarray");
    check(ref_longest_subarray_sum_k({1,-1,1,-1,1}, 0) == 4,
          "alternating signs");
    check(ref_longest_subarray_sum_k({2,0,0,3}, 3) == 3,
          "zeros in array");
    check(ref_longest_subarray_sum_k({1}, 1) == 1,
          "single element match");
}

void test_p4_count_subarrays_sum_k() {
    cout << "Testing P4: Count Subarrays with Sum K..." << endl;
    check(ref_count_subarrays_sum_k({1,1,1}, 2) == 2,
          "basic count");
    check(ref_count_subarrays_sum_k({1,2,3}, 3) == 2,
          "two subarrays");
    check(ref_count_subarrays_sum_k({1}, 0) == 0,
          "no matching subarray");
    check(ref_count_subarrays_sum_k({1,-1,0}, 0) == 3,
          "negative and zero");
    check(ref_count_subarrays_sum_k({0,0,0}, 0) == 6,
          "all zeros");
    check(ref_count_subarrays_sum_k({1}, 1) == 1,
          "single element match");
}

void test_p5_sort_chars_by_freq() {
    cout << "Testing P5: Sort Characters by Frequency..." << endl;
    check(ref_sort_chars_by_freq("tree") == "eert",
          "basic frequency sort");
    check(ref_sort_chars_by_freq("cccaaa") == "aaaccc",
          "tiebreak alphabetically");
    check(ref_sort_chars_by_freq("aab") == "aab",
          "two chars different freq");
    check(ref_sort_chars_by_freq("hello") == "lleho",
          "multiple characters");
    check(ref_sort_chars_by_freq("x") == "x",
          "single character");
    check(ref_sort_chars_by_freq("") == "",
          "empty string");
}

void test_c1_missing_number_four_ways() {
    cout << "Testing C1: Missing Number Four Ways..." << endl;
    // Test all four methods on same inputs
    vector<pair<vector<int>, int>> cases = {
        {{3,0,1}, 2},
        {{0,1}, 2},
        {{9,6,4,2,3,5,7,0,1}, 8},
        {{1}, 0},
        {{0}, 1}
    };
    for (auto& [nums, expected] : cases) {
        string label = "nums size=" + to_string(nums.size()) + " expected=" + to_string(expected);
        check(ref_missing_sort(nums) == expected, "sort: " + label);
        check(ref_missing_xor(nums) == expected, "xor: " + label);
        check(ref_missing_math(nums) == expected, "math: " + label);
        check(ref_missing_hash(nums) == expected, "hash: " + label);
    }
}

void test_c2_longest_consecutive() {
    cout << "Testing C2: Longest Consecutive Sequence..." << endl;
    check(ref_longest_consecutive({100,4,200,1,3,2}) == 4,
          "basic consecutive");
    check(ref_longest_consecutive({0,3,7,2,5,8,4,6,0,1}) == 9,
          "long sequence with duplicate");
    check(ref_longest_consecutive({}) == 0,
          "empty array");
    check(ref_longest_consecutive({1}) == 1,
          "single element");
    check(ref_longest_consecutive({1,1,1}) == 1,
          "all duplicates");
    check(ref_longest_consecutive({9,1,4,7,3,-1,0,5,8,2,6}) == 11,
          "negative numbers included");
}

void test_c3_repeating_missing() {
    cout << "Testing C3: Repeating and Missing Number..." << endl;
    check(ref_repeating_missing({3,1,2,5,3}) == vector<int>{3,4},
          "basic repeating/missing");
    check(ref_repeating_missing({1,1}) == vector<int>{1,2},
          "smallest case - repeat 1");
    check(ref_repeating_missing({2,2}) == vector<int>{2,1},
          "smallest case - repeat 2");
    check(ref_repeating_missing({4,3,6,2,1,1}) == vector<int>{1,5},
          "repeat at start");
    check(ref_repeating_missing({1,2,3,4,4}) == vector<int>{4,5},
          "repeat at end");
}

// =====================================================================
// Main
// =====================================================================

int main() {
    test_w1_frequency_count();
    test_w2_highest_lowest_freq();
    test_w3_first_non_repeating();
    test_w4_valid_anagram();
    test_w5_intersection();
    test_p1_group_anagrams();
    test_p2_missing_number();
    test_p3_longest_subarray_sum_k();
    test_p4_count_subarrays_sum_k();
    test_p5_sort_chars_by_freq();
    test_c1_missing_number_four_ways();
    test_c2_longest_consecutive();
    test_c3_repeating_missing();

    cout << endl;
    if (tests_passed == tests_total) {
        cout << "All " << tests_total << " tests passed!" << endl;
    } else {
        cout << tests_passed << " / " << tests_total << " tests passed." << endl;
    }
    return (tests_passed == tests_total) ? 0 : 1;
}
