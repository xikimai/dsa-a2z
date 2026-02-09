/*
 * Solution for Challenge 2: Maximum Rectangle in Histogram
 * Chapter 34: Computational Geometry & Sweep Line
 */
#include <algorithm>
#include <stack>
#include <vector>
using namespace std;

int solve(vector<int>& heights) {
    stack<int> st;
    int maxArea = 0, n = heights.size();
    for (int i = 0; i <= n; i++) {
        int h = (i < n) ? heights[i] : 0;
        while (!st.empty() && heights[st.top()] > h) {
            int height = heights[st.top()]; st.pop();
            int width = st.empty() ? i : i - st.top() - 1;
            maxArea = max(maxArea, height * width);
        }
        st.push(i);
    }
    return maxArea;
}

int main() { return 0; }
