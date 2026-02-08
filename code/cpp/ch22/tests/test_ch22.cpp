/*
 * Tests for Chapter 22: Stacks & Queues — Order Matters
 * Build: g++ -std=c++17 -o /tmp/test_ch22 code/cpp/ch22/tests/test_ch22.cpp && /tmp/test_ch22
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <deque>
#include <iostream>
#include <list>
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

static int passed = 0;
static int failed_count = 0;

void check(bool cond, const string& msg) {
    if (cond) { passed++; }
    else { failed_count++; cout << "FAIL: " << msg << endl; }
}

// =====================================================================
// Reference solutions
// =====================================================================

// W1: Valid Parentheses
bool ref_valid_parens(string s) {
    stack<char> stk;
    for (char ch : s) {
        if (ch == '(' || ch == '[' || ch == '{') { stk.push(ch); }
        else {
            if (stk.empty()) return false;
            char top = stk.top(); stk.pop();
            if ((ch == ')' && top != '(') || (ch == ']' && top != '[') || (ch == '}' && top != '{')) return false;
        }
    }
    return stk.empty();
}

// W2: Implement Stack
vector<int> ref_stack(vector<pair<string,int>> ops) {
    vector<int> data, results;
    for (auto& [op, val] : ops) {
        if (op == "push") data.push_back(val);
        else if (op == "pop") { results.push_back(data.empty() ? -1 : data.back()); if (!data.empty()) data.pop_back(); }
        else if (op == "top") results.push_back(data.empty() ? -1 : data.back());
        else if (op == "is_empty") results.push_back(data.empty() ? 1 : 0);
    }
    return results;
}

// W3: Implement Queue
vector<int> ref_queue(vector<pair<string,int>> ops) {
    deque<int> q;
    vector<int> results;
    for (auto& [op, val] : ops) {
        if (op == "enqueue") q.push_back(val);
        else if (op == "dequeue") { results.push_back(q.empty() ? -1 : q.front()); if (!q.empty()) q.pop_front(); }
        else if (op == "front") results.push_back(q.empty() ? -1 : q.front());
        else if (op == "is_empty") results.push_back(q.empty() ? 1 : 0);
    }
    return results;
}

// W4: Next Greater Element
vector<int> ref_next_greater(vector<int> arr) {
    int n = arr.size();
    vector<int> result(n, -1);
    stack<int> stk;
    for (int i = n - 1; i >= 0; i--) {
        while (!stk.empty() && arr[stk.top()] <= arr[i]) stk.pop();
        if (!stk.empty()) result[i] = arr[stk.top()];
        stk.push(i);
    }
    return result;
}

// W5: Min Stack
vector<int> ref_min_stack(vector<pair<string,int>> ops) {
    stack<int> stk, minStk;
    vector<int> results;
    for (auto& [op, val] : ops) {
        if (op == "push") {
            stk.push(val);
            minStk.push(minStk.empty() || val <= minStk.top() ? val : minStk.top());
        } else if (op == "pop") { stk.pop(); minStk.pop(); }
        else if (op == "top") results.push_back(stk.top());
        else if (op == "getMin") results.push_back(minStk.top());
    }
    return results;
}

// P1: Daily Temperatures
vector<int> ref_daily_temps(vector<int> temps) {
    int n = temps.size();
    vector<int> result(n, 0);
    stack<int> stk;
    for (int i = 0; i < n; i++) {
        while (!stk.empty() && temps[stk.top()] < temps[i]) {
            int j = stk.top(); stk.pop(); result[j] = i - j;
        }
        stk.push(i);
    }
    return result;
}

// P2: Evaluate RPN
int ref_eval_rpn(vector<string> tokens) {
    stack<int> stk;
    for (const string& t : tokens) {
        if (t == "+" || t == "-" || t == "*" || t == "/") {
            int b = stk.top(); stk.pop(); int a = stk.top(); stk.pop();
            if (t == "+") stk.push(a + b);
            else if (t == "-") stk.push(a - b);
            else if (t == "*") stk.push(a * b);
            else stk.push(a / b);
        } else stk.push(stoi(t));
    }
    return stk.top();
}

// P3: Sliding Window Maximum
vector<int> ref_sliding_window_max(vector<int> nums, int k) {
    deque<int> dq;
    vector<int> result;
    for (int i = 0; i < (int)nums.size(); i++) {
        while (!dq.empty() && dq.front() < i - k + 1) dq.pop_front();
        while (!dq.empty() && nums[dq.back()] <= nums[i]) dq.pop_back();
        dq.push_back(i);
        if (i >= k - 1) result.push_back(nums[dq.front()]);
    }
    return result;
}

// P4: Queue Using Two Stacks
vector<int> ref_queue_using_stacks(vector<pair<string,int>> ops) {
    stack<int> in, out;
    vector<int> results;
    auto transfer = [&]() { while (!in.empty()) { out.push(in.top()); in.pop(); } };
    for (auto& [op, val] : ops) {
        if (op == "enqueue") in.push(val);
        else if (op == "dequeue") { if (out.empty()) transfer(); results.push_back(out.top()); out.pop(); }
        else if (op == "peek") { if (out.empty()) transfer(); results.push_back(out.top()); }
        else if (op == "empty") results.push_back(in.empty() && out.empty() ? 1 : 0);
    }
    return results;
}

// P5: Remove Adjacent Duplicates
string ref_remove_adj_dups(string s) {
    string stk;
    for (char ch : s) {
        if (!stk.empty() && stk.back() == ch) stk.pop_back();
        else stk.push_back(ch);
    }
    return stk;
}

// C1: Largest Rectangle
int ref_largest_rectangle(vector<int> heights) {
    stack<int> stk;
    int maxArea = 0, n = heights.size();
    for (int i = 0; i <= n; i++) {
        int curr = (i == n) ? 0 : heights[i];
        while (!stk.empty() && heights[stk.top()] > curr) {
            int h = heights[stk.top()]; stk.pop();
            int w = stk.empty() ? i : i - stk.top() - 1;
            maxArea = max(maxArea, h * w);
        }
        stk.push(i);
    }
    return maxArea;
}

// C2: Trapping Rain Water
int ref_trapping_rain(vector<int> height) {
    int n = height.size();
    if (n < 3) return 0;
    int left = 0, right = n - 1, leftMax = height[0], rightMax = height[n-1], water = 0;
    while (left < right) {
        if (leftMax <= rightMax) { left++; leftMax = max(leftMax, height[left]); water += leftMax - height[left]; }
        else { right--; rightMax = max(rightMax, height[right]); water += rightMax - height[right]; }
    }
    return water;
}

// C3: Online Stock Span
vector<int> ref_stock_span(vector<int> prices) {
    stack<pair<int,int>> stk;
    vector<int> result;
    for (int price : prices) {
        int span = 1;
        while (!stk.empty() && stk.top().first <= price) { span += stk.top().second; stk.pop(); }
        stk.push({price, span});
        result.push_back(span);
    }
    return result;
}

// C4: LRU Cache
vector<int> ref_lru_cache(int capacity, vector<vector<string>> ops) {
    list<pair<int,int>> items;
    unordered_map<int, list<pair<int,int>>::iterator> cache;
    vector<int> results;
    for (auto& op : ops) {
        if (op[0] == "get") {
            int key = stoi(op[1]);
            auto it = cache.find(key);
            if (it == cache.end()) { results.push_back(-1); }
            else { items.splice(items.begin(), items, it->second); results.push_back(it->second->second); }
        } else if (op[0] == "put") {
            int key = stoi(op[1]), value = stoi(op[2]);
            auto it = cache.find(key);
            if (it != cache.end()) { it->second->second = value; items.splice(items.begin(), items, it->second); }
            else {
                if ((int)cache.size() >= capacity) { cache.erase(items.back().first); items.pop_back(); }
                items.push_front({key, value}); cache[key] = items.begin();
            }
        }
    }
    return results;
}

// =====================================================================
// Tests
// =====================================================================

void testW1() {
    check(ref_valid_parens("()") == true, "W1: ()");
    check(ref_valid_parens("()[]{}") == true, "W1: ()[]{}");
    check(ref_valid_parens("{[]}") == true, "W1: {[]}");
    check(ref_valid_parens("([)]") == false, "W1: ([)]");
    check(ref_valid_parens("(((") == false, "W1: (((");
    check(ref_valid_parens("") == true, "W1: empty");
    check(ref_valid_parens(")") == false, "W1: )");
    check(ref_valid_parens("({[(){}]})") == true, "W1: complex");
}

void testW2() {
    check(ref_stack({{"push",1},{"push",2},{"top",0},{"pop",0},{"is_empty",0}}) == vector<int>{2,2,0}, "W2: basic");
    check(ref_stack({{"pop",0},{"top",0},{"is_empty",0}}) == vector<int>{-1,-1,1}, "W2: empty ops");
    check(ref_stack({{"push",10},{"push",20},{"push",30},{"pop",0},{"pop",0},{"pop",0},{"is_empty",0}})
          == vector<int>{30,20,10,1}, "W2: push-pop all");
}

void testW3() {
    check(ref_queue({{"enqueue",1},{"enqueue",2},{"front",0},{"dequeue",0},{"is_empty",0}})
          == vector<int>{1,1,0}, "W3: basic");
    check(ref_queue({{"dequeue",0},{"front",0},{"is_empty",0}}) == vector<int>{-1,-1,1}, "W3: empty ops");
    check(ref_queue({{"enqueue",10},{"enqueue",20},{"enqueue",30},{"dequeue",0},{"dequeue",0},{"dequeue",0},{"is_empty",0}})
          == vector<int>{10,20,30,1}, "W3: FIFO");
}

void testW4() {
    check(ref_next_greater({4,5,2,10,8}) == vector<int>{5,10,10,-1,-1}, "W4: basic");
    check(ref_next_greater({3,2,1}) == vector<int>{-1,-1,-1}, "W4: decreasing");
    check(ref_next_greater({1,2,3}) == vector<int>{2,3,-1}, "W4: increasing");
    check(ref_next_greater({5}) == vector<int>{-1}, "W4: single");
    check(ref_next_greater({2,1,2,4,3}) == vector<int>{4,2,4,-1,-1}, "W4: duplicates");
}

void testW5() {
    check(ref_min_stack({{"push",-2},{"push",0},{"push",-3},{"getMin",0},{"pop",0},{"top",0},{"getMin",0}})
          == vector<int>{-3,0,-2}, "W5: basic");
    check(ref_min_stack({{"push",5},{"top",0},{"getMin",0}}) == vector<int>{5,5}, "W5: single");
    check(ref_min_stack({{"push",3},{"push",2},{"push",1},{"getMin",0},{"pop",0},{"getMin",0},{"pop",0},{"getMin",0}})
          == vector<int>{1,2,3}, "W5: decreasing");
}

void testP1() {
    check(ref_daily_temps({73,74,75,71,69,72,76,73}) == vector<int>{1,1,4,2,1,1,0,0}, "P1: basic");
    check(ref_daily_temps({30,40,50,60}) == vector<int>{1,1,1,0}, "P1: increasing");
    check(ref_daily_temps({30,30,30}) == vector<int>{0,0,0}, "P1: all same");
    check(ref_daily_temps({90,80,70,60}) == vector<int>{0,0,0,0}, "P1: decreasing");
    check(ref_daily_temps({50}) == vector<int>{0}, "P1: single");
}

void testP2() {
    check(ref_eval_rpn({"2","1","+","3","*"}) == 9, "P2: (2+1)*3");
    check(ref_eval_rpn({"4","13","5","/","+"}) == 6, "P2: 4+(13/5)");
    check(ref_eval_rpn({"42"}) == 42, "P2: single");
    check(ref_eval_rpn({"5","3","-"}) == 2, "P2: subtraction");
    check(ref_eval_rpn({"3","5","-"}) == -2, "P2: negative result");
}

void testP3() {
    check(ref_sliding_window_max({1,3,-1,-3,5,3,6,7}, 3) == vector<int>{3,3,5,5,6,7}, "P3: basic");
    check(ref_sliding_window_max({1}, 1) == vector<int>{1}, "P3: single");
    check(ref_sliding_window_max({1,3,2}, 3) == vector<int>{3}, "P3: k=n");
    check(ref_sliding_window_max({5,5,5,5}, 2) == vector<int>{5,5,5}, "P3: all same");
    check(ref_sliding_window_max({9,7,5,3,1}, 3) == vector<int>{9,7,5}, "P3: decreasing");
}

void testP4() {
    check(ref_queue_using_stacks({{"enqueue",1},{"enqueue",2},{"peek",0},{"dequeue",0},{"empty",0}})
          == vector<int>{1,1,0}, "P4: basic");
    check(ref_queue_using_stacks({{"enqueue",10},{"enqueue",20},{"enqueue",30},{"dequeue",0},{"dequeue",0},{"dequeue",0}})
          == vector<int>{10,20,30}, "P4: FIFO");
    check(ref_queue_using_stacks({{"empty",0},{"enqueue",1},{"empty",0},{"dequeue",0},{"empty",0}})
          == vector<int>{1,0,1,1}, "P4: empty checks");
}

void testP5() {
    check(ref_remove_adj_dups("abbaca") == "ca", "P5: abbaca");
    check(ref_remove_adj_dups("azxxzy") == "ay", "P5: azxxzy");
    check(ref_remove_adj_dups("abc") == "abc", "P5: abc");
    check(ref_remove_adj_dups("aabbcc") == "", "P5: aabbcc");
    check(ref_remove_adj_dups("a") == "a", "P5: single");
    check(ref_remove_adj_dups("abba") == "", "P5: abba");
}

void testC1() {
    check(ref_largest_rectangle({2,1,5,6,2,3}) == 10, "C1: basic");
    check(ref_largest_rectangle({2,4}) == 4, "C1: two bars");
    check(ref_largest_rectangle({5}) == 5, "C1: single");
    check(ref_largest_rectangle({1,2,3,4,5}) == 9, "C1: increasing");
    check(ref_largest_rectangle({5,4,3,2,1}) == 9, "C1: decreasing");
    check(ref_largest_rectangle({3,3,3,3}) == 12, "C1: all same");
    check(ref_largest_rectangle({6,2,5,4,5,1,6}) == 12, "C1: valley");
}

void testC2() {
    check(ref_trapping_rain({0,1,0,2,1,0,1,3,2,1,2,1}) == 6, "C2: basic");
    check(ref_trapping_rain({4,2,0,3,2,5}) == 9, "C2: v-shape");
    check(ref_trapping_rain({1,2,3}) == 0, "C2: increasing");
    check(ref_trapping_rain({3,2,1}) == 0, "C2: decreasing");
    check(ref_trapping_rain({}) == 0, "C2: empty");
    check(ref_trapping_rain({3,0,3}) == 3, "C2: simple pool");
}

void testC3() {
    check(ref_stock_span({100,80,60,70,60,75,85}) == vector<int>{1,1,1,2,1,4,6}, "C3: basic");
    check(ref_stock_span({1,2,3,4,5}) == vector<int>{1,2,3,4,5}, "C3: increasing");
    check(ref_stock_span({5,4,3,2,1}) == vector<int>{1,1,1,1,1}, "C3: decreasing");
    check(ref_stock_span({5,5,5,5}) == vector<int>{1,2,3,4}, "C3: all same");
    check(ref_stock_span({10}) == vector<int>{1}, "C3: single");
}

void testC4() {
    check(ref_lru_cache(2, {{"put","1","1"},{"put","2","2"},{"get","1"},
        {"put","3","3"},{"get","2"},{"put","4","4"},{"get","1"},{"get","3"},{"get","4"}})
        == vector<int>{1,-1,-1,3,4}, "C4: basic");
    check(ref_lru_cache(2, {{"put","1","1"},{"put","1","10"},{"get","1"}})
        == vector<int>{10}, "C4: update");
    check(ref_lru_cache(1, {{"get","1"}}) == vector<int>{-1}, "C4: get missing");
    check(ref_lru_cache(2, {{"put","1","1"},{"put","2","2"},{"put","3","3"},
        {"get","1"},{"get","2"},{"get","3"}})
        == vector<int>{-1,2,3}, "C4: eviction");
    check(ref_lru_cache(1, {{"put","1","10"},{"get","1"},{"put","2","20"},{"get","1"},{"get","2"}})
        == vector<int>{10,-1,20}, "C4: cap=1");
}

int main() {
    cout << "Chapter 22: Stacks & Queues — Order Matters" << endl;
    cout << "=============================================" << endl << endl;

    testW1(); testW2(); testW3(); testW4(); testW5();
    testP1(); testP2(); testP3(); testP4(); testP5();
    testC1(); testC2(); testC3(); testC4();

    cout << endl;
    if (failed_count == 0) {
        cout << "All " << passed << " tests passed!" << endl;
    } else {
        cout << passed << " passed, " << failed_count << " failed." << endl;
        return 1;
    }
    return 0;
}
