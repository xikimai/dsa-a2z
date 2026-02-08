/*
 * Example 01: Stack & Queue Basics — See LIFO and FIFO in Action
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * Demonstrates:
 *   - Stack (LIFO) using std::stack
 *   - Queue (FIFO) using std::queue
 *   - Balanced parentheses with a stack
 *
 * Build: g++ -std=c++17 -o /tmp/ex01_ch22 code/cpp/ch22/learn/example_01_stack_queue_basics.cpp && /tmp/ex01_ch22
 */

#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <vector>
using namespace std;

void stackDemo() {
    cout << "=== Stack (LIFO) Demo ===" << endl;
    stack<int> stk;
    stk.push(10); cout << "push(10)" << endl;
    stk.push(20); cout << "push(20)" << endl;
    stk.push(30); cout << "push(30)" << endl;
    cout << "top() -> " << stk.top() << endl;
    stk.pop();
    cout << "pop() -> top is now " << stk.top() << endl;
    cout << "size: " << stk.size() << ", empty: " << stk.empty() << endl;
    cout << endl;
}

void queueDemo() {
    cout << "=== Queue (FIFO) Demo ===" << endl;
    queue<string> q;
    q.push("Alice");   cout << "enqueue Alice" << endl;
    q.push("Bob");     cout << "enqueue Bob" << endl;
    q.push("Charlie"); cout << "enqueue Charlie" << endl;
    cout << "front() -> " << q.front() << endl;
    q.pop();
    cout << "dequeue -> front is now " << q.front() << endl;
    cout << "size: " << q.size() << endl;
    cout << endl;
}

bool isValid(const string& s) {
    stack<char> stk;
    for (char ch : s) {
        if (ch == '(' || ch == '[' || ch == '{') {
            stk.push(ch);
        } else {
            if (stk.empty()) return false;
            char top = stk.top(); stk.pop();
            if ((ch == ')' && top != '(') ||
                (ch == ']' && top != '[') ||
                (ch == '}' && top != '{')) return false;
        }
    }
    return stk.empty();
}

void balancedParens() {
    cout << "=== Balanced Parentheses ===" << endl;
    vector<string> tests = {"({[]})", "([)]", "((()))", "(((", ""};
    for (const string& s : tests) {
        cout << "  \"" << s << "\" -> " << (isValid(s) ? "VALID" : "INVALID") << endl;
    }
}

int main() {
    stackDemo();
    queueDemo();
    balancedParens();
    return 0;
}
