/*
 * Tests for Chapter 18: Greedy Algorithms — The Smart Shortcut
 * Build: g++ -std=c++17 -o /tmp/test_ch18 code/cpp/ch18/tests/test_ch18.cpp && /tmp/test_ch18
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

// W1: Assign Cookies
int ref_w1(vector<int> greed, vector<int> cookies) {
    sort(greed.begin(), greed.end());
    sort(cookies.begin(), cookies.end());
    int child = 0, cookie = 0;
    while (child < (int)greed.size() && cookie < (int)cookies.size()) {
        if (cookies[cookie] >= greed[child]) child++;
        cookie++;
    }
    return child;
}

// W2: Jump Game
bool ref_w2(vector<int> nums) {
    int maxReach = 0;
    for (int i = 0; i < (int)nums.size(); i++) {
        if (i > maxReach) return false;
        maxReach = max(maxReach, i + nums[i]);
    }
    return true;
}

// W3: Best Buy Sell Stock
int ref_w3(vector<int> prices) {
    if (prices.size() < 2) return 0;
    int minPrice = prices[0], maxProfit = 0;
    for (int i = 1; i < (int)prices.size(); i++) {
        maxProfit = max(maxProfit, prices[i] - minPrice);
        minPrice = min(minPrice, prices[i]);
    }
    return maxProfit;
}

// W4: Lemonade Change
bool ref_w4(vector<int> bills) {
    int fives = 0, tens = 0;
    for (int bill : bills) {
        if (bill == 5) fives++;
        else if (bill == 10) { if (fives == 0) return false; fives--; tens++; }
        else {
            if (tens > 0 && fives > 0) { tens--; fives--; }
            else if (fives >= 3) fives -= 3;
            else return false;
        }
    }
    return true;
}

// P1: Activity Selection
int ref_p1(vector<vector<int>> activities) {
    if (activities.empty()) return 0;
    sort(activities.begin(), activities.end(),
         [](auto& a, auto& b) { return a[1] < b[1]; });
    int count = 0, lastEnd = 0;
    for (auto& act : activities) {
        if (act[0] >= lastEnd) { count++; lastEnd = act[1]; }
    }
    return count;
}

// P2: Fractional Knapsack
double ref_p2(int capacity, vector<pair<int,int>> items) {
    if (capacity == 0 || items.empty()) return 0.0;
    sort(items.begin(), items.end(), [](auto& a, auto& b) {
        return (double)a.second / a.first > (double)b.second / b.first;
    });
    double totalValue = 0.0;
    int remaining = capacity;
    for (auto& [w, v] : items) {
        if (remaining <= 0) break;
        int take = min(w, remaining);
        totalValue += take * ((double)v / w);
        remaining -= take;
    }
    return totalValue;
}

// P3: Merge Intervals
vector<vector<int>> ref_p3(vector<vector<int>> intervals) {
    if (intervals.empty()) return {};
    sort(intervals.begin(), intervals.end());
    vector<vector<int>> merged = {intervals[0]};
    for (int i = 1; i < (int)intervals.size(); i++) {
        if (intervals[i][0] <= merged.back()[1]) {
            merged.back()[1] = max(merged.back()[1], intervals[i][1]);
        } else {
            merged.push_back(intervals[i]);
        }
    }
    return merged;
}

// P4: Non-overlapping Intervals
int ref_p4(vector<vector<int>> intervals) {
    if (intervals.empty()) return 0;
    sort(intervals.begin(), intervals.end(),
         [](auto& a, auto& b) { return a[1] < b[1]; });
    int keep = 0, lastEnd = INT_MIN;
    for (auto& iv : intervals) {
        if (iv[0] >= lastEnd) { keep++; lastEnd = iv[1]; }
    }
    return (int)intervals.size() - keep;
}

// P5: Jump Game II
int ref_p5(vector<int> nums) {
    if (nums.size() <= 1) return 0;
    int jumps = 0, currentEnd = 0, farthest = 0;
    for (int i = 0; i < (int)nums.size() - 1; i++) {
        farthest = max(farthest, i + nums[i]);
        if (i == currentEnd) {
            jumps++;
            currentEnd = farthest;
            if (currentEnd >= (int)nums.size() - 1) break;
        }
    }
    return jumps;
}

// C1: Job Sequencing
pair<int,int> ref_c1(vector<vector<int>> jobs) {
    if (jobs.empty()) return {0, 0};
    sort(jobs.begin(), jobs.end(),
         [](auto& a, auto& b) { return a[2] > b[2]; });
    int maxDeadline = 0;
    for (auto& j : jobs) maxDeadline = max(maxDeadline, j[1]);
    vector<bool> slots(maxDeadline + 1, false);
    int count = 0, totalProfit = 0;
    for (auto& job : jobs) {
        for (int t = job[1]; t >= 1; t--) {
            if (!slots[t]) {
                slots[t] = true;
                count++;
                totalProfit += job[2];
                break;
            }
        }
    }
    return {count, totalProfit};
}

// C2: Gas Station
int ref_c2(vector<int> gas, vector<int> cost) {
    int totalGas = 0, totalCost = 0;
    for (int i = 0; i < (int)gas.size(); i++) {
        totalGas += gas[i]; totalCost += cost[i];
    }
    if (totalGas < totalCost) return -1;
    int start = 0, tank = 0;
    for (int i = 0; i < (int)gas.size(); i++) {
        tank += gas[i] - cost[i];
        if (tank < 0) { start = i + 1; tank = 0; }
    }
    return start;
}

// C3: Min Platforms
int ref_c3(vector<int> arr, vector<int> dep) {
    if (arr.empty()) return 0;
    sort(arr.begin(), arr.end());
    sort(dep.begin(), dep.end());
    int plat = 0, maxPlat = 0;
    int i = 0, j = 0, n = arr.size();
    while (i < n) {
        if (arr[i] <= dep[j]) { plat++; maxPlat = max(maxPlat, plat); i++; }
        else { plat--; j++; }
    }
    return maxPlat;
}

// C4: Candy
int ref_c4(vector<int> ratings) {
    int n = ratings.size();
    if (n == 0) return 0;
    vector<int> candies(n, 1);
    for (int i = 1; i < n; i++)
        if (ratings[i] > ratings[i-1]) candies[i] = candies[i-1] + 1;
    for (int i = n-2; i >= 0; i--)
        if (ratings[i] > ratings[i+1]) candies[i] = max(candies[i], candies[i+1] + 1);
    return accumulate(candies.begin(), candies.end(), 0);
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
// Test functions
// =====================================================================

void test_w1() {
    cout << "Testing W1: Assign Cookies..." << endl;
    check(ref_w1({1,2,3}, {1,1}) == 1, "basic");
    check(ref_w1({1,2}, {1,2,3}) == 2, "all");
    check(ref_w1({10,9}, {1,2}) == 0, "none");
    check(ref_w1({10,9,8,7}, {5,6,7,8}) == 2, "partial");
    check(ref_w1({}, {1,2}) == 0, "empty children");
    check(ref_w1({1,2}, {}) == 0, "empty cookies");
    check(ref_w1({1}, {1}) == 1, "single");
    check(ref_w1({1,2,3}, {3}) == 1, "one big cookie");
}

void test_w2() {
    cout << "Testing W2: Jump Game..." << endl;
    check(ref_w2({2,3,1,1,4}) == true, "reachable");
    check(ref_w2({3,2,1,0,4}) == false, "unreachable");
    check(ref_w2({0}) == true, "single");
    check(ref_w2({1,0}) == true, "two ok");
    check(ref_w2({0,1}) == false, "two fail");
    check(ref_w2({1,1,1,1}) == true, "all ones");
    check(ref_w2({5,0,0,0,0,0}) == true, "big jump");
    check(ref_w2({2,0,0}) == true, "zeros mid");
}

void test_w3() {
    cout << "Testing W3: Best Buy Sell Stock..." << endl;
    check(ref_w3({7,1,5,3,6,4}) == 5, "basic");
    check(ref_w3({7,6,4,3,1}) == 0, "decreasing");
    check(ref_w3({5}) == 0, "single");
    check(ref_w3({2,4}) == 2, "two profit");
    check(ref_w3({4,2}) == 0, "two no profit");
    check(ref_w3({3,3,3}) == 0, "same");
    check(ref_w3({1,2,3,4,5}) == 4, "increasing");
    check(ref_w3({10,1,10}) == 9, "valley");
}

void test_w4() {
    cout << "Testing W4: Lemonade Change..." << endl;
    check(ref_w4({5,5,5,10,20}) == true, "basic true");
    check(ref_w4({5,5,10,10,20}) == false, "basic false");
    check(ref_w4({5,5,5}) == true, "all fives");
    check(ref_w4({5}) == true, "single five");
    check(ref_w4({10}) == false, "ten no change");
    check(ref_w4({20}) == false, "twenty no change");
    check(ref_w4({5,5,10,5,5,20}) == true, "complex");
    check(ref_w4({5,5,5,20}) == true, "three fives twenty");
}

void test_p1() {
    cout << "Testing P1: Activity Selection..." << endl;
    check(ref_p1({{1,2},{3,4},{0,6},{5,7},{8,9},{5,9}}) == 4, "basic");
    check(ref_p1({{1,3},{2,5},{4,7},{6,8}}) == 2, "overlap");
    check(ref_p1({{1,2},{3,4},{5,6}}) == 3, "no overlap");
    check(ref_p1({{1,10},{2,10},{3,10}}) == 1, "all overlap");
    check(ref_p1({{0,5}}) == 1, "single");
    check(ref_p1({}) == 0, "empty");
    check(ref_p1({{0,1},{1,2},{2,3},{3,4}}) == 4, "touching");
}

void test_p2() {
    cout << "Testing P2: Fractional Knapsack..." << endl;
    check(abs(ref_p2(50, {{10,60},{20,100},{30,120}}) - 240.0) < 1e-6, "basic");
    check(abs(ref_p2(30, {{10,60},{20,100}}) - 160.0) < 1e-6, "exact");
    check(abs(ref_p2(15, {{10,60},{20,100}}) - 85.0) < 1e-6, "partial");
    check(abs(ref_p2(0, {{10,60}}) - 0.0) < 1e-6, "zero cap");
    check(abs(ref_p2(100, {{10,50}}) - 50.0) < 1e-6, "excess cap");
    check(abs(ref_p2(5, {{10,50}}) - 25.0) < 1e-6, "half item");
    check(abs(ref_p2(10, {}) - 0.0) < 1e-6, "empty");
}

void test_p3() {
    cout << "Testing P3: Merge Intervals..." << endl;
    check(ref_p3({{1,3},{2,6},{8,10},{15,18}}) == vector<vector<int>>{{1,6},{8,10},{15,18}}, "basic");
    check(ref_p3({{1,4},{4,5}}) == vector<vector<int>>{{1,5}}, "touching");
    check(ref_p3({{1,4},{2,3}}) == vector<vector<int>>{{1,4}}, "contained");
    check(ref_p3({{1,2},{5,6},{9,10}}) == vector<vector<int>>{{1,2},{5,6},{9,10}}, "no overlap");
    check(ref_p3({{1,5},{1,5},{1,5}}) == vector<vector<int>>{{1,5}}, "all same");
    check(ref_p3({{1,10}}) == vector<vector<int>>{{1,10}}, "single");
    check(ref_p3({{1,4},{0,4}}) == vector<vector<int>>{{0,4}}, "unsorted");
    check(ref_p3({}) == vector<vector<int>>{}, "empty");
}

void test_p4() {
    cout << "Testing P4: Non-overlapping Intervals..." << endl;
    check(ref_p4({{1,2},{2,3},{3,4},{1,3}}) == 1, "basic");
    check(ref_p4({{1,2},{1,2},{1,2}}) == 2, "all same");
    check(ref_p4({{1,2},{2,3}}) == 0, "no overlap");
    check(ref_p4({{1,5},{2,6},{3,7}}) == 2, "all overlap");
    check(ref_p4({{1,2}}) == 0, "single");
    check(ref_p4({{1,100},{2,3},{4,5},{6,7}}) == 1, "nested");
    check(ref_p4({}) == 0, "empty");
}

void test_p5() {
    cout << "Testing P5: Jump Game II..." << endl;
    check(ref_p5({2,3,1,1,4}) == 2, "basic");
    check(ref_p5({2,3,0,1,4}) == 2, "zeros");
    check(ref_p5({1}) == 0, "single");
    check(ref_p5({1,1}) == 1, "two");
    check(ref_p5({10,0,0,0,0}) == 1, "big jump");
    check(ref_p5({1,1,1,1,1}) == 4, "all ones");
    check(ref_p5({4,3,2,1,0}) == 1, "decreasing");
}

void test_c1() {
    cout << "Testing C1: Job Sequencing..." << endl;
    check(ref_c1({{1,4,20},{2,1,10},{3,1,40},{4,1,30}}) == make_pair(2,60), "basic");
    check(ref_c1({{1,2,100},{2,1,19},{3,2,27},{4,1,25},{5,1,15}}) == make_pair(2,127), "five");
    check(ref_c1({{1,1,10},{2,1,20},{3,1,30}}) == make_pair(1,30), "same deadline");
    check(ref_c1({{1,1,10},{2,2,20},{3,3,30}}) == make_pair(3,60), "all fit");
    check(ref_c1({{1,1,50}}) == make_pair(1,50), "single");
    check(ref_c1({}) == make_pair(0,0), "empty");
}

void test_c2() {
    cout << "Testing C2: Gas Station..." << endl;
    check(ref_c2({1,2,3,4,5}, {3,4,5,1,2}) == 3, "basic");
    check(ref_c2({2,3,4}, {3,4,3}) == -1, "impossible");
    check(ref_c2({5,1,2,3,4}, {4,4,1,5,1}) == 4, "start last");
    check(ref_c2({5}, {4}) == 0, "single ok");
    check(ref_c2({3}, {5}) == -1, "single fail");
    check(ref_c2({3,1,1}, {1,2,2}) == 0, "start zero");
    check(ref_c2({3,3,3}, {3,3,3}) == 0, "equal");
}

void test_c3() {
    cout << "Testing C3: Min Platforms..." << endl;
    check(ref_c3({900,940,950,1100,1500,1800}, {910,1200,1120,1130,1900,2000}) == 3, "basic");
    check(ref_c3({900,1100,1235}, {1000,1200,1240}) == 1, "no overlap");
    check(ref_c3({100,100,100}, {200,200,200}) == 3, "all overlap");
    check(ref_c3({900}, {1000}) == 1, "single");
    check(ref_c3({900,940}, {1000,950}) == 2, "two overlap");
    check(ref_c3({100,200,300}, {150,250,350}) == 1, "sequential");
    check(ref_c3({}, {}) == 0, "empty");
}

void test_c4() {
    cout << "Testing C4: Candy..." << endl;
    check(ref_c4({1,0,2}) == 5, "basic");
    check(ref_c4({1,2,2}) == 4, "equal neighbor");
    check(ref_c4({3,2,1}) == 6, "decreasing");
    check(ref_c4({1,2,3}) == 6, "increasing");
    check(ref_c4({5}) == 1, "single");
    check(ref_c4({1,1}) == 2, "two same");
    check(ref_c4({1,3,2,2,1}) == 7, "valley");
    check(ref_c4({5,5,5,5}) == 4, "all same");
}

// =====================================================================
// Main
// =====================================================================

int main() {
    cout << "Chapter 18: Greedy Algorithms — The Smart Shortcut" << endl;
    cout << "===================================================" << endl << endl;

    test_w1(); test_w2(); test_w3(); test_w4();
    test_p1(); test_p2(); test_p3(); test_p4(); test_p5();
    test_c1(); test_c2(); test_c3(); test_c4();

    cout << endl;
    if (tests_passed == tests_total) {
        cout << "All " << tests_total << " tests passed!" << endl;
    } else {
        cout << tests_passed << " / " << tests_total << " tests passed." << endl;
    }
    return (tests_passed == tests_total) ? 0 : 1;
}
