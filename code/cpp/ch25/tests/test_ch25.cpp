/*
 * Tests for Chapter 25: Dynamic Programming III — Subsequences & Knapsack
 * Build: g++ -std=c++17 -o /tmp/test_ch25 code/cpp/ch25/tests/test_ch25.cpp && /tmp/test_ch25
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <iostream>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named with ref_ prefix)
// =====================================================================

// W1: 0/1 Knapsack
int ref_knapsack(vector<int> w, vector<int> v, int cap) {
    vector<int> dp(cap + 1, 0);
    for (int i = 0; i < (int)w.size(); i++)
        for (int c = cap; c >= w[i]; c--)
            dp[c] = max(dp[c], dp[c - w[i]] + v[i]);
    return dp[cap];
}

// W2: Subset Sum
bool ref_subset_sum(vector<int> nums, int target) {
    vector<bool> dp(target + 1, false);
    dp[0] = true;
    for (int num : nums)
        for (int s = target; s >= num; s--)
            if (dp[s - num]) dp[s] = true;
    return dp[target];
}

// W3: Coin Change Min
int ref_coin_change_min(vector<int> coins, int amount) {
    vector<int> dp(amount + 1, amount + 1);
    dp[0] = 0;
    for (int a = 1; a <= amount; a++)
        for (int coin : coins)
            if (coin <= a) dp[a] = min(dp[a], dp[a - coin] + 1);
    return dp[amount] > amount ? -1 : dp[amount];
}

// W4: Coin Change Ways
int ref_coin_change_ways(vector<int> coins, int amount) {
    vector<int> dp(amount + 1, 0);
    dp[0] = 1;
    for (int coin : coins)
        for (int a = coin; a <= amount; a++)
            dp[a] += dp[a - coin];
    return dp[amount];
}

// W5: LCS
int ref_lcs(string a, string b) {
    int m = a.size(), n = b.size();
    vector<int> prev(n + 1, 0);
    for (int i = 1; i <= m; i++) {
        vector<int> curr(n + 1, 0);
        for (int j = 1; j <= n; j++) {
            if (a[i-1] == b[j-1]) curr[j] = prev[j-1] + 1;
            else curr[j] = max(prev[j], curr[j-1]);
        }
        prev = curr;
    }
    return prev[n];
}

// P1: Partition Equal Subset Sum
bool ref_partition(vector<int> nums) {
    int total = accumulate(nums.begin(), nums.end(), 0);
    if (total % 2 != 0) return false;
    int target = total / 2;
    vector<bool> dp(target + 1, false);
    dp[0] = true;
    for (int num : nums)
        for (int s = target; s >= num; s--)
            if (dp[s - num]) dp[s] = true;
    return dp[target];
}

// P2: Unbounded Knapsack
int ref_unbounded_knapsack(vector<int> w, vector<int> v, int cap) {
    vector<int> dp(cap + 1, 0);
    for (int i = 0; i < (int)w.size(); i++)
        for (int c = w[i]; c <= cap; c++)
            dp[c] = max(dp[c], dp[c - w[i]] + v[i]);
    return dp[cap];
}

// P3: Edit Distance
int ref_edit_distance(string a, string b) {
    int m = a.size(), n = b.size();
    vector<int> prev(n + 1);
    for (int j = 0; j <= n; j++) prev[j] = j;
    for (int i = 1; i <= m; i++) {
        vector<int> curr(n + 1);
        curr[0] = i;
        for (int j = 1; j <= n; j++) {
            if (a[i-1] == b[j-1]) curr[j] = prev[j-1];
            else curr[j] = 1 + min({prev[j], curr[j-1], prev[j-1]});
        }
        prev = curr;
    }
    return prev[n];
}

// P4: LIS
int ref_lis(vector<int> nums) {
    if (nums.empty()) return 0;
    int n = nums.size();
    vector<int> dp(n, 1);
    int best = 1;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++)
            if (nums[j] < nums[i]) dp[i] = max(dp[i], dp[j] + 1);
        best = max(best, dp[i]);
    }
    return best;
}

// P5: Distinct Subsequences
int ref_distinct_subseq(string s, string t) {
    int m = s.size(), n = t.size();
    vector<int> dp(n + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= m; i++)
        for (int j = min(i, n); j >= 1; j--)
            if (s[i-1] == t[j-1]) dp[j] += dp[j-1];
    return dp[n];
}

// P6: Wildcard Matching
bool ref_wildcard(string s, string p) {
    int m = s.size(), n = p.size();
    vector<bool> prev(n + 1, false);
    prev[0] = true;
    for (int j = 1; j <= n; j++) {
        if (p[j-1] == '*') prev[j] = prev[j-1];
        else break;
    }
    for (int i = 1; i <= m; i++) {
        vector<bool> curr(n + 1, false);
        for (int j = 1; j <= n; j++) {
            if (p[j-1] == '*') curr[j] = curr[j-1] || prev[j];
            else if (p[j-1] == '?' || s[i-1] == p[j-1]) curr[j] = prev[j-1];
        }
        prev = curr;
    }
    return prev[n];
}

// C1: Shortest Common Supersequence
string ref_scs(string str1, string str2) {
    int m = str1.size(), n = str2.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++) {
            if (str1[i-1] == str2[j-1]) dp[i][j] = dp[i-1][j-1] + 1;
            else dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
        }
    string result;
    int i = m, j = n;
    while (i > 0 && j > 0) {
        if (str1[i-1] == str2[j-1]) { result += str1[i-1]; i--; j--; }
        else if (dp[i-1][j] >= dp[i][j-1]) { result += str1[i-1]; i--; }
        else { result += str2[j-1]; j--; }
    }
    while (i > 0) { result += str1[i-1]; i--; }
    while (j > 0) { result += str2[j-1]; j--; }
    reverse(result.begin(), result.end());
    return result;
}

// C2: Rod Cutting
int ref_rod_cutting(vector<int> prices) {
    int n = prices.size();
    vector<int> dp(n + 1, 0);
    for (int len = 1; len <= n; len++)
        for (int k = 1; k <= len; k++)
            dp[len] = max(dp[len], dp[len - k] + prices[k - 1]);
    return dp[n];
}

// C3: Target Sum
int ref_target_sum(vector<int> nums, int target) {
    int total = accumulate(nums.begin(), nums.end(), 0);
    if ((total + target) % 2 != 0 || total + target < 0) return 0;
    int p = (total + target) / 2;
    if (p < 0) return 0;
    vector<int> dp(p + 1, 0);
    dp[0] = 1;
    for (int num : nums)
        for (int s = p; s >= num; s--)
            dp[s] += dp[s - num];
    return dp[p];
}

// C4: Longest String Chain
int ref_string_chain(vector<string> words) {
    sort(words.begin(), words.end(), [](const string& a, const string& b) {
        return a.size() < b.size();
    });
    unordered_map<string, int> dp;
    int best = 1;
    for (const string& word : words) {
        dp[word] = 1;
        for (int i = 0; i < (int)word.size(); i++) {
            string pred = word.substr(0, i) + word.substr(i + 1);
            if (dp.count(pred))
                dp[word] = max(dp[word], dp[pred] + 1);
        }
        best = max(best, dp[word]);
    }
    return best;
}

// C5: Min Insertions Palindrome
int ref_min_insertions(string s) {
    int n = s.size();
    string t(s.rbegin(), s.rend());
    vector<int> prev(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        vector<int> curr(n + 1, 0);
        for (int j = 1; j <= n; j++) {
            if (s[i-1] == t[j-1]) curr[j] = prev[j-1] + 1;
            else curr[j] = max(prev[j], curr[j-1]);
        }
        prev = curr;
    }
    return n - prev[n];
}

// =====================================================================
// Helper: check if s is a subsequence of t
// =====================================================================
bool is_subseq(const string& s, const string& t) {
    int si = 0;
    for (int ti = 0; ti < (int)t.size() && si < (int)s.size(); ti++)
        if (s[si] == t[ti]) si++;
    return si == (int)s.size();
}

// =====================================================================
// Test runner
// =====================================================================

int passed = 0, failed = 0;

void check(int expected, int actual, const string& msg) {
    if (expected == actual) { passed++; }
    else { failed++; cout << "FAIL: " << msg << " — expected " << expected << ", got " << actual << endl; }
}

void check_bool(bool expected, bool actual, const string& msg) {
    if (expected == actual) { passed++; }
    else { failed++; cout << "FAIL: " << msg << " — expected " << expected << ", got " << actual << endl; }
}

void check_scs(const string& s1, const string& s2, const string& result, int expectedLen, const string& msg) {
    if ((int)result.size() == expectedLen && is_subseq(s1, result) && is_subseq(s2, result)) { passed++; }
    else { failed++; cout << "FAIL: " << msg << " — got '" << result << "' (len " << result.size() << "), expected len " << expectedLen << endl; }
}

int main() {
    cout << "Chapter 25: Dynamic Programming III — Subsequences & Knapsack" << endl;
    cout << "================================================================" << endl << endl;

    // W1: 0/1 Knapsack
    check(9, ref_knapsack({1,3,4,5}, {1,4,5,7}, 7), "W1: basic");
    check(7, ref_knapsack({2,3,4,5}, {3,4,5,6}, 5), "W1: tight");
    check(0, ref_knapsack({10}, {10}, 5), "W1: too heavy");
    check(10, ref_knapsack({5}, {10}, 5), "W1: exact fit");
    check(0, ref_knapsack({}, {}, 10), "W1: empty");

    // W2: Subset Sum
    check_bool(true, ref_subset_sum({3,34,4,12,5,2}, 9), "W2: basic true");
    check_bool(false, ref_subset_sum({3,34,4,12,5,2}, 30), "W2: basic false");
    check_bool(true, ref_subset_sum({1,5,11,5}, 11), "W2: sum 11");
    check_bool(true, ref_subset_sum({1,2,3}, 0), "W2: target 0");

    // W3: Coin Change Min
    check(3, ref_coin_change_min({1,5,11}, 15), "W3: basic");
    check(-1, ref_coin_change_min({2}, 3), "W3: impossible");
    check(0, ref_coin_change_min({1}, 0), "W3: zero");
    check(3, ref_coin_change_min({1,2,5}, 11), "W3: classic");

    // W4: Coin Change Ways
    check(4, ref_coin_change_ways({1,2,5}, 5), "W4: basic");
    check(0, ref_coin_change_ways({2}, 3), "W4: impossible");
    check(1, ref_coin_change_ways({10}, 10), "W4: exact");
    check(1, ref_coin_change_ways({1,2}, 0), "W4: zero amount");

    // W5: LCS
    check(3, ref_lcs("abcde", "ace"), "W5: basic");
    check(3, ref_lcs("abc", "abc"), "W5: identical");
    check(0, ref_lcs("abc", "def"), "W5: no common");
    check(2, ref_lcs("oxcpqrsvwf", "shmtulqrypy"), "W5: longer");

    // P1: Partition Equal Subset Sum
    check_bool(true, ref_partition({1,5,11,5}), "P1: true");
    check_bool(false, ref_partition({1,2,3,5}), "P1: false");
    check_bool(true, ref_partition({1,1}), "P1: pair");
    check_bool(false, ref_partition({1}), "P1: single");

    // P2: Unbounded Knapsack
    check(27, ref_unbounded_knapsack({2,4,6}, {5,11,13}, 10), "P2: basic");
    check(110, ref_unbounded_knapsack({1,3,4,5}, {10,40,50,70}, 8), "P2: basic2");
    check(21, ref_unbounded_knapsack({3}, {7}, 9), "P2: single item");

    // P3: Edit Distance
    check(3, ref_edit_distance("horse", "ros"), "P3: basic");
    check(5, ref_edit_distance("intention", "execution"), "P3: longer");
    check(3, ref_edit_distance("", "abc"), "P3: empty source");
    check(0, ref_edit_distance("abc", "abc"), "P3: identical");

    // P4: LIS
    check(4, ref_lis({10,9,2,5,3,7,101,18}), "P4: basic");
    check(4, ref_lis({0,1,0,3,2,3}), "P4: mixed");
    check(1, ref_lis({7,7,7,7,7}), "P4: all same");
    check(5, ref_lis({1,2,3,4,5}), "P4: increasing");
    check(1, ref_lis({5,4,3,2,1}), "P4: decreasing");

    // P5: Distinct Subsequences
    check(3, ref_distinct_subseq("rabbbit", "rabbit"), "P5: rabbbit");
    check(5, ref_distinct_subseq("babgbag", "bag"), "P5: babgbag");
    check(3, ref_distinct_subseq("aaa", "a"), "P5: aaa");

    // P6: Wildcard Matching
    check_bool(false, ref_wildcard("aa", "a"), "P6: no match");
    check_bool(true, ref_wildcard("aa", "*"), "P6: star all");
    check_bool(false, ref_wildcard("cb", "?a"), "P6: question fail");
    check_bool(true, ref_wildcard("adceb", "*a*b"), "P6: star match");
    check_bool(true, ref_wildcard("", ""), "P6: empty both");
    check_bool(true, ref_wildcard("", "*"), "P6: empty star");

    // C1: Shortest Common Supersequence
    check_scs("abac", "cab", ref_scs("abac", "cab"), 5, "C1: basic");
    check_scs("aaaaaaaa", "aaaaaaaa", ref_scs("aaaaaaaa", "aaaaaaaa"), 8, "C1: identical");
    check_scs("abc", "xyz", ref_scs("abc", "xyz"), 6, "C1: no common");

    // C2: Rod Cutting
    check(22, ref_rod_cutting({1,5,8,9,10,17,17,20}), "C2: basic");
    check(24, ref_rod_cutting({3,5,8,9,10,17,17,20}), "C2: basic2");
    check(1, ref_rod_cutting({1}), "C2: single");

    // C3: Target Sum
    check(5, ref_target_sum({1,1,1,1,1}, 3), "C3: basic");
    check(1, ref_target_sum({1}, 1), "C3: single");
    check(2, ref_target_sum({1,0}, 1), "C3: with zero");
    check(0, ref_target_sum({1}, 2), "C3: impossible");

    // C4: Longest String Chain
    check(4, ref_string_chain({"a","b","ba","bca","bda","bdca"}), "C4: basic");
    check(5, ref_string_chain({"xbc","pcxbcf","xb","cxbc","pcxbc"}), "C4: longer");
    check(1, ref_string_chain({"abc"}), "C4: single");

    // C5: Min Insertions Palindrome
    check(0, ref_min_insertions("zzazz"), "C5: palindrome");
    check(2, ref_min_insertions("mbadm"), "C5: basic");
    check(5, ref_min_insertions("leetcode"), "C5: longer");
    check(0, ref_min_insertions("a"), "C5: single");

    cout << endl;
    if (failed == 0) {
        printf("All %d ch25 C++ tests passed!\n", passed);
    } else {
        printf("%d passed, %d failed.\n", passed, failed);
        return 1;
    }
    return 0;
}
