/*
 * Tests for Chapter 5: Collections
 * Build: g++ -std=c++17 -o test_ch05 code/cpp/ch05/tests/test_ch05.cpp && ./test_ch05
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <iostream>
#include <map>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named to avoid collisions)
// =====================================================================

// --- Warmup 01: Second Largest ---
int solve_second_largest(vector<int> nums) {
    if (nums.size() < 2) return -1;

    int first = INT_MIN;
    int second = INT_MIN;

    for (int x : nums) {
        if (x > first) {
            second = first;
            first = x;
        } else if (x > second && x != first) {
            second = x;
        }
    }
    return (second == INT_MIN) ? -1 : second;
}

// --- Warmup 02: Reverse List ---
vector<int> solve_reverse_list(vector<int> nums) {
    int left = 0;
    int right = (int)nums.size() - 1;
    while (left < right) {
        swap(nums[left], nums[right]);
        left++;
        right--;
    }
    return nums;
}

// --- Warmup 03: Count Vowels ---
int solve_count_vowels(string s) {
    unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
    int count = 0;
    for (char c : s) {
        if (vowels.count(tolower(c))) {
            count++;
        }
    }
    return count;
}

// --- Warmup 04: Remove Duplicates ---
vector<int> solve_remove_duplicates(vector<int> nums) {
    if (nums.empty()) return {};
    vector<int> result;
    result.push_back(nums[0]);
    for (int i = 1; i < (int)nums.size(); i++) {
        if (nums[i] != nums[i - 1]) {
            result.push_back(nums[i]);
        }
    }
    return result;
}

// --- Warmup 05: Character Frequency ---
unordered_map<char, int> solve_char_frequency(string s) {
    unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }
    return freq;
}

// --- Warmup 06: Move Zeros ---
vector<int> solve_move_zeros(vector<int> nums) {
    int write = 0;
    for (int i = 0; i < (int)nums.size(); i++) {
        if (nums[i] != 0) {
            nums[write] = nums[i];
            write++;
        }
    }
    while (write < (int)nums.size()) {
        nums[write] = 0;
        write++;
    }
    return nums;
}

// --- Practice 01: Union Arrays ---
vector<int> solve_union_arrays(vector<int> a, vector<int> b) {
    unordered_set<int> seen;
    for (int x : a) seen.insert(x);
    for (int x : b) seen.insert(x);
    vector<int> result(seen.begin(), seen.end());
    sort(result.begin(), result.end());
    return result;
}

// --- Practice 02: Anagram Check ---
bool solve_anagram_check(string s1, string s2) {
    if (s1.size() != s2.size()) return false;
    int freq[26] = {};
    for (int i = 0; i < (int)s1.size(); i++) {
        freq[tolower(s1[i]) - 'a']++;
        freq[tolower(s2[i]) - 'a']--;
    }
    for (int i = 0; i < 26; i++) {
        if (freq[i] != 0) return false;
    }
    return true;
}

// --- Practice 03: Two Sum ---
vector<int> solve_two_sum(vector<int> nums, int target) {
    unordered_map<int, int> seen;
    for (int i = 0; i < (int)nums.size(); i++) {
        int complement = target - nums[i];
        if (seen.count(complement)) {
            return {seen[complement], i};
        }
        seen[nums[i]] = i;
    }
    return {-1, -1};
}

// --- Practice 04: Sort by Frequency ---
vector<int> solve_sort_by_frequency(vector<int> nums) {
    unordered_map<int, int> freq;
    for (int x : nums) freq[x]++;

    vector<int> result = nums;
    sort(result.begin(), result.end(), [&freq](int a, int b) {
        if (freq[a] != freq[b]) return freq[a] > freq[b];
        return a < b;
    });
    return result;
}

// --- Practice 05: Longest Common Prefix ---
string solve_longest_common_prefix(vector<string> strs) {
    if (strs.empty()) return "";
    for (int i = 0; i < (int)strs[0].size(); i++) {
        char c = strs[0][i];
        for (int j = 1; j < (int)strs.size(); j++) {
            if (i >= (int)strs[j].size() || strs[j][i] != c) {
                return strs[0].substr(0, i);
            }
        }
    }
    return strs[0];
}

// --- Challenge 01: Find Duplicates ---
vector<int> solve_find_duplicates(vector<int> nums) {
    unordered_set<int> seen;
    unordered_set<int> dups;
    for (int x : nums) {
        if (seen.count(x)) {
            dups.insert(x);
        }
        seen.insert(x);
    }
    vector<int> result(dups.begin(), dups.end());
    sort(result.begin(), result.end());
    return result;
}

// --- Challenge 02: Group Anagrams ---
vector<vector<string>> solve_group_anagrams(vector<string> strs) {
    map<string, vector<string>> groups;
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
    sort(result.begin(), result.end(), [](const vector<string>& a, const vector<string>& b) {
        return a[0] < b[0];
    });
    return result;
}

// --- Challenge 03: Rotate Array ---
vector<int> solve_rotate_array(vector<int> nums, int k) {
    int n = (int)nums.size();
    if (n == 0) return nums;
    k = k % n;
    if (k == 0) return nums;
    reverse(nums.begin(), nums.end());
    reverse(nums.begin(), nums.begin() + k);
    reverse(nums.begin() + k, nums.end());
    return nums;
}

// =====================================================================
// Test functions
// =====================================================================

void test_warmup_01_second_largest() {
    assert(solve_second_largest({3, 1, 4, 1, 5}) == 4);
    assert(solve_second_largest({7, 7, 7}) == -1);
    assert(solve_second_largest({1, 2}) == 1);
    assert(solve_second_largest({10}) == -1);
    assert(solve_second_largest({1, 2, 3, 4, 5}) == 4);
    assert(solve_second_largest({5, 5, 4}) == 4);
    cout << "  test_warmup_01_second_largest........ PASS" << endl;
}

void test_warmup_02_reverse_list() {
    assert(solve_reverse_list({1, 2, 3, 4, 5}) == (vector<int>{5, 4, 3, 2, 1}));
    assert(solve_reverse_list({1}) == (vector<int>{1}));
    assert(solve_reverse_list({}) == (vector<int>{}));
    assert(solve_reverse_list({1, 2}) == (vector<int>{2, 1}));
    cout << "  test_warmup_02_reverse_list.......... PASS" << endl;
}

void test_warmup_03_count_vowels() {
    assert(solve_count_vowels("Hello World") == 3);
    assert(solve_count_vowels("aeiou") == 5);
    assert(solve_count_vowels("xyz") == 0);
    assert(solve_count_vowels("") == 0);
    assert(solve_count_vowels("AEIOU") == 5);
    assert(solve_count_vowels("AeIoU") == 5);
    cout << "  test_warmup_03_count_vowels.......... PASS" << endl;
}

void test_warmup_04_remove_duplicates() {
    assert(solve_remove_duplicates({1, 1, 2}) == (vector<int>{1, 2}));
    assert(solve_remove_duplicates({1, 1, 1, 2, 2, 3}) == (vector<int>{1, 2, 3}));
    assert(solve_remove_duplicates({1}) == (vector<int>{1}));
    assert(solve_remove_duplicates({}) == (vector<int>{}));
    assert(solve_remove_duplicates({1, 2, 3}) == (vector<int>{1, 2, 3}));
    cout << "  test_warmup_04_remove_duplicates..... PASS" << endl;
}

void test_warmup_05_char_frequency() {
    auto r1 = solve_char_frequency("aab");
    assert(r1['a'] == 2);
    assert(r1['b'] == 1);
    assert((int)r1.size() == 2);

    auto r2 = solve_char_frequency("");
    assert(r2.empty());

    auto r3 = solve_char_frequency("aaa");
    assert(r3['a'] == 3);
    assert((int)r3.size() == 1);
    cout << "  test_warmup_05_char_frequency........ PASS" << endl;
}

void test_warmup_06_move_zeros() {
    assert(solve_move_zeros({0, 1, 0, 3, 12}) == (vector<int>{1, 3, 12, 0, 0}));
    assert(solve_move_zeros({1, 2, 3}) == (vector<int>{1, 2, 3}));
    assert(solve_move_zeros({0, 0, 0}) == (vector<int>{0, 0, 0}));
    assert(solve_move_zeros({}) == (vector<int>{}));
    assert(solve_move_zeros({0}) == (vector<int>{0}));
    cout << "  test_warmup_06_move_zeros............ PASS" << endl;
}

void test_practice_01_union_arrays() {
    assert(solve_union_arrays({1, 2, 3}, {3, 4, 5}) == (vector<int>{1, 2, 3, 4, 5}));
    assert(solve_union_arrays({1, 1, 2}, {2, 3}) == (vector<int>{1, 2, 3}));
    assert(solve_union_arrays({}, {1, 2}) == (vector<int>{1, 2}));
    assert(solve_union_arrays({1, 2}, {}) == (vector<int>{1, 2}));
    assert(solve_union_arrays({}, {}) == (vector<int>{}));
    cout << "  test_practice_01_union_arrays........ PASS" << endl;
}

void test_practice_02_anagram_check() {
    assert(solve_anagram_check("listen", "silent") == true);
    assert(solve_anagram_check("hello", "world") == false);
    assert(solve_anagram_check("Listen", "Silent") == true);
    assert(solve_anagram_check("abc", "ab") == false);
    assert(solve_anagram_check("", "") == true);
    cout << "  test_practice_02_anagram_check....... PASS" << endl;
}

void test_practice_03_two_sum() {
    assert(solve_two_sum({2, 7, 11, 15}, 9) == (vector<int>{0, 1}));
    assert(solve_two_sum({3, 3}, 6) == (vector<int>{0, 1}));
    assert(solve_two_sum({1, 2, 3}, 10) == (vector<int>{-1, -1}));
    assert(solve_two_sum({1, 5, 3, 7}, 8) == (vector<int>{1, 2}));
    cout << "  test_practice_03_two_sum............. PASS" << endl;
}

void test_practice_04_sort_by_frequency() {
    assert(solve_sort_by_frequency({2, 3, 1, 3, 2}) == (vector<int>{2, 2, 3, 3, 1}));
    assert(solve_sort_by_frequency({1}) == (vector<int>{1}));
    assert(solve_sort_by_frequency({5, 5, 4, 4, 3}) == (vector<int>{4, 4, 5, 5, 3}));
    assert(solve_sort_by_frequency({1, 1, 2, 2, 3, 3}) == (vector<int>{1, 1, 2, 2, 3, 3}));
    cout << "  test_practice_04_sort_by_frequency... PASS" << endl;
}

void test_practice_05_longest_common_prefix() {
    assert(solve_longest_common_prefix({"flower", "flow", "flight"}) == "fl");
    assert(solve_longest_common_prefix({"dog", "racecar", "car"}) == "");
    assert(solve_longest_common_prefix({"abc"}) == "abc");
    assert(solve_longest_common_prefix({"", "abc"}) == "");
    assert(solve_longest_common_prefix({"abc", "abc", "abc"}) == "abc");
    cout << "  test_practice_05_longest_common_pfx.. PASS" << endl;
}

void test_challenge_01_find_duplicates() {
    assert(solve_find_duplicates({4, 3, 2, 7, 8, 2, 3, 1}) == (vector<int>{2, 3}));
    assert(solve_find_duplicates({1, 2, 3}) == (vector<int>{}));
    assert(solve_find_duplicates({1, 1, 1, 1}) == (vector<int>{1}));
    assert(solve_find_duplicates({1, 2, 1, 3, 2}) == (vector<int>{1, 2}));
    cout << "  test_challenge_01_find_duplicates.... PASS" << endl;
}

void test_challenge_02_group_anagrams() {
    auto result = solve_group_anagrams({"eat", "tea", "tan", "ate", "nat", "bat"});
    assert((int)result.size() == 3);
    assert(result[0] == (vector<string>{"ate", "eat", "tea"}));
    assert(result[1] == (vector<string>{"bat"}));
    assert(result[2] == (vector<string>{"nat", "tan"}));

    auto result2 = solve_group_anagrams({"a"});
    assert((int)result2.size() == 1);
    assert(result2[0] == (vector<string>{"a"}));

    auto result3 = solve_group_anagrams({""});
    assert((int)result3.size() == 1);
    assert(result3[0] == (vector<string>{""}));
    cout << "  test_challenge_02_group_anagrams..... PASS" << endl;
}

void test_challenge_03_rotate_array() {
    assert(solve_rotate_array({1, 2, 3, 4, 5, 6, 7}, 3) == (vector<int>{5, 6, 7, 1, 2, 3, 4}));
    assert(solve_rotate_array({1, 2, 3}, 1) == (vector<int>{3, 1, 2}));
    assert(solve_rotate_array({1, 2, 3}, 5) == (vector<int>{2, 3, 1}));
    assert(solve_rotate_array({1}, 10) == (vector<int>{1}));
    assert(solve_rotate_array({}, 3) == (vector<int>{}));
    assert(solve_rotate_array({1, 2, 3}, 0) == (vector<int>{1, 2, 3}));
    cout << "  test_challenge_03_rotate_array....... PASS" << endl;
}

// =====================================================================
// Main -- run all tests
// =====================================================================
int main() {
    cout << "Testing Chapter 5..." << endl;
    cout << endl;

    cout << "--- Warmup Problems ---" << endl;
    test_warmup_01_second_largest();
    test_warmup_02_reverse_list();
    test_warmup_03_count_vowels();
    test_warmup_04_remove_duplicates();
    test_warmup_05_char_frequency();
    test_warmup_06_move_zeros();
    cout << endl;

    cout << "--- Practice Problems ---" << endl;
    test_practice_01_union_arrays();
    test_practice_02_anagram_check();
    test_practice_03_two_sum();
    test_practice_04_sort_by_frequency();
    test_practice_05_longest_common_prefix();
    cout << endl;

    cout << "--- Challenge Problems ---" << endl;
    test_challenge_01_find_duplicates();
    test_challenge_02_group_anagrams();
    test_challenge_03_rotate_array();
    cout << endl;

    cout << "All tests passed!" << endl;
    return 0;
}
