/*
 * Tests for Chapter 14: Prefix Sums — The Running Total Trick
 * Build: g++ -std=c++17 -o /tmp/test_ch14 code/cpp/ch14/tests/test_ch14.cpp && /tmp/test_ch14
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

// W1: Build Prefix Sum
vector<long long> ref_w1(vector<int> arr) {
    int n = arr.size();
    vector<long long> p(n + 1, 0);
    for (int i = 1; i <= n; i++) p[i] = p[i-1] + arr[i-1];
    return p;
}

// W2: Range Sum Query
vector<long long> ref_w2(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size();
    vector<long long> p(n + 1, 0);
    for (int i = 0; i < n; i++) p[i+1] = p[i] + arr[i];
    vector<long long> r;
    for (auto& q : queries) r.push_back(p[q[1]+1] - p[q[0]]);
    return r;
}

// W3: Running Sum
vector<long long> ref_w3(vector<int> arr) {
    if (arr.empty()) return {};
    vector<long long> r(arr.size());
    r[0] = arr[0];
    for (int i = 1; i < (int)arr.size(); i++) r[i] = r[i-1] + arr[i];
    return r;
}

// W4: Is Prefix
bool ref_w4(vector<int> a1, vector<int> a2) {
    if (a1.size() > a2.size()) return false;
    for (int i = 0; i < (int)a1.size(); i++) if (a1[i] != a2[i]) return false;
    return true;
}

// P1: Equilibrium Index
int ref_p1(vector<int> arr) {
    int n = arr.size();
    vector<long long> p(n + 1, 0);
    for (int i = 0; i < n; i++) p[i+1] = p[i] + arr[i];
    for (int i = 0; i < n; i++) if (p[i] == p[n] - p[i+1]) return i;
    return -1;
}

// P2: Subarray Sum K
int ref_p2(vector<int> arr, int k) {
    unordered_map<long long, int> m; m[0] = 1;
    long long s = 0; int c = 0;
    for (int x : arr) { s += x; if (m.count(s-k)) c += m[s-k]; m[s]++; }
    return c;
}

// P3: Product Except Self
vector<long long> ref_p3(vector<int> arr) {
    int n = arr.size();
    vector<long long> r(n, 1);
    long long left = 1;
    for (int i = 0; i < n; i++) { r[i] = left; left *= arr[i]; }
    long long right = 1;
    for (int i = n-1; i >= 0; i--) { r[i] *= right; right *= arr[i]; }
    return r;
}

// P4: Range Update
vector<long long> ref_p4(int n, vector<vector<int>> updates) {
    vector<long long> d(n + 1, 0);
    for (auto& u : updates) { d[u[0]] += u[2]; if (u[1]+1 <= n) d[u[1]+1] -= u[2]; }
    vector<long long> r(n); long long run = 0;
    for (int i = 0; i < n; i++) { run += d[i]; r[i] = run; }
    return r;
}

// P5: Kadane's
long long ref_p5(vector<int> arr) {
    if (arr.empty()) return 0;
    long long cur = arr[0], mx = arr[0];
    for (int i = 1; i < (int)arr.size(); i++) { cur = max(cur + arr[i], (long long)arr[i]); mx = max(mx, cur); }
    return mx;
}

// C1: 2D Prefix Sum
vector<long long> ref_c1(vector<vector<int>> matrix, vector<vector<int>> queries) {
    int rows = matrix.size(), cols = matrix[0].size();
    vector<vector<long long>> p(rows+1, vector<long long>(cols+1, 0));
    for (int i = 1; i <= rows; i++)
        for (int j = 1; j <= cols; j++)
            p[i][j] = p[i-1][j] + p[i][j-1] - p[i-1][j-1] + matrix[i-1][j-1];
    vector<long long> r;
    for (auto& q : queries) r.push_back(p[q[2]+1][q[3]+1] - p[q[0]][q[3]+1] - p[q[2]+1][q[1]] + p[q[0]][q[1]]);
    return r;
}

// C2: Three Ways
long long ref_c2_brute(vector<int> arr) {
    if (arr.empty()) return 0;
    long long mx = arr[0]; int n = arr.size();
    for (int l = 0; l < n; l++) for (int r = l; r < n; r++) {
        long long t = 0; for (int k = l; k <= r; k++) t += arr[k]; mx = max(mx, t);
    }
    return mx;
}
long long ref_c2_prefix(vector<int> arr) {
    if (arr.empty()) return 0;
    int n = arr.size(); vector<long long> p(n+1, 0);
    for (int i = 0; i < n; i++) p[i+1] = p[i] + arr[i];
    long long mx = arr[0];
    for (int l = 0; l < n; l++) for (int r = l; r < n; r++) mx = max(mx, p[r+1]-p[l]);
    return mx;
}
long long ref_c2_kadane(vector<int> arr) { return ref_p5(arr); }

// C3: Divisible by K
int ref_c3(vector<int> arr, int k) {
    unordered_map<int, int> m; m[0] = 1;
    long long s = 0; int c = 0;
    for (int x : arr) { s += x; int rem = ((s%k)+k)%k; if (m.count(rem)) c += m[rem]; m[rem]++; }
    return c;
}

// C4: Min Ops Make Equal
long long ref_c4(vector<int> arr) {
    sort(arr.begin(), arr.end()); int n = arr.size();
    if (n <= 1) return 0;
    vector<long long> p(n+1, 0);
    for (int i = 0; i < n; i++) p[i+1] = p[i] + arr[i];
    long long mn = LLONG_MAX;
    for (int i = 0; i < n; i++) {
        long long lc = (long long)i * arr[i] - p[i];
        long long rc = (p[n] - p[i+1]) - (long long)(n-i-1) * arr[i];
        mn = min(mn, lc + rc);
    }
    return mn;
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
    cout << "Testing W1: Build Prefix Sum..." << endl;
    check(ref_w1({3,1,4,1,5}) == vector<long long>{0,3,4,8,9,14}, "basic");
    check(ref_w1({5}) == vector<long long>{0,5}, "single");
    check(ref_w1({}) == vector<long long>{0}, "empty");
    check(ref_w1({-1,-2,-3}) == vector<long long>{0,-1,-3,-6}, "negatives");
    check(ref_w1({1,-1,2,-2,3}) == vector<long long>{0,1,0,2,0,3}, "mixed");
    check(ref_w1({0,0,0}) == vector<long long>{0,0,0,0}, "zeros");
}

void test_w2() {
    cout << "Testing W2: Range Sum Query..." << endl;
    check(ref_w2({3,1,4,1,5,9}, {{0,5},{2,4},{3,3}}) == vector<long long>{23,10,1}, "basic");
    check(ref_w2({10,20,30}, {{0,0},{1,1},{2,2}}) == vector<long long>{10,20,30}, "singles");
    check(ref_w2({1,2,3,4,5}, {{0,4}}) == vector<long long>{15}, "full");
    check(ref_w2({1,2,3,4}, {{0,1},{2,3}}) == vector<long long>{3,7}, "adjacent");
    check(ref_w2({1000000000,1000000000,1000000000}, {{0,2}}) == vector<long long>{3000000000LL}, "large");
    check(ref_w2({-5,3,-2,7,-1}, {{0,4},{1,3}}) == vector<long long>{2,8}, "negatives");
}

void test_w3() {
    cout << "Testing W3: Running Sum..." << endl;
    check(ref_w3({1,2,3,4}) == vector<long long>{1,3,6,10}, "basic");
    check(ref_w3({5}) == vector<long long>{5}, "single");
    check(ref_w3({}) == vector<long long>{}, "empty");
    check(ref_w3({-1,-2,-3}) == vector<long long>{-1,-3,-6}, "negatives");
    check(ref_w3({3,-1,2,-4,5}) == vector<long long>{3,2,4,0,5}, "mixed");
    check(ref_w3({0,0,0}) == vector<long long>{0,0,0}, "zeros");
}

void test_w4() {
    cout << "Testing W4: Is Prefix..." << endl;
    check(ref_w4({1,2,3}, {1,2,3,4,5}) == true, "is prefix");
    check(ref_w4({1,2,4}, {1,2,3,4,5}) == false, "not prefix");
    check(ref_w4({}, {1,2,3}) == true, "empty prefix");
    check(ref_w4({1,2,3}, {1,2,3}) == true, "equal");
    check(ref_w4({1,2,3,4}, {1,2,3}) == false, "longer");
    check(ref_w4({}, {}) == true, "both empty");
    check(ref_w4({7}, {7,8,9}) == true, "single match");
    check(ref_w4({7}, {8,9}) == false, "single no match");
}

void test_p1() {
    cout << "Testing P1: Equilibrium Index..." << endl;
    check(ref_p1({-7,1,5,2,-4,3,0}) == 3, "basic");
    check(ref_p1({1,2,3}) == -1, "no equilibrium");
    check(ref_p1({0,1,-1}) == 0, "at start");
    check(ref_p1({1,-1,0}) == 2, "at end");
    check(ref_p1({42}) == 0, "single");
    check(ref_p1({1,1}) == -1, "two elements");
    check(ref_p1({1,3,5,2,2}) == 2, "another");
}

void test_p2() {
    cout << "Testing P2: Subarray Sum K..." << endl;
    check(ref_p2({1,1,1}, 2) == 2, "basic");
    check(ref_p2({1,2,3}, 3) == 2, "two ways");
    check(ref_p2({1}, 0) == 0, "no match");
    check(ref_p2({1,-1,0}, 0) == 3, "zeros");
    check(ref_p2({0,0,0}, 0) == 6, "all zeros");
    check(ref_p2({1}, 1) == 1, "single match");
    check(ref_p2({1,-2,3,-1}, -1) == 2, "negative k");
}

void test_p3() {
    cout << "Testing P3: Product Except Self..." << endl;
    check(ref_p3({1,2,3,4}) == vector<long long>{24,12,8,6}, "basic");
    check(ref_p3({-1,1,0,-3,3}) == vector<long long>{0,0,9,0,0}, "with zero");
    check(ref_p3({3,5}) == vector<long long>{5,3}, "two elements");
    check(ref_p3({-1,-2,-3}) == vector<long long>{6,3,2}, "negatives");
    check(ref_p3({1,1,1,1}) == vector<long long>{1,1,1,1}, "all ones");
    check(ref_p3({0,0,1}) == vector<long long>{0,0,0}, "two zeros");
}

void test_p4() {
    cout << "Testing P4: Range Update..." << endl;
    check(ref_p4(5, {{1,3,2},{2,4,3},{0,1,-1}}) == vector<long long>{-1,1,5,5,3}, "basic");
    check(ref_p4(4, {{0,3,5}}) == vector<long long>{5,5,5,5}, "full range");
    check(ref_p4(6, {{0,1,10},{4,5,20}}) == vector<long long>{10,10,0,0,20,20}, "non-overlapping");
    check(ref_p4(3, {{0,2,7}}) == vector<long long>{7,7,7}, "full");
    check(ref_p4(5, {{2,2,100}}) == vector<long long>{0,0,100,0,0}, "single element");
    check(ref_p4(4, {{0,3,10},{1,2,-5}}) == vector<long long>{10,5,5,10}, "negative");
}

void test_p5() {
    cout << "Testing P5: Kadane's..." << endl;
    check(ref_p5({-2,1,-3,4,-1,2,1,-5,4}) == 6, "basic");
    check(ref_p5({-5,-3,-1,-4}) == -1, "all negative");
    check(ref_p5({1}) == 1, "single");
    check(ref_p5({5,4,-1,7,8}) == 23, "all positive-ish");
    check(ref_p5({-7}) == -7, "single negative");
    check(ref_p5({2,-1,2,-1,2}) == 4, "alternating");
    check(ref_p5({10,-20,30}) == 30, "large dip");
}

void test_c1() {
    cout << "Testing C1: 2D Prefix Sum..." << endl;
    check(ref_c1({{1,2,3},{4,5,6},{7,8,9}}, {{0,0,2,2},{1,1,2,2},{0,0,0,0}})
        == vector<long long>{45,28,1}, "3x3");
    check(ref_c1({{5}}, {{0,0,0,0}}) == vector<long long>{5}, "single");
    check(ref_c1({{1,2,3,4}}, {{0,0,0,3},{0,1,0,2}}) == vector<long long>{10,5}, "single row");
    check(ref_c1({{1},{2},{3}}, {{0,0,2,0},{1,0,2,0}}) == vector<long long>{6,5}, "single col");
    check(ref_c1({{1,2},{3,4}}, {{0,0,1,1},{0,0,0,1},{1,0,1,1}})
        == vector<long long>{10,3,7}, "2x2");
    check(ref_c1({{-1,2},{3,-4}}, {{0,0,1,1}}) == vector<long long>{0}, "negatives");
}

void test_c2() {
    cout << "Testing C2: Three Ways..." << endl;
    vector<int> a1 = {-2,1,-3,4,-1,2,1,-5,4};
    check(ref_c2_brute(a1) == 6, "brute basic");
    check(ref_c2_prefix(a1) == 6, "prefix basic");
    check(ref_c2_kadane(a1) == 6, "kadane basic");
    vector<int> a2 = {-5,-3,-1,-4};
    check(ref_c2_brute(a2) == -1, "brute all neg");
    check(ref_c2_prefix(a2) == -1, "prefix all neg");
    check(ref_c2_kadane(a2) == -1, "kadane all neg");
    check(ref_c2_brute({7}) == 7, "brute single");
    check(ref_c2_prefix({7}) == 7, "prefix single");
    check(ref_c2_kadane({7}) == 7, "kadane single");
    check(ref_c2_brute({1,2,3}) == 6, "brute all pos");
    check(ref_c2_prefix({1,2,3}) == 6, "prefix all pos");
    check(ref_c2_kadane({1,2,3}) == 6, "kadane all pos");
    vector<int> a5 = {5,-9,6,-2,3};
    check(ref_c2_brute(a5) == 7, "brute mixed");
    check(ref_c2_prefix(a5) == 7, "prefix mixed");
    check(ref_c2_kadane(a5) == 7, "kadane mixed");
}

void test_c3() {
    cout << "Testing C3: Divisible by K..." << endl;
    check(ref_c3({4,5,0,-2,-3,1}, 5) == 7, "basic");
    check(ref_c3({5}, 9) == 0, "no match");
    check(ref_c3({5,10,15}, 5) == 6, "all divisible");
    check(ref_c3({-1,2,9}, 2) == 2, "negative");
    check(ref_c3({0}, 1) == 1, "single zero");
    check(ref_c3({1,2,3}, 1) == 6, "k=1");
}

void test_c4() {
    cout << "Testing C4: Min Ops Make Equal..." << endl;
    check(ref_c4({1,2,3}) == 2, "basic");
    check(ref_c4({5}) == 0, "single");
    check(ref_c4({3,3,3}) == 0, "equal");
    check(ref_c4({1,5}) == 4, "two elements");
    check(ref_c4({1,2,9,10}) == 16, "larger");
    check(ref_c4({-5,-3,-1}) == 4, "negatives");
    check(ref_c4({1,100}) == 99, "spread");
}

// =====================================================================
// Main
// =====================================================================

int main() {
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
