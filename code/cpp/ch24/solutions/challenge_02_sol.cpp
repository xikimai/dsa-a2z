/*
 * Solution for Challenge 2: Maximal Rectangle
 * Chapter 24: Dynamic Programming II — Grids and Paths
 */

#include <algorithm>
#include <climits>
#include <stack>
#include <vector>
using namespace std;

int largestRect(vector<int>& heights) {
    stack<int> st;
    int maxArea = 0, n = heights.size();
    for (int i = 0; i <= n; i++) {
        int h = i < n ? heights[i] : 0;
        while (!st.empty() && heights[st.top()] > h) {
            int height = heights[st.top()]; st.pop();
            int width = st.empty() ? i : i - st.top() - 1;
            maxArea = max(maxArea, height * width);
        }
        st.push(i);
    }
    return maxArea;
}

int solve(vector<vector<int>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) return 0;
    int m = matrix.size(), n = matrix[0].size();
    vector<int> heights(n, 0);
    int maxArea = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++)
            heights[j] = matrix[i][j] == 1 ? heights[j] + 1 : 0;
        maxArea = max(maxArea, largestRect(heights));
    }
    return maxArea;
}

int main() { return 0; }
