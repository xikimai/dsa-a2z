/*
 * Tests for Chapter 24: Dynamic Programming II — Grids and Paths
 * Build: g++ -std=c++17 -o /tmp/test_ch24 code/cpp/ch24/tests/test_ch24.cpp && /tmp/test_ch24
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <cstdio>
#include <functional>
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named with ref_ prefix)
// =====================================================================

// W1: Unique Paths
int ref_unique_paths(int m, int n) {
    vector<int> dp(n, 1);
    for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
            dp[j] += dp[j - 1];
    return dp[n - 1];
}

// W2: Unique Paths with Obstacles
int ref_unique_paths_obstacles(vector<vector<int>> grid) {
    int m = grid.size(), n = grid[0].size();
    if (grid[0][0] == 1) return 0;
    vector<int> dp(n, 0);
    dp[0] = 1;
    for (int j = 1; j < n; j++) dp[j] = grid[0][j] == 0 ? dp[j-1] : 0;
    for (int i = 1; i < m; i++) {
        dp[0] = grid[i][0] == 0 ? dp[0] : 0;
        for (int j = 1; j < n; j++)
            dp[j] = grid[i][j] == 1 ? 0 : dp[j] + dp[j-1];
    }
    return dp[n - 1];
}

// W3: Minimum Path Sum
int ref_min_path_sum(vector<vector<int>> grid) {
    int m = grid.size(), n = grid[0].size();
    vector<int> dp(n);
    dp[0] = grid[0][0];
    for (int j = 1; j < n; j++) dp[j] = dp[j-1] + grid[0][j];
    for (int i = 1; i < m; i++) {
        dp[0] += grid[i][0];
        for (int j = 1; j < n; j++)
            dp[j] = min(dp[j], dp[j-1]) + grid[i][j];
    }
    return dp[n - 1];
}

// W4: Triangle
int ref_triangle(vector<vector<int>> tri) {
    int n = tri.size();
    vector<int> dp = tri[n-1];
    for (int i = n-2; i >= 0; i--)
        for (int j = 0; j <= i; j++)
            dp[j] = tri[i][j] + min(dp[j], dp[j+1]);
    return dp[0];
}

// P1: Unique Paths III
int ref_unique_paths_iii(vector<vector<int>> grid) {
    int m = grid.size(), n = grid[0].size();
    int sr = 0, sc = 0, empty = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) { sr = i; sc = j; empty++; }
            else if (grid[i][j] == 0) empty++;
        }
    int result = 0;
    int dx[] = {0,0,1,-1}, dy[] = {1,-1,0,0};
    function<void(int,int,int)> dfs = [&](int r, int c, int rem) {
        if (grid[r][c] == 2) { if (rem == 0) result++; return; }
        int tmp = grid[r][c]; grid[r][c] = -2;
        for (int d = 0; d < 4; d++) {
            int nr = r+dx[d], nc = c+dy[d];
            if (nr>=0&&nr<m&&nc>=0&&nc<n&&grid[nr][nc]!=-1&&grid[nr][nc]!=-2)
                dfs(nr, nc, rem-1);
        }
        grid[r][c] = tmp;
    };
    dfs(sr, sc, empty);
    return result;
}

// P2: Min Falling Path
int ref_min_falling_path(vector<vector<int>> matrix) {
    int n = matrix.size();
    vector<int> dp = matrix[0];
    for (int i = 1; i < n; i++) {
        vector<int> nd(n);
        for (int j = 0; j < n; j++) {
            int best = dp[j];
            if (j > 0) best = min(best, dp[j-1]);
            if (j < n-1) best = min(best, dp[j+1]);
            nd[j] = matrix[i][j] + best;
        }
        dp = nd;
    }
    return *min_element(dp.begin(), dp.end());
}

// P3: Maximal Square
int ref_maximal_square(vector<vector<int>> matrix) {
    int m = matrix.size(), n = matrix[0].size();
    vector<int> dp(n, 0);
    int maxSide = 0, prevDiag = 0;
    for (int i = 0; i < m; i++) {
        prevDiag = 0;
        for (int j = 0; j < n; j++) {
            int temp = dp[j];
            if (matrix[i][j] == 1) {
                dp[j] = (i==0||j==0) ? 1 : min({dp[j],dp[j-1],prevDiag})+1;
                maxSide = max(maxSide, dp[j]);
            } else dp[j] = 0;
            prevDiag = temp;
        }
    }
    return maxSide * maxSide;
}

// P4: Cherry Pickup II
int ref_cherry_pickup_ii(vector<vector<int>> grid) {
    int m = grid.size(), n = grid[0].size();
    vector<vector<int>> dp(n, vector<int>(n, -1));
    for (int c1 = 0; c1 < n; c1++)
        for (int c2 = 0; c2 < n; c2++)
            dp[c1][c2] = grid[m-1][c1] + (c1!=c2 ? grid[m-1][c2] : 0);
    for (int i = m-2; i >= 0; i--) {
        vector<vector<int>> nd(n, vector<int>(n, -1));
        for (int c1 = 0; c1 < n; c1++)
            for (int c2 = 0; c2 < n; c2++) {
                int best = -1;
                for (int d1=-1; d1<=1; d1++)
                    for (int d2=-1; d2<=1; d2++) {
                        int nc1=c1+d1, nc2=c2+d2;
                        if (nc1>=0&&nc1<n&&nc2>=0&&nc2<n&&dp[nc1][nc2]!=-1)
                            best = max(best, dp[nc1][nc2]);
                    }
                if (best == -1) continue;
                nd[c1][c2] = grid[i][c1] + (c1!=c2 ? grid[i][c2] : 0) + best;
            }
        dp = nd;
    }
    return dp[0][n-1] != -1 ? dp[0][n-1] : 0;
}

// P5: Count Squares
int ref_count_squares(vector<vector<int>> matrix) {
    int m = matrix.size(), n = matrix[0].size();
    vector<int> dp(n, 0);
    int total = 0, prevDiag = 0;
    for (int i = 0; i < m; i++) {
        prevDiag = 0;
        for (int j = 0; j < n; j++) {
            int temp = dp[j];
            if (matrix[i][j] == 1) {
                dp[j] = (i==0||j==0) ? 1 : min({dp[j],dp[j-1],prevDiag})+1;
                total += dp[j];
            } else dp[j] = 0;
            prevDiag = temp;
        }
    }
    return total;
}

// C1: Dungeon
int ref_dungeon(vector<vector<int>> dungeon) {
    int m = dungeon.size(), n = dungeon[0].size();
    vector<int> dp(n+1, INT_MAX);
    dp[n-1] = 1;
    for (int i = m-1; i >= 0; i--) {
        vector<int> nd(n+1, INT_MAX);
        for (int j = n-1; j >= 0; j--) {
            int mn = min(dp[j], nd[j+1]);
            nd[j] = max(1, mn - dungeon[i][j]);
        }
        dp = nd;
    }
    return dp[0];
}

// C2: Maximal Rectangle
int ref_largest_rect(vector<int> heights) {
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

int ref_maximal_rectangle(vector<vector<int>> matrix) {
    if (matrix.empty() || matrix[0].empty()) return 0;
    int m = matrix.size(), n = matrix[0].size();
    vector<int> heights(n, 0);
    int maxArea = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++)
            heights[j] = matrix[i][j] == 1 ? heights[j]+1 : 0;
        maxArea = max(maxArea, ref_largest_rect(heights));
    }
    return maxArea;
}

// C3: Ninja Training
int ref_ninja_training(vector<vector<int>> points) {
    int prev[3] = {points[0][0], points[0][1], points[0][2]};
    for (int i = 1; i < (int)points.size(); i++) {
        int curr[3] = {0,0,0};
        for (int j = 0; j < 3; j++)
            for (int k = 0; k < 3; k++)
                if (k != j) curr[j] = max(curr[j], prev[k] + points[i][j]);
        prev[0]=curr[0]; prev[1]=curr[1]; prev[2]=curr[2];
    }
    return max({prev[0], prev[1], prev[2]});
}

// C4: Cherry Pickup I
int ref_cherry_pickup(vector<vector<int>> grid) {
    int n = grid.size();
    if (n == 0 || grid[0][0] == -1 || grid[n-1][n-1] == -1) return 0;
    const int NEG = INT_MIN / 2;
    vector<vector<int>> dp(n, vector<int>(n, NEG));
    dp[0][0] = grid[0][0];
    int maxT = 2*(n-1);
    for (int t = 1; t <= maxT; t++) {
        vector<vector<int>> nd(n, vector<int>(n, NEG));
        int rLo = max(0, t-(n-1)), rHi = min(n-1, t);
        for (int r1 = rLo; r1 <= rHi; r1++) {
            int c1 = t-r1;
            if (c1<0||c1>=n||grid[r1][c1]==-1) continue;
            for (int r2 = rLo; r2 <= rHi; r2++) {
                int c2 = t-r2;
                if (c2<0||c2>=n||grid[r2][c2]==-1) continue;
                int best = NEG;
                for (int pr1 : {r1,r1-1})
                    for (int pr2 : {r2,r2-1})
                        if (pr1>=0&&pr2>=0&&pr1<n&&pr2<n)
                            best = max(best, dp[pr1][pr2]);
                if (best == NEG) continue;
                int ch = grid[r1][c1];
                if (r1 != r2) ch += grid[r2][c2];
                nd[r1][r2] = best + ch;
            }
        }
        dp = nd;
    }
    return max(0, dp[n-1][n-1]);
}

// =====================================================================
// Test runner
// =====================================================================

int passed = 0, failed_count = 0;

void check(int expected, int actual, const string& msg) {
    if (expected == actual) {
        passed++;
    } else {
        failed_count++;
        cout << "FAIL: " << msg << " — expected " << expected << ", got " << actual << endl;
    }
}

int main() {
    cout << "Chapter 24: Dynamic Programming II — Grids and Paths" << endl;
    cout << "=====================================================" << endl << endl;

    // W1
    check(28, ref_unique_paths(3, 7), "W1: (3,7)");
    check(1, ref_unique_paths(1, 1), "W1: (1,1)");
    check(3, ref_unique_paths(3, 2), "W1: (3,2)");
    check(3, ref_unique_paths(2, 3), "W1: (2,3)");
    check(48620, ref_unique_paths(10, 10), "W1: (10,10)");
    check(1, ref_unique_paths(1, 5), "W1: (1,5)");
    check(1, ref_unique_paths(5, 1), "W1: (5,1)");

    // W2
    check(2, ref_unique_paths_obstacles({{0,0,0},{0,1,0},{0,0,0}}), "W2: basic");
    check(1, ref_unique_paths_obstacles({{0,1},{0,0}}), "W2: small");
    check(0, ref_unique_paths_obstacles({{1,0}}), "W2: start blocked");
    check(0, ref_unique_paths_obstacles({{0,0},{0,1}}), "W2: end blocked");
    check(6, ref_unique_paths_obstacles({{0,0,0},{0,0,0},{0,0,0}}), "W2: no obstacle");
    check(1, ref_unique_paths_obstacles({{0}}), "W2: single");

    // W3
    check(7, ref_min_path_sum({{1,3,1},{1,5,1},{4,2,1}}), "W3: basic");
    check(6, ref_min_path_sum({{1,2,3}}), "W3: single row");
    check(6, ref_min_path_sum({{1},{2},{3}}), "W3: single col");
    check(5, ref_min_path_sum({{5}}), "W3: single cell");
    check(7, ref_min_path_sum({{1,2},{3,4}}), "W3: 2x2");

    // W4
    check(11, ref_triangle({{2},{3,4},{6,5,7},{4,1,8,3}}), "W4: basic");
    check(-10, ref_triangle({{-10}}), "W4: single");
    check(-1, ref_triangle({{-1},{2,3},{1,-1,-3}}), "W4: negative");
    check(3, ref_triangle({{1},{2,3}}), "W4: two rows");
    check(0, ref_triangle({{0},{0,0},{0,0,0}}), "W4: zeros");

    // P1
    check(2, ref_unique_paths_iii({{1,0,0,0},{0,0,0,0},{0,0,2,-1}}), "P1: basic");
    check(4, ref_unique_paths_iii({{1,0,0,0},{0,0,0,0},{0,0,0,2}}), "P1: full");
    check(0, ref_unique_paths_iii({{0,1},{2,0}}), "P1: no path");
    check(1, ref_unique_paths_iii({{1,2}}), "P1: minimal");

    // P2
    check(13, ref_min_falling_path({{2,1,3},{6,5,4},{7,8,9}}), "P2: basic");
    check(-59, ref_min_falling_path({{-19,57},{-40,-5}}), "P2: negative");
    check(-48, ref_min_falling_path({{-48}}), "P2: single");
    check(3, ref_min_falling_path({{1,1,1},{1,1,1},{1,1,1}}), "P2: all same");
    check(4, ref_min_falling_path({{1,2},{3,4}}), "P2: 2x2");

    // P3
    check(4, ref_maximal_square({{1,0,1,0,0},{1,0,1,1,1},{1,1,1,1,1},{1,0,0,1,0}}), "P3: basic");
    check(1, ref_maximal_square({{0,1},{1,0}}), "P3: diagonal");
    check(0, ref_maximal_square({{0}}), "P3: zero");
    check(4, ref_maximal_square({{1,1},{1,1}}), "P3: all ones");
    check(1, ref_maximal_square({{1}}), "P3: single one");

    // P4
    check(24, ref_cherry_pickup_ii({{3,1,1},{2,5,1},{1,5,5},{2,1,1}}), "P4: basic");
    check(28, ref_cherry_pickup_ii({{1,0,0,0,0,0,1},{2,0,0,0,0,3,0},{2,0,9,0,0,0,0},{0,3,0,5,4,0,0},{1,0,2,3,0,0,6}}), "P4: large");
    check(4, ref_cherry_pickup_ii({{1,1},{1,1}}), "P4: 2x2");

    // P5
    check(15, ref_count_squares({{0,1,1,1},{1,1,1,1},{0,1,1,1}}), "P5: basic");
    check(7, ref_count_squares({{1,0,1},{1,1,0},{1,1,0}}), "P5: mixed");
    check(5, ref_count_squares({{1,1},{1,1}}), "P5: all ones");
    check(0, ref_count_squares({{0,0},{0,0}}), "P5: all zeros");
    check(1, ref_count_squares({{1}}), "P5: single");

    // C1
    check(7, ref_dungeon({{-2,-3,3},{-5,-10,1},{10,30,-5}}), "C1: basic");
    check(1, ref_dungeon({{0}}), "C1: zero");
    check(1, ref_dungeon({{100}}), "C1: positive");
    check(6, ref_dungeon({{-5}}), "C1: negative");
    check(6, ref_dungeon({{-2,-3,3}}), "C1: single row");

    // C2
    check(6, ref_maximal_rectangle({{1,0,1,0,0},{1,0,1,1,1},{1,1,1,1,1},{1,0,0,1,0}}), "C2: basic");
    check(0, ref_maximal_rectangle({{0}}), "C2: zero");
    check(1, ref_maximal_rectangle({{1}}), "C2: one");
    check(4, ref_maximal_rectangle({{1,1},{1,1}}), "C2: all ones");
    check(3, ref_maximal_rectangle({{1,1,1,0,1}}), "C2: single row");

    // C3
    check(210, ref_ninja_training({{10,40,70},{20,50,80},{30,60,90}}), "C3: basic");
    check(11, ref_ninja_training({{1,2,5},{3,1,1},{3,3,3}}), "C3: small");
    check(10, ref_ninja_training({{10,10,10}}), "C3: single day");
    check(6, ref_ninja_training({{1,2,3},{3,2,1}}), "C3: two days");
    check(15, ref_ninja_training({{5,5,5},{5,5,5},{5,5,5}}), "C3: uniform");

    // C4
    check(5, ref_cherry_pickup({{0,1,-1},{1,0,-1},{1,1,1}}), "C4: basic");
    check(0, ref_cherry_pickup({{1,1,-1},{1,-1,1},{-1,1,1}}), "C4: blocked");
    check(1, ref_cherry_pickup({{1}}), "C4: single");
    check(0, ref_cherry_pickup({{0,0},{0,0}}), "C4: no cherries");
    check(4, ref_cherry_pickup({{1,1},{1,1}}), "C4: all cherries");

    cout << endl;
    if (failed_count == 0) {
        cout << "All " << passed << " tests passed!" << endl;
    } else {
        cout << passed << " passed, " << failed_count << " failed." << endl;
        return 1;
    }
    return 0;
}
