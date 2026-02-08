#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};

void bfs(vector<vector<int>>& heights, queue<pair<int,int>>& q, vector<vector<bool>>& visited) {
    int rows = heights.size(), cols = heights[0].size();
    while (!q.empty()) {
        auto [r, c] = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols
                && !visited[nr][nc] && heights[nr][nc] >= heights[r][c]) {
                visited[nr][nc] = true;
                q.push({nr, nc});
            }
        }
    }
}

vector<vector<int>> solve(vector<vector<int>>& heights) {
    int rows = heights.size(), cols = heights[0].size();
    vector<vector<bool>> pacific(rows, vector<bool>(cols, false));
    vector<vector<bool>> atlantic(rows, vector<bool>(cols, false));
    queue<pair<int,int>> pq, aq;

    for (int c = 0; c < cols; c++) {
        pacific[0][c] = true; pq.push({0, c});
        atlantic[rows-1][c] = true; aq.push({rows-1, c});
    }
    for (int r = 0; r < rows; r++) {
        pacific[r][0] = true; pq.push({r, 0});
        atlantic[r][cols-1] = true; aq.push({r, cols-1});
    }

    bfs(heights, pq, pacific);
    bfs(heights, aq, atlantic);

    vector<vector<int>> result;
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if (pacific[r][c] && atlantic[r][c])
                result.push_back({r, c});
    sort(result.begin(), result.end());
    return result;
}

int main() {
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<int>> heights(rows, vector<int>(cols));
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            cin >> heights[i][j];
    auto result = solve(heights);
    for (auto& cell : result)
        cout << cell[0] << " " << cell[1] << "\n";
    return 0;
}
