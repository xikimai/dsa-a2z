/*
 * Tests for Chapter 23: Dynamic Programming I — The Foundation
 * Build: g++ -std=c++17 -o /tmp/test_ch23 code/cpp/ch23/tests/test_ch23.cpp && /tmp/test_ch23
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named with ref_ prefix)
// =====================================================================

// W1: Climbing Stairs
int ref_climbing_stairs(int n) {
    if (n <= 2) return n;
    int p2 = 1, p1 = 2;
    for (int i = 3; i <= n; i++) { int c = p1 + p2; p2 = p1; p1 = c; }
    return p1;
}

// W2: Fibonacci
int ref_fibonacci(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) { int c = a + b; a = b; b = c; }
    return b;
}

// W3: Min Cost Climbing
int ref_min_cost_climbing(vector<int> cost) {
    int n = cost.size();
    int p2 = 0, p1 = 0;
    for (int i = 2; i <= n; i++) {
        int c = min(p1 + cost[i-1], p2 + cost[i-2]);
        p2 = p1; p1 = c;
    }
    return p1;
}

// W4: House Robber
int ref_house_robber(vector<int> nums) {
    int n = nums.size();
    if (n == 0) return 0;
    if (n == 1) return nums[0];
    int p2 = nums[0], p1 = max(nums[0], nums[1]);
    for (int i = 2; i < n; i++) { int c = max(p1, p2 + nums[i]); p2 = p1; p1 = c; }
    return p1;
}

// W5: Max Subarray
int ref_max_subarray(vector<int> nums) {
    int cur = nums[0], best = nums[0];
    for (int i = 1; i < (int)nums.size(); i++) {
        cur = max(cur + nums[i], nums[i]);
        best = max(best, cur);
    }
    return best;
}

// P1: Frog Jump K
int ref_frog_jump_k(vector<int> costs, int k) {
    int n = costs.size();
    if (n <= 1) return n == 1 ? costs[0] : 0;
    vector<int> dp(n, INT_MAX);
    dp[0] = costs[0];
    for (int i = 1; i < n; i++) {
        for (int j = 1; j <= min(k, i); j++) dp[i] = min(dp[i], dp[i-j]);
        dp[i] += costs[i];
    }
    return dp[n-1];
}

// P2: House Robber II
int ref_house_robber_ii(vector<int> nums) {
    int n = nums.size();
    if (n == 0) return 0;
    if (n == 1) return nums[0];
    if (n == 2) return max(nums[0], nums[1]);
    auto rob = [&](int lo, int hi) {
        int p2 = nums[lo], p1 = max(nums[lo], nums[lo+1]);
        for (int i = lo+2; i <= hi; i++) { int c = max(p1, p2+nums[i]); p2 = p1; p1 = c; }
        return p1;
    };
    return max(rob(0, n-2), rob(1, n-1));
}

// P3: Decode Ways
int ref_decode_ways(string s) {
    if (s.empty() || s[0] == '0') return 0;
    int n = s.size();
    int p2 = 1, p1 = 1;
    for (int i = 2; i <= n; i++) {
        int c = 0;
        if (s[i-1] != '0') c += p1;
        int td = stoi(s.substr(i-2, 2));
        if (td >= 10 && td <= 26) c += p2;
        p2 = p1; p1 = c;
    }
    return p1;
}

// P4: Stock I
int ref_stock_i(vector<int> prices) {
    if (prices.empty()) return 0;
    int mn = prices[0], profit = 0;
    for (int i = 1; i < (int)prices.size(); i++) {
        profit = max(profit, prices[i] - mn);
        mn = min(mn, prices[i]);
    }
    return profit;
}

// P5: Stock II
int ref_stock_ii(vector<int> prices) {
    int profit = 0;
    for (int i = 1; i < (int)prices.size(); i++)
        if (prices[i] > prices[i-1]) profit += prices[i] - prices[i-1];
    return profit;
}

// P6: Tribonacci
int ref_tribonacci(int n) {
    if (n == 0) return 0;
    if (n <= 2) return 1;
    int a = 0, b = 1, c = 1;
    for (int i = 3; i <= n; i++) { int next = a+b+c; a = b; b = c; c = next; }
    return c;
}

// C1: Stock III
int ref_stock_iii(vector<int> prices) {
    if (prices.empty()) return 0;
    int b1 = -prices[0], s1 = 0, b2 = -prices[0], s2 = 0;
    for (int i = 1; i < (int)prices.size(); i++) {
        b1 = max(b1, -prices[i]);
        s1 = max(s1, b1 + prices[i]);
        b2 = max(b2, s1 - prices[i]);
        s2 = max(s2, b2 + prices[i]);
    }
    return s2;
}

// C2: Stock Cooldown
int ref_stock_cooldown(vector<int> prices) {
    if (prices.empty()) return 0;
    int held = -prices[0], sold = 0, rest = 0;
    for (int i = 1; i < (int)prices.size(); i++) {
        int ph = held;
        held = max(held, rest - prices[i]);
        rest = max(rest, sold);
        sold = ph + prices[i];
    }
    return max(sold, rest);
}

// C3: Stock Fee
int ref_stock_fee(vector<int> prices, int fee) {
    if (prices.empty()) return 0;
    int cash = 0, hold = -prices[0];
    for (int i = 1; i < (int)prices.size(); i++) {
        cash = max(cash, hold + prices[i] - fee);
        hold = max(hold, cash - prices[i]);
    }
    return cash;
}

// C4: House Robber III
int ref_house_robber_iii(vector<int> tree) {
    if (tree.empty()) return 0;
    function<pair<int,int>(int)> dfs = [&](int idx) -> pair<int,int> {
        if (idx >= (int)tree.size() || tree[idx] == -1) return {0, 0};
        auto [lr, ls] = dfs(2*idx+1);
        auto [rr, rs] = dfs(2*idx+2);
        int rob = tree[idx] + ls + rs;
        int skip = max(lr, ls) + max(rr, rs);
        return {rob, skip};
    };
    auto [r, s] = dfs(0);
    return max(r, s);
}

// C5: LIS
int ref_lis(vector<int> nums) {
    if (nums.empty()) return 0;
    int n = nums.size();
    vector<int> dp(n, 1);
    int best = 1;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++)
            if (nums[j] < nums[i]) dp[i] = max(dp[i], dp[j]+1);
        best = max(best, dp[i]);
    }
    return best;
}

// =====================================================================
// Test runner
// =====================================================================

int passed = 0, failed = 0;

void check(int expected, int actual, const string& msg) {
    if (expected == actual) {
        passed++;
    } else {
        failed++;
        cout << "FAIL: " << msg << " — expected " << expected << ", got " << actual << endl;
    }
}

int main() {
    cout << "Chapter 23: Dynamic Programming I — The Foundation" << endl;
    cout << "====================================================" << endl << endl;

    // W1
    check(1, ref_climbing_stairs(1), "W1: n=1");
    check(2, ref_climbing_stairs(2), "W1: n=2");
    check(3, ref_climbing_stairs(3), "W1: n=3");
    check(8, ref_climbing_stairs(5), "W1: n=5");
    check(89, ref_climbing_stairs(10), "W1: n=10");

    // W2
    check(0, ref_fibonacci(0), "W2: n=0");
    check(1, ref_fibonacci(1), "W2: n=1");
    check(55, ref_fibonacci(10), "W2: n=10");
    check(6765, ref_fibonacci(20), "W2: n=20");

    // W3
    check(15, ref_min_cost_climbing({10,15,20}), "W3: [10,15,20]");
    check(6, ref_min_cost_climbing({1,100,1,1,1,100,1,1,100,1}), "W3: long");
    check(10, ref_min_cost_climbing({10,15}), "W3: [10,15]");
    check(10, ref_min_cost_climbing({5,5,5,5}), "W3: [5,5,5,5]");
    check(6, ref_min_cost_climbing({1,2,3,4,5}), "W3: [1,2,3,4,5]");

    // W4
    check(4, ref_house_robber({1,2,3,1}), "W4: [1,2,3,1]");
    check(12, ref_house_robber({2,7,9,3,1}), "W4: [2,7,9,3,1]");
    check(5, ref_house_robber({5}), "W4: [5]");
    check(2, ref_house_robber({1,2}), "W4: [1,2]");
    check(4, ref_house_robber({2,1,1,2}), "W4: [2,1,1,2]");

    // W5
    check(6, ref_max_subarray({-2,1,-3,4,-1,2,1,-5,4}), "W5: mixed");
    check(1, ref_max_subarray({1}), "W5: [1]");
    check(23, ref_max_subarray({5,4,-1,7,8}), "W5: all positive");
    check(-1, ref_max_subarray({-1,-2,-3}), "W5: all negative");

    // P1
    check(3, ref_frog_jump_k({0,3,2,6,1}, 2), "P1: k=2");
    check(20, ref_frog_jump_k({10,20,30,10}, 3), "P1: k=3");
    check(5, ref_frog_jump_k({5}, 1), "P1: single");
    check(100, ref_frog_jump_k({10,30,40,20}, 1), "P1: k=1");
    check(60, ref_frog_jump_k({10,30,40,20}, 2), "P1: k=2 v2");

    // P2
    check(3, ref_house_robber_ii({2,3,2}), "P2: [2,3,2]");
    check(4, ref_house_robber_ii({1,2,3,1}), "P2: [1,2,3,1]");
    check(3, ref_house_robber_ii({1,2,3}), "P2: [1,2,3]");
    check(5, ref_house_robber_ii({5}), "P2: [5]");
    check(2, ref_house_robber_ii({1,2}), "P2: [1,2]");
    check(103, ref_house_robber_ii({1,3,1,3,100}), "P2: [1,3,1,3,100]");

    // P3
    check(2, ref_decode_ways("12"), "P3: 12");
    check(3, ref_decode_ways("226"), "P3: 226");
    check(0, ref_decode_ways("06"), "P3: 06");
    check(1, ref_decode_ways("1"), "P3: 1");
    check(1, ref_decode_ways("10"), "P3: 10");
    check(1, ref_decode_ways("27"), "P3: 27");
    check(3, ref_decode_ways("1234"), "P3: 1234");

    // P4
    check(5, ref_stock_i({7,1,5,3,6,4}), "P4: basic");
    check(0, ref_stock_i({7,6,4,3,1}), "P4: decreasing");
    check(0, ref_stock_i({1}), "P4: single");
    check(1, ref_stock_i({1,2}), "P4: [1,2]");

    // P5
    check(7, ref_stock_ii({7,1,5,3,6,4}), "P5: basic");
    check(4, ref_stock_ii({1,2,3,4,5}), "P5: increasing");
    check(0, ref_stock_ii({7,6,4,3,1}), "P5: decreasing");
    check(0, ref_stock_ii({5}), "P5: single");

    // P6
    check(0, ref_tribonacci(0), "P6: n=0");
    check(1, ref_tribonacci(1), "P6: n=1");
    check(1, ref_tribonacci(2), "P6: n=2");
    check(4, ref_tribonacci(4), "P6: n=4");
    check(1389537, ref_tribonacci(25), "P6: n=25");

    // C1
    check(6, ref_stock_iii({3,3,5,0,0,3,1,4}), "C1: basic");
    check(4, ref_stock_iii({1,2,3,4,5}), "C1: increasing");
    check(0, ref_stock_iii({7,6,4,3,1}), "C1: decreasing");
    check(0, ref_stock_iii({1}), "C1: single");

    // C2
    check(3, ref_stock_cooldown({1,2,3,0,2}), "C2: basic");
    check(0, ref_stock_cooldown({1}), "C2: single");
    check(1, ref_stock_cooldown({1,2}), "C2: [1,2]");
    check(0, ref_stock_cooldown({5,4,3,2,1}), "C2: decreasing");
    check(6, ref_stock_cooldown({1,4,2,7}), "C2: alternating");

    // C3
    check(8, ref_stock_fee({1,3,2,8,4,9}, 2), "C3: basic");
    check(6, ref_stock_fee({1,3,7,5,10,3}, 3), "C3: basic2");
    check(0, ref_stock_fee({5}, 1), "C3: single");
    check(0, ref_stock_fee({7,6,4,3,1}, 2), "C3: no profit");
    check(4, ref_stock_fee({1,2,3,4,5}, 0), "C3: zero fee");

    // C4
    check(7, ref_house_robber_iii({3,2,3,-1,3,-1,1}), "C4: basic");
    check(9, ref_house_robber_iii({3,4,5,1,3,-1,1}), "C4: basic2");
    check(1, ref_house_robber_iii({1}), "C4: single");
    check(5, ref_house_robber_iii({1,2,3}), "C4: two levels");

    // C5
    check(4, ref_lis({10,9,2,5,3,7,101,18}), "C5: basic");
    check(4, ref_lis({0,1,0,3,2,3}), "C5: mixed");
    check(1, ref_lis({7,7,7,7}), "C5: all same");
    check(5, ref_lis({1,2,3,4,5}), "C5: increasing");
    check(1, ref_lis({5,4,3,2,1}), "C5: decreasing");

    cout << endl;
    if (failed == 0) {
        cout << "All " << passed << " tests passed!" << endl;
    } else {
        cout << passed << " passed, " << failed << " failed." << endl;
        return 1;
    }
    return 0;
}
